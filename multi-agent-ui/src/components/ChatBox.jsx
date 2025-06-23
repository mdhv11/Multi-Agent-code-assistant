import React from "react";
import AgentMessage from "./AgentMessage";

export default function ChatBox({ messages }) {
  return (
    <div className="chat-box">
      {messages.map((msg, index) => (
        <AgentMessage
          key={index}
          sender={msg.sender}
          role={msg.role}
          content={msg.content}
        />
      ))}
    </div>
  );
}
