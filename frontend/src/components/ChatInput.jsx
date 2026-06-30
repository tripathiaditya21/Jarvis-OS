import { useState } from "react";

export default function ChatInput({ onSend }) {
    const [message, setMessage] = useState("");

    const sendMessage = () => {
        if (!message.trim()) return;

        onSend(message);
        setMessage("");
    };

    return (
        <div className="chat-input">
            <input
                type="text"
                placeholder="Ask JARVIS..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") sendMessage();
                }}
            />

            <button onClick={sendMessage}>
                Send
            </button>
        </div>
    );
}