# Model Trial

*[Hydra]: Codename for LLM Studio

Most models in Hydra not only provide descriptive information but also offer an interactive trial feature. For example, you can chat with a large language model to directly experience its capabilities.

## Trial Entry Points

Hydra provides two convenient entry points for model trial. Choose the one that best suits your needs:

- **Option 1:** On the [Model Gallery](./index.md) page, select a model you like and click **Try** to enter the trial interface.
- **Option 2:** From the left menu, click **Model Trial**, select a model type, and begin. Currently supported types are **Text Models** and **Image Models**.

## Trial Overview

When you first enter the **Trial Center**, the system will recommend popular high-quality models for you to try. You can:

- Click on a recommended model to immediately start a chat with it;
- Or select other models of interest from the **Public Models** list;
- If you’ve deployed your own models, you can also try them from the **Model Services** list.

## Model Types

### Text Models

The Trial Center supports pre-configured conversational models, as well as your self-deployed models. Multiple online text models can be selected at once.

### Image Models

Currently supports the preconfigured image generation model `Hidream-l1-Dev`, along with user-deployed services. Only **one** image model can be used in a trial at a time.

### Completing a Full Conversation

Just three steps to complete a trial conversation:

1. On your first visit, choose an API Key. If you don't have one, the platform can auto-generate it for you.
2. Select a model from the list and click it to begin. If you’ve already added a model, you can skip this step and start directly.
3. If you're not satisfied with the response, click **Refresh** to regenerate. Click **Copy** to copy the generated content.

At the bottom of the conversation, the number of tokens used is displayed, which helps evaluate model performance.

## More Conversation Features

Click **Clear Context** in the upper-right of the chat box to end the current session and reset the context — new messages won’t be influenced by previous ones.

## Model Comparison

Click **Add Model** in the top-right to compare up to **three** text-generation models side by side.

## Switching Models

Click the **Switch Model** button in the top information bar to switch to another model.


## Model Parameters

Hydra allows users to adjust various model parameters. Different configurations affect the generated response.  
Click **Model Config** in the top bar to adjust settings.

Hover over the **?** next to each parameter to see its detailed explanation.

| Parameter      | Description |
| -------------- | ----------- |
| System         | System role: Defines the model’s behavior guidelines and background. For example: “You are an AI assistant.” |
| Temperature    | Higher values produce more diverse and random outputs; lower values produce more focused and deterministic responses. Recommended to set **either** this or top_p. |
| TopP           | Controls output diversity. Higher values yield richer responses. Recommended to set **only one** of top_p or temperature. |
| Max_tokens     | Maximum number of tokens the model can generate. Set to 0 for no limit. Suggested values: 500–800 for chat, 800–2000 for short text, 2000–3600 for code, 4000+ for long text. |
| <span style=";color:red">* | Required fields are marked with a red asterisk. |
| Negative Prompt | For image generation: specify content you **do not** want in the output. |
| Guidance scale | Controls how closely the image adheres to the text description. Higher values mean more accurate images; lower values allow more creativity. |
