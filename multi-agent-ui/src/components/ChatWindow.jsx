import AgentMessage from "./AgentMessage";

const ChatWindow = ({ messages }) => {
  return (
    <div className="bg-white p-4 rounded-lg shadow mb-4 max-h-[70vh] overflow-y-auto">
      {messages.map((msg, idx) => (
        <AgentMessage key={idx} role={msg.role} content={msg.content} />
      ))}
    </div>
  );
};

export default ChatWindow;
