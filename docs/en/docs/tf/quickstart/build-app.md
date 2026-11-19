# Build an Intelligent App - User

This tutorial builds a corpus and creates a RAG Q&A application in [AI Applications](../dak/index.md), so the model answers questions based on your private knowledge.

## Prerequisites

- You have signed in to the console with a user that has the AI Applications module permission.
- A business document is ready (e.g. FAQ or product manual), in text or Q&A pair format.

## Steps

1. In the left navigation, click **AI Applications** -> **My Corpus**, then click **Create Corpus**.

2. Enter the basic corpus information and click **Next**:

    - **Corpus Name**: letters, numbers, and symbols, up to 20 characters.
    - **Vectorization Model Service**: select `bge-large-zh` or `bge-large-en`.
    - **Visibility**: public, private, or a specified workspace.
    - **Description**: up to 100 characters.

3. Upload the corpus following the wizard: import local files or online data. After confirmation, the system automatically parses and splits the content into knowledge blocks.
   Once processing completes, you can view the quality and hit rate of the knowledge blocks in the corpus details.

4. In the left navigation, click **App Center**, click **Create**, and choose to create a **RAG application**.

5. Enter the basic app information: upload an app icon (jpg/jpeg/png, no more than 10 MB), an app name (up to 20 characters), and an app description (up to 100 characters).

6. In the AI configuration, select the LLM service (the [deployed model service](deploy-model.md) or an online model), the vectorization model, and the system prompt. Keep the remaining parameters at their defaults.

7. Associate the corpus created in the previous step, then click **OK** to finish.

8. Open the app conversation page and ask questions around the corpus content to verify that the answers are generated from your knowledge base.

## Verification

The conversation answers cite knowledge blocks from the corpus, and app debugging shows the retrieved corpus hits, which means the RAG application is set up successfully.

## Next Step

After putting the app into use, see [Operations and Billing](billing.md). For the complete usage of corpora and applications, see [AI Applications](../dak/index.md).
