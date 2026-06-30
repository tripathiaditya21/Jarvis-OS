export default function Message({ sender, text }) {
    return (
        <div className={`message ${sender}`}>
            <strong>
                {sender === "user" ? "You" : "JARVIS"}
            </strong>

            <p>{text}</p>
        </div>
    );
}