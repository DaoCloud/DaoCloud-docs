# FAQ

??? "Which directories are persisted?"

    ClawOS currently persists files in `/openclaw/data` on a persistent volume. This is OpenClaw's working directory, and FileBrowser uploads are stored there. These files are retained when the Pod restarts or is recreated.

    In the noVNC desktop, the `node` user can create and edit files under `/home/node`, but this directory is not on the persistent volume. Files saved under `/home/node` or elsewhere outside `/openclaw/data` are not guaranteed to survive Pod recreation. To keep files, save them under `/openclaw/data` or upload them there through FileBrowser.

??? "Is my OpenClaw secure?"

    **Yes**

    DaoCloud’s ClawOS is an enterprise-grade “AI agent platform”:

    - Uses container technology as a secure sandbox for each agent
    - Leverages Kubernetes to ensure data security across compute, network, and storage layers
    - All data and conversations are processed through the DCE LLM platform, ensuring sensitive data protection

??? "Can I upload files for OpenClaw to analyze?"

    **Absolutely**

    You can do this in the following ways:

    1. Send files to OpenClaw via Feishu chat
    2. Upload and manage files through the DCE file management interface

??? "OpenClaw instance creation failed"

    Please check:

    1. Whether real-name verification is completed
    2. Whether your account balance is greater than the selected resource price

??? "Feishu integration not working"

    A single Feishu application can only be connected to one OpenClaw instance at a time.

    If you have multiple OpenClaw instances, each one must use a separate App ID and App Secret.
