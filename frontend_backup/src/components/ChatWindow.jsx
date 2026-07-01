import Message from "./Message";

export default function ChatWindow({ messages }) {
    return (
        <div className="chat-window">
            {messages.map((msg, index) => (
                <Message
                    key={index}
                    sender={msg.sender}
                    text={msg.text}
                />
            ))}
        </div>
    );
}