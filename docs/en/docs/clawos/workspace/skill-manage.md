# Skill Management

Skill Management is the administration entry in ClawHub for workspace administrators. Workspace administrators can publish, edit, unlist, or delete Skills within their workspace. After a Skill passes review, it appears in the **Private Skills** category of the **Skill Marketplace**.

After a Skill is published, it must go through a review process. Once approved, the Skill becomes available in the **Private Skills** marketplace of the current workspace and can only be viewed and used by members of that workspace.

## Viewing the Skill List

Navigate to **ClawHub > Skill Management** to view all Skills that have been created or published within the current workspace.

Common statuses include:

| Status | Description |
| ------ | ----------- |
| **Published** | The Skill has passed review and is available for workspace members to view and use in the Private Skills marketplace |
| **Under Review** | The Skill publication request has been submitted and is awaiting review |
| **Review Failed** | The Skill did not pass the review and must be modified and resubmitted |
| **Unlisted** | The Skill is temporarily hidden from workspace members and can no longer be installed |

## Publishing a Skill

1. Click **Publish Skill** in the upper-right corner to enter the publishing page.

2. Fill in the following information:

    * **Skill Name**: The name displayed in the Skill Marketplace. It is recommended to use a concise and descriptive name.
    * **Version**: The version identifier for this release.
    * **Skill File**: Upload the Skill package.

3. After the upload is complete, click **Submit and Publish** to initiate the review workflow.

After the review is approved, the Skill appears in the **Private Skills** marketplace of the current workspace.

## Skill File Requirements

The uploaded Skill file is typically provided as a compressed package. The package should contain the documentation, configuration files, scripts, and dependency declarations required to run the Skill.

It is recommended to include at least:

* Skill documentation
* Manifest configuration file
* Entry script or tool definitions
* Dependency declarations
* Examples or a README file

!!! note

    The package contents should not contain sensitive information such as plaintext keys, account passwords, internal Tokens, or similar credentials.

## Editing a Skill

For existing Skills, administrators can click **Edit** to modify the Skill information.

The original file name cannot be changed during editing. Only the content can be modified and resubmitted. If the Skill file or version content is changed, the Skill typically needs to go through the review process again. The new version becomes available to workspace members only after the review is approved.

## Unlisting a Skill

If you no longer want workspace members to install a Skill temporarily, you can **Unlist** it.

After a Skill is unlisted, it no longer appears in the Private Skills marketplace, and new users cannot install it. Whether the Skill remains available in OpenClaw instances where it has already been installed depends on platform policies and instance-side behavior.

## Deleting a Skill

Deleting a Skill removes the Skill record permanently. Before deleting a Skill, ensure that it is no longer needed and that no users depend on it for daily work.

If the Skill is still being used by multiple OpenClaw instances, it is recommended to unlist the Skill first and notify the affected users before deletion.

## Viewing Published Skills

After a Skill passes review, both administrators and workspace members can find it under **Skill Marketplace > Private Skills**. On the details page, users can view the overview, files, versions, and installation instructions. Members can then follow the installation instructions to install and use the Skill in OpenClaw instances.

For more information, see [Skill Marketplace](./skill.md).
