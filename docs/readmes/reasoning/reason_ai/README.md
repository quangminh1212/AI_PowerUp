<!-- source: https://github.com/MinecraftPublisher/reason_ai.git sha: d7ee9c793716d5f8623e4ec7059359ae0150a315 readme: master/README.md -->
# MinecraftPublisher/reason_ai

ReasonAI - AI chat with rudimentary chain-of-thought reasoning

---

# ReasonAI
This is a very basic project that uses [PollinationsAI](https://pollinations.ai/) to generate images and text. The AI model is instructed to be able to use HTML and also have a chain-of-thought reasoning (like deepseek-r1 but worse) (which is hidden in a `<think></think>` element).

ReasonAI also supports a summarization feature which means the AI should theoretically keep a context as to what information was exchanged before, even after a ton of long messages.

To generate an image, simply ask it to generate an image for you.