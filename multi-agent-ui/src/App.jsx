import React, { useState, useRef, useEffect } from "react";
import ChatBox from "./components/ChatBox";
import ChatInput from "./components/ChatInput";
import "./App.css";

const App = () => {
  const [messages, setMessages] = useState([]);
  const [socket, setSocket] = useState(null);
  const chatEndRef = useRef(null);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/generate");
    setSocket(ws);

    ws.onmessage = (event) => {
      const parsed = JSON.parse(event.data);
      setMessages((prev) => [...prev, parsed]);
    };

    ws.onerror = (err) => {
      console.error("WebSocket error:", err);
    };

    ws.onclose = () => {
      console.log("WebSocket closed");
    };

    return () => {
      ws.close();
    };
  }, []);

  const handleSend = (task) => {
    if (!socket || socket.readyState !== WebSocket.OPEN) return;

    const userMessage = {
      sender: "You",
      role: "user",
      content: task,
    };
    setMessages((prev) => [...prev, userMessage]);
    socket.send(task);
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="app">
      <h1 className="header">🧠 Multi-Agent Code Assistant</h1>
      <ChatBox messages={messages} chatEndRef={chatEndRef} />
      <ChatInput onSend={handleSend} />
    </div>
  );
};

export default App;
