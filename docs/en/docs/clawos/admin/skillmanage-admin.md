# Skill Management (Administrator View)

Skill Management from the platform administrator perspective serves as the platform-level supply and governance console of ClawHub for publishing, reviewing, listing, unlisting, and maintaining **public Skills**.

Platform administrators do not consume Skills and do not need to install Skills from the Skill Marketplace. Therefore, the administrator console does not provide access to the Skill Marketplace and only offers Skill management capabilities. Skills published and listed by platform administrators are added to the **Public Skills** section of the ClawHub **Skill Marketplace** in all workspaces, where all workspace members can install and use them.

!!! note

    For instructions on publishing private Skills by workspace administrators, see the Skill Management documentation from the workspace perspective.

## Roles and Responsibilities

### Platform Administrators

Platform administrators are responsible for maintaining the platform's public Skill offerings, including:

* Publishing new Skills
* Uploading Skill packages
* Viewing the list of published Skills
* Editing Skill metadata and versions
* Initiating or processing Skill reviews
* Viewing automatic security scan results
* Listing Skills in the public marketplace
* Unlisting Skills from the public marketplace
* Deleting unpublished or no longer needed Skills

### Workspace Members

Workspace members do not appear in the administrator console. They can only discover public Skills in the ClawHub **Skill Marketplace** from the workspace perspective and install and use them within their workspaces.

### Workspace Administrators

Workspace administrators can install, enable, disable, configure, or uninstall Skills within their workspaces, but they cannot publish platform-level public Skills or bypass the platform review process.

## Publishing a Skill

1. Click **Publish Skill** to enter the publishing page.

2. Fill in the Skill information, upload the Skill package, and submit the publication request.

After submission, the system creates a Skill record and enters the review workflow. The Skill will **not immediately** appear in the workspace Skill Marketplace.

### Status Flow After Publishing

1. The platform administrator fills in the information and uploads the Skill package.
2. The system creates a Skill draft.
3. The system automatically initiates a security scan.
4. After the security scan is completed, the Skill enters the Pending Review state.
5. A platform administrator or reviewer performs the review.
6. After approval, the Skill enters the Unlisted state.
7. The platform administrator lists the Skill.
8. The Skill appears in the **Public Skills** section of the ClawHub Skill Marketplace in all workspaces.

## Listing and Unlisting

### Listing

Platform administrators can list approved Skills. After a Skill is listed:

* The Skill status changes to **Listed**
* The Skill becomes available in the ClawHub Skill Marketplace of all workspaces
* The Skill is categorized as a **Public Skill** in the marketplace
* All workspace members can view, install, and use the Skill
* Workspaces that have installed the Skill can continue to manage, enable, disable, and configure it within the workspace

### Unlisting

Platform administrators can unlist a listed Skill. After a Skill is unlisted:

* The Skill is removed from the **Public Skills** list in the ClawHub Skill Marketplace of all workspaces
* New workspaces can no longer install the Skill
* Whether the Skill remains available in workspaces that have already installed it depends on the platform policy
* Unlisting does not immediately uninstall the Skill; existing installations can continue using the current version
* Workspaces can no longer create new instances of the Skill or upgrade to the unlisted version
