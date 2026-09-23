import os
import gradio as gr
import ollama
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "gemma3:1b")
HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")

client = ollama.Client(host=HOST)


def chat(message, history):
    if not message.strip():
        return "", history

    messages = [
        {"role": "system", "content": "You are a helpful and concise voice AI assistant."}
    ]

    for item in history:
        if isinstance(item, dict):
            role = item.get("role")
            content = item.get("content")

            if role in ["user", "assistant"] and isinstance(content, str):
                messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": message})

    try:
        response = client.chat(
            model=MODEL,
            messages=messages
        )
        answer = response["message"]["content"]
    except Exception as e:
        answer = f"Ollama error: {e}"

    history = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": answer}
    ]

    return "", history


HEAD = """
<script>
window.startVoice = function() {

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Please use Google Chrome or Microsoft Edge.");
        return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = function(event) {

        const text = event.results[0][0].transcript;

        const textbox =
            document.querySelector("#message-box textarea");

        if (!textbox) return;

        const setter =
            Object.getOwnPropertyDescriptor(
                HTMLTextAreaElement.prototype,
                "value"
            ).set;

        setter.call(textbox, text);

        textbox.dispatchEvent(
            new Event("input", { bubbles: true })
        );

        setTimeout(function() {

            const button =
                document.querySelector("#send-button button");

            if (button) {
                button.click();
            }

        }, 500);
    };

    recognition.onerror = function(event) {
        console.log("Voice error:", event.error);
    };

    recognition.start();
};


window.speakText = function(text) {

    if (!text) return;

    speechSynthesis.cancel();

    const utterance =
        new SpeechSynthesisUtterance(text);

    utterance.lang = "en-US";
    utterance.rate = 1;
    utterance.pitch = 1;

    speechSynthesis.speak(utterance);
};


let lastSpoken = "";

function watchChat() {

    const chatbot =
        document.querySelector("#chatbot");

    if (!chatbot) {
        setTimeout(watchChat, 500);
        return;
    }

    const observer =
        new MutationObserver(function() {

            const messages =
                chatbot.querySelectorAll(".message");

            if (!messages.length) return;

            const last =
                messages[messages.length - 1];

            const text =
                last.innerText.trim();

            if (!text || text === lastSpoken) return;

            if (text.startsWith("You:")) return;

            lastSpoken = text;

            window.speakText(text);
        });

    observer.observe(chatbot, {
        childList: true,
        subtree: true
    });
}

setTimeout(watchChat, 1000);
</script>
"""


with gr.Blocks() as app:

    gr.Markdown("# 🤖 Local Voice AI")

    chatbot = gr.Chatbot(
        height=500,
        elem_id="chatbot"
    )

    with gr.Row():

        message = gr.Textbox(
            placeholder="Type or speak...",
            elem_id="message-box",
            scale=7
        )

        send = gr.Button(
            "Send",
            elem_id="send-button",
            scale=1
        )

        voice = gr.Button(
            "🎤 Speak",
            scale=1
        )

    send.click(
        chat,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )

    message.submit(
        chat,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )

    voice.click(
        None,
        js="() => window.startVoice()"
    )


app.launch(
    server_name="127.0.0.1",
    server_port=7860,
    head=HEAD
)