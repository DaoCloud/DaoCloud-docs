# System Configuration

!!! note

    The parameters in the system configuration will serve as default parameters when creating apps.

<!-- ![System-config](./images/system-config.png) -->

## Conversation Memory Rounds

This refers to the number of rounds or turns used to track and manage conversation history in a chat system. Each time a user interacts with the system, the conversation round count increases by one. Here, it indicates that when a user interacts with the conversation app, it will retain a portion of the conversation history in a small memory window for a certain period, with the size of the memory rounds determining the duration of retention.

- Default value is 10
- Minimum value is 0

## Corpus Prompt Template

This template is activated when the app is associated with a template. The template content includes knowledge blocks obtained through similarity search, user inputs, and embedded prompt templates.

## Embedded Prompt Template

The embedded prompts are concatenated before the user's question as a general convention to guide the app model in generating responses to the question.
