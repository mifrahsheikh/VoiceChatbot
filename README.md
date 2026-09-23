# Local Voice AI Chatbot

A local voice-enabled AI chatbot built with **Python, Gradio, Ollama, and a local LLM**.

The application allows you to interact with an AI assistant in two ways:

* Type messages using the chat interface
* Speak using your microphone
* Hear the AI response using browser text-to-speech

The AI runs locally through **Ollama**, so the chatbot can work without sending conversations to a cloud AI API.

---

## Features

* Text-based AI chat
* Speech-to-text using the browser's Web Speech API
* Text-to-speech using the browser's Speech Synthesis API
* Local LLM inference using Ollama
* Runs locally on your computer
* Maintains conversation history
* Model configuration through environment variables
* Simple Gradio web interface

---

## Technologies Used

| Technology           | Purpose                                   |
| -------------------- | ----------------------------------------- |
| Python               | Application logic                         |
| Gradio               | Web interface                             |
| Ollama               | Runs the local LLM                        |
| Gemma 3 1B           | Default local AI model                    |
| Web Speech API       | Speech-to-text                            |
| Speech Synthesis API | Text-to-speech                            |
| python-dotenv        | Environment configuration                 |
| uv                   | Python package and environment management |

---

## How It Works

```text
                 User
                  |
          +-------+-------+
          |               |
       Type            Speak
          |               |
          +-------+-------+
                  |
                  v
             Gradio UI
                  |
                  v
              agent.py
                  |
                  v
               Ollama
                  |
                  v
            Local LLM Model
             (Gemma 3 1B)
                  |
                  v
             AI Response
                  |
          +-------+-------+
          |               |
       Display          Speak
```

The browser handles voice input and output, while **Ollama handles the AI generation locally**.

---

## Requirements

Before running the project, install:

* Python 3.13+
* Git
* uv
* Ollama
* Google Chrome or Microsoft Edge

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd VoiceChatbot
```

### 2. Install dependencies

Using `uv`:

```bash
uv sync
```

This installs the dependencies defined in `pyproject.toml`.

---

## Ollama Setup

Install Ollama on your computer and make sure it is running.

Download the default model:

```bash
ollama pull gemma3:1b
```

Check your installed models:

```bash
ollama list
```

Test the model:

```bash
ollama run gemma3:1b
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
OLLAMA_MODEL=gemma3:1b
OLLAMA_HOST=http://127.0.0.1:11434
```

The application uses these variables to determine which Ollama model and server to connect to.

Do not commit your `.env` file to GitHub if it contains secrets or private configuration.

Add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

## Run the Application

Start the Gradio application with:

```bash
uv run python agent.py
```

The application will run on:

```text
http://127.0.0.1:7860
```

Open this address in your browser.

---

## Voice Input

1. Open the application in Chrome or Microsoft Edge.
2. Click the Speak button.
3. Allow microphone access when the browser asks.
4. Speak your question.
5. The browser converts your speech into text.
6. The message is automatically sent to the AI.
7. The AI response is displayed in the chat.
8. The response is automatically spoken using browser text-to-speech.

---

## Text-to-Speech

The project uses the browser's built-in:

```text
SpeechSynthesis API
```

The AI response is detected in the chat interface and converted into speech.

No external text-to-speech API is required.

---

## Local AI Architecture

This project uses **Ollama** to run the language model locally.

```text
Gradio
   |
   v
Python
   |
   v
Ollama Python Client
   |
   v
Ollama Server
   |
   v
Gemma 3 1B
   |
   v
AI Response
```

Because the model runs locally, the conversation does not need to be sent to OpenAI, Anthropic, or another cloud LLM provider.

However, the model's knowledge is limited to what is contained in its training data. It does not automatically have access to live internet information.

---

## Project Structure

```text
VoiceChatbot/
|
├── agent.py
├── README.md
├── pyproject.toml
├── .python-version
├── .gitignore
├── .env
|
└── src/
    └── voicechatbot/
        └── __init__.py
```

### agent.py

Contains the main chatbot application, including:

* Ollama connection
* Chat logic
* Conversation history
* Gradio interface
* Browser speech recognition
* Browser text-to-speech

### pyproject.toml

Contains the project's Python dependencies and package configuration.

### .env

Stores local configuration such as the Ollama model and server address.

---

## Changing the AI Model

You can use another model installed in Ollama.

Check available models:

```bash
ollama list
```

For example:

```text
gemma3:1b
gemma3
qwen3.5
```

Then change `.env`:

```env
OLLAMA_MODEL=qwen3.5
```

Restart the application after changing the model.

---

## Troubleshooting

### Ollama Connection Error

Make sure Ollama is running.

Check:

```bash
ollama list
```

You can also start the Ollama server:

```bash
ollama serve
```

The default Ollama address is:

```text
http://127.0.0.1:11434
```

### Microphone Does Not Work

Make sure:

* You are using Chrome or Microsoft Edge.
* The browser has microphone permission.
* Your computer has a working microphone.
* You clicked the Speak button.

### Model Not Found

Check:

```bash
ollama list
```

If `gemma3:1b` is missing:

```bash
ollama pull gemma3:1b
```

---

## Learning Goals

This project was built to understand practical AI application development, including:

* Python AI application development
* LLM integration
* Local LLMs
* Ollama
* Prompt construction
* Conversation history
* Environment variables
* Gradio interfaces
* Speech-to-text
* Text-to-speech
* Local AI architecture

---

## Future Improvements

Possible improvements include:

* Better voice activity detection
* Streaming AI responses
* Higher-quality speech recognition
* More natural text-to-speech voices
* RAG for custom documents
* PDF and document question answering
* AI tool calling
* Agentic AI capabilities
* Persistent conversation history
* Optional web search
* Authentication
* Cloud deployment

---

## License

This project is intended for learning and experimentation with local AI technologies.