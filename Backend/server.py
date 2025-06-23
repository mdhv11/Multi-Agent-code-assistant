import asyncio
import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from autogen_core import TRACE_LOGGER_NAME, FunctionCall
from autogen_agentchat.messages import TextMessage
from code_gen import build_agent_team

load_dotenv()
app = FastAPI()
logger = logging.getLogger(TRACE_LOGGER_NAME)
logger.setLevel(logging.INFO)

CORS_ORIGINS = ["http://localhost:5173"]  # Adjust as per your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws/generate")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info("connection open")

    try:
        task = await websocket.receive_text()

        # Send the user's prompt as the first message
        await websocket.send_json({
            "sender": "User",
            "role": "user",
            "content": task
        })

        team, openai_client = await build_agent_team(task)
        try:
            async for message in team.run_stream(task=task):
                # Handle different message types
                if isinstance(message, TextMessage):
                    sender_name = getattr(message, 'source', 'Unknown')
                    await websocket.send_json({
                        "sender": sender_name,
                        "role": "assistant",
                        "content": str(message.content),
                    })
                elif isinstance(message, FunctionCall):
                    await websocket.send_json({
                        "sender": "System",
                        "role": "system",
                        "content": f"Calling function: {message.name}",
                    })
                elif hasattr(message, "content") and message.content:
                    # Fallback for other message types with content
                    sender_name = getattr(message, 'source', 'Unknown')
                    if hasattr(message, 'sender') and hasattr(message.sender, 'name'):
                        sender_name = message.sender.name

                    await websocket.send_json({
                        "sender": sender_name,
                        "role": "assistant",
                        "content": str(message.content),
                    })
        finally:
            # Try to close the client gracefully
            try:
                await openai_client.close()
            except Exception as e:
                logger.warning(f"Error closing client: {e}")

    except WebSocketDisconnect:
        logger.info("connection closed")
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}")
        try:
            await websocket.send_json({
                "sender": "System",
                "role": "error",
                "content": f"An error occurred: {str(e)}"
            })
        except:
            pass  # WebSocket might already be closed
        finally:
            await websocket.close()
