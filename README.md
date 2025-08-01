# Multi-Agent Code Assistant

A sophisticated AI-powered code generation and review system that leverages multiple specialized agents working collaboratively to create, review, and test Python code.

## 🚀 Project Overview

The Multi-Agent Code Assistant is a full-stack web application that demonstrates the power of collaborative AI agents in software development. The system uses a team of specialized AI agents (Coder, Reviewer, and Tester) that work together to generate high-quality, tested Python code based on user requirements.

## ✨ Key Features

### 🤖 Multi-Agent Collaboration

- **Coder Agent**: Generates Python code based on user specifications
- **Reviewer Agent**: Reviews code for correctness, efficiency, and best practices
- **Tester Agent**: Creates comprehensive test cases for the generated code
- **Real-time Collaboration**: Agents communicate and hand off tasks seamlessly

### 💻 Modern Web Interface

- **Real-time Chat Interface**: WebSocket-based communication for instant responses
- **Code Syntax Highlighting**: Beautiful syntax highlighting for Python code
- **Markdown Support**: Rich text formatting with GitHub Flavored Markdown
- **Responsive Design**: Modern UI built with React and Tailwind CSS

### 🔧 Technical Capabilities

- **Streaming Responses**: Real-time message streaming from AI agents
- **Error Handling**: Robust error handling and graceful degradation
- **CORS Support**: Cross-origin resource sharing for development
- **Environment Configuration**: Secure API key management

## 🏗️ Architecture

### Backend (Python/FastAPI)

```
Backend/
├── server.py          # FastAPI WebSocket server
├── code_gen.py        # Agent team configuration
├── requirements.txt   # Python dependencies
└── venv/             # Virtual environment
```

**Technologies:**

- **FastAPI**: Modern, fast web framework for building APIs
- **AutoGen**: Microsoft's framework for building multi-agent systems
- **OpenAI GPT-4**: Advanced language model for code generation
- **WebSockets**: Real-time bidirectional communication
- **Python-dotenv**: Environment variable management

### Frontend (React/Vite)

```
multi-agent-ui/
├── src/
│   ├── App.jsx              # Main application component
│   │   ├── ChatBox.jsx      # Message display component
│   │   ├── ChatInput.jsx    # User input component
│   │   └── AgentMessage.jsx # Individual message component
│   └── assets/              # Static assets
├── package.json             # Node.js dependencies
└── vite.config.js          # Vite configuration
```

**Technologies:**

- **React 19**: Latest React with modern hooks and features
- **Vite**: Fast build tool and development server
- **Tailwind CSS**: Utility-first CSS framework
- **React Markdown**: Markdown rendering with syntax highlighting
- **Socket.io-client**: WebSocket client for real-time communication

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+ with pip
- Node.js 18+ with npm
- OpenAI API key

### Backend Setup

1. **Navigate to the backend directory:**

   ```bash
   cd Backend
   ```

2. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the Backend directory:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Start the backend server:**
   ```bash
   python server.py
   ```
   The server will run on `http://localhost:8000`

### Frontend Setup

1. **Navigate to the frontend directory:**

   ```bash
   cd multi-agent-ui
   ```

2. **Install Node.js dependencies:**

   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```
   The frontend will run on `http://localhost:5173`

## 🎯 Usage

### Basic Workflow

1. **Open the Application**: Navigate to `http://localhost:5173` in your browser
2. **Enter Your Request**: Type a description of the Python code you want to generate
3. **Watch the Collaboration**: Observe as the three agents work together:
   - **Coder** generates the initial code
   - **Reviewer** evaluates and suggests improvements
   - **Tester** creates comprehensive test cases
4. **Get Your Result**: Receive fully tested, reviewed Python code

### Example Requests

- "Create a function to calculate the factorial of a number"
- "Write a class to manage a simple bank account with deposit and withdrawal methods"
- "Generate a script to read CSV files and perform data analysis"
- "Create a decorator that measures function execution time"

### Agent Roles & Responsibilities

#### 🧑‍💻 Coder Agent

- **Primary Role**: Code generation
- **Responsibilities**:
  - Write clean, functional Python code
  - Follow Python best practices and PEP 8
  - Provide code in markdown code blocks
  - Hand off to Reviewer when complete

#### 🔍 Reviewer Agent

- **Primary Role**: Code review and quality assurance
- **Responsibilities**:
  - Review code for correctness and efficiency
  - Suggest improvements and optimizations
  - Ensure code follows best practices
  - Approve code or request revisions

#### 🧪 Tester Agent

- **Primary Role**: Test case generation
- **Responsibilities**:
  - Create comprehensive test cases
  - Cover edge cases and error conditions
  - Provide clear test documentation
  - Ensure code reliability

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the Backend directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### CORS Configuration

The backend is configured to allow requests from `http://localhost:5173`. To modify this, edit the `CORS_ORIGINS` list in `server.py`.

### Agent Configuration

Agent behavior can be customized by modifying the system messages in `code_gen.py`:

- **Coder System Message**: Controls code generation style and requirements
- **Reviewer System Message**: Defines review criteria and standards
- **Tester System Message**: Specifies test case requirements

## 🚀 Deployment

### Production Considerations

1. **Environment Variables**: Use proper environment variable management
2. **CORS Configuration**: Update CORS origins for production domains
3. **WebSocket Security**: Implement proper WebSocket authentication
4. **API Rate Limiting**: Add rate limiting for OpenAI API calls
5. **Error Monitoring**: Implement proper logging and error tracking

### Docker Deployment

Create a `Dockerfile` for containerized deployment:

```dockerfile
# Backend Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Microsoft AutoGen**: For the multi-agent framework
- **OpenAI**: For the GPT-4 language model
- **FastAPI**: For the modern Python web framework
- **React**: For the frontend framework
- **Tailwind CSS**: For the utility-first CSS framework

## 📞 Support

For support and questions:

- Create an issue in the GitHub repository
- Check the documentation for common issues
- Review the code examples and configuration options

---

**Built with ❤️ hope you like it, im working on a better UI**
