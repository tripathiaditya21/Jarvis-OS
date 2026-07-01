import { useState } from "react";
import api from "./services/api";

import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

import "./App.css";

export default function App() {

    const [messages, setMessages] = useState([]);

    async function send(message) {

        setMessages((prev) => [
            ...prev,
            {
                sender: "user",
                text: message,
            },
        ]);

        try {

            const response = await api.get("/chat", {
                params: {
                    message,
                },
            });

            setMessages((prev) => [
                ...prev,
                {
                    sender: "jarvis",
                    text: response.data.reply,
                },
            ]);

        } catch (error) {

            setMessages((prev) => [
                ...prev,
                {
                    sender: "jarvis",
                    text: "Unable to connect to JARVIS.",
                },
            ]);

        }
    }

    return (
        <div className="app">

            <h1>🤖 JARVIS OS</h1>

            <ChatWindow messages={messages} />

            <ChatInput onSend={send} />

        </div>
    );
}