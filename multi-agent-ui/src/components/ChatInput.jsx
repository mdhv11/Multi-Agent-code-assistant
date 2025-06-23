import { useState } from "react";

const ChatInput = ({ onSend, loading }) => {
  const [task, setTask] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!task.trim()) return;
    onSend(task);
    setTask("");
  };

  return (
    <form onSubmit={handleSubmit} className="flex items-center gap-2">
      <input
        type="text"
        className="flex-1 border border-gray-300 p-2 rounded"
        placeholder="Describe your coding task..."
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        disabled={loading}
      >
        {loading ? "Working..." : "Send"}
      </button>
    </form>
  );
};

export default ChatInput;
