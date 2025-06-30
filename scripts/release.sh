#!/bin/bash
#

# Copyright DaoCloud authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http:/www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script checks if the English version of a page has changed since a localized
# page has been committed.
# Usage:
# This script fetches release notes from GitHub repositories and generates markdown files.
#
# Environment variables required:
# - GH_TOKEN: GitHub access token for API authentication
# - PROJECT_REPO: Repository to fetch release notes from (format: owner/repo)
# - PROJECT_NAME: Name of the project (used for file naming)
# - PROJECT_EN_RELEASE_NOTES_PATH: Path to store English release notes（e.g., docs/en/docs/network/modules/spiderpool）
# - PROJECT_ZH_RELEASE_NOTES_PATH: Path to store Chinese release notes (optional)
# - MIN_SYNC_RELEASE_PROJECT_VERSION: Minimum version to sync from
#
# Example:
# GH_TOKEN=your_token PROJECT_REPO=spidernet-io/spiderpool PROJECT_NAME=spiderpool \
# PROJECT_EN_RELEASE_NOTES_PATH=docs/en/docs/network/modules/spiderpool/release-notes \
# MIN_SYNC_RELEASE_PROJECT_VERSION=v0.6.0 ./scripts/release.sh
#
# Output:
# The script will generate markdown files in the specified PROJECT_EN_RELEASE_NOTES_PATH
# with filenames matching the tag versions (e.g., v1.0.0.md, v1.0.1.md).
# Each file will contain the formatted release notes for that version.
# 本脚本用于自动从 GitHub Release Notes 中提取指定项目的 release notes，（从给定的最小同步tag开始，到最新tag结束）
# 会在 docs/en/docs/network/modules/{PROJECT_NAME}下自动创建 release-notes 文件夹，将 release notes 存放在
# release-notes 文件夹中
# !! 目前由网络组人维护，请不要随意修改和删除！

PROJECT_DIR=$(
    cd "$(dirname "$0")"
    pwd
)

if ! command -v jq &>/dev/null; then
    echo "jq is required but not installed. Installing jq..."
    apt-get update && apt-get install -y jq
fi

# Set up temporary directory for git operations
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

if [ -z "$GH_TOKEN" ]; then
    echo "GH_TOKEN is not set"
    exit 1
fi

if [ -z "$PROJECT_REPO" ]; then
    echo "PROJECT_REPO is not set"
    exit 1
fi

if [ -z "$MIN_SYNC_RELEASE_PROJECT_VERSION" ]; then
    echo "MIN_SYNC_RELEASE_PROJECT_VERSION is not set"
    exit 1
fi

if [ -z "$PROJECT_NAME" ]; then
    echo "PROJECT_NAME is not set"
    exit 1
fi

if [ -z "$PROJECT_EN_RELEASE_NOTES_PATH" ]; then
    echo "PROJECT_EN_RELEASE_NOTES_PATH is not set"
    exit 1
fi

if [ -z "$PROJECT_ZH_RELEASE_NOTES_PATH" ]; then
    echo "PROJECT_ZH_RELEASE_NOTES_PATH is not set"
fi

# Create release-notes directory if it doesn't exist
RELEASE_NOTES_DIR="${PROJECT_EN_RELEASE_NOTES_PATH}/release-notes"
mkdir -p "$RELEASE_NOTES_DIR"

# Function to fetch release notes for a specific tag
fetch_release_notes() {
    local tag=$1

    # Extract major.minor version from the tag
    # Remove 'v' prefix if present
    local version=${tag#v}

    # Extract major and minor version numbers
    local major_minor=$(echo "$version" | grep -oE '^[0-9]+\.[0-9]+')

    if [ -z "$major_minor" ]; then
        echo "Warning: Could not extract major.minor version from tag: $tag"
        # Fallback to using the tag directly
        major_minor="$version"
    fi

    # Create directory for this major.minor version
    local version_dir="$RELEASE_NOTES_DIR/release-$major_minor"
    mkdir -p "$version_dir"

    local output_file="$version_dir/${tag}.md"

    echo "Fetching release notes for tag: $tag"

    # Use GitHub API to fetch release notes
    # Extract the owner and repo from PROJECT_REPO (format: owner/repo)
    IFS='/' read -r owner repo <<<"$PROJECT_REPO"

    # Try to get the release for this specific tag
    echo "Fetching release for tag: $tag"
    release_info=$(curl -s "https://api.github.com/repos/$owner/$repo/releases/tags/$tag" -H "Authorization: Bearer $GH_TOKEN")

    # If we get a "Not Found" message, try to get release info from the tag's commit
    if echo "$release_info" | grep -q "message": "Not Found" &>/dev/null; then
        echo "No release found for tag: $tag."
        return 1
    else
        # Extract the release body from the release info
        release_body=$(echo "$release_info" | jq -r '.body')
    fi

    # Check if we found a release for this tag
    if [ -z "$release_body" ] || [ "$release_body" = "null" ]; then
        echo "No release found for tag: $tag. Creating placeholder."
        release_body="No release notes available for $tag"
        return 1
    fi

    # release_body is already extracted using jq above

    # Create the markdown file with the release notes
    echo "# Release Notes for $tag" >"$output_file"
    echo "" >>"$output_file"
    echo "$release_body" >>"$output_file"

    echo "Release notes saved to: $output_file"
}

# Get all tags sorted by version
echo "Fetching tags from repository: $PROJECT_REPO"
IFS='/' read -r owner repo <<<"$PROJECT_REPO"

echo "curl --retry 10 -s https://api.github.com/repos/$owner/$repo/tags -H \"Authorization: Bearer $GH_TOKEN\""
response=$(curl --retry 10 -s https://api.github.com/repos/$owner/$repo/tags -H "Authorization: Bearer $GH_TOKEN")

# Check if the response is empty or contains an error
if [ -z "$response" ]; then
    echo "Error: Empty response from GitHub API. Check your network connection."
    exit 1
fi

# Extract tag names from the response using jq
all_tags=$(echo "$response" | jq -r '.[].name')

if [ -z "$all_tags" ]; then
    echo "Error: No tags found for $PROJECT_NAME repository."
    exit 1
fi

echo "all_tags: ${all_tags}"

# Filter tags that are greater than or equal to MIN_SYNC_RELEASE_PROJECT_VERSION
# This uses a simple version comparison, assuming semantic versioning
for tag in $all_tags; do
    # Remove 'v' prefix if present for comparison
    tag_version=${tag#v}
    min_version=${MIN_SYNC_RELEASE_PROJECT_VERSION#v}

    # Skip release candidate tags
    if [[ "$tag" == *"rc"* ]] || [[ "$tag" == *"RC"* ]] || [[ "$tag" == *"alpha"* ]] || [[ "$tag" == *"beta"* ]]; then
        echo "Skipping release candidate tag: $tag"
        continue
    fi

    # Compare versions
    if [ "$(printf '%s\n' "$min_version" "$tag_version" | sort -V | head -n1)" = "$min_version" ] &&
        [ "$min_version" != "$tag_version" ]; then
        echo "Processing tag: $tag"
        fetch_release_notes "$tag"
    fi
done

echo "Release notes extraction completed."
