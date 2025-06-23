import { Light as SyntaxHighlighter } from "react-syntax-highlighter";
import python from "react-syntax-highlighter/dist/esm/languages/hljs/python";
import docco from "react-syntax-highlighter/dist/esm/styles/hljs/docco";
import remarkGfm from "remark-gfm";
import ReactMarkdown from "react-markdown";

SyntaxHighlighter.registerLanguage("python", python);

const AgentMessage = ({ role, content }) => {
  return (
    <div className="mb-3">
      <div className="font-semibold text-indigo-600">{role}</div>
      <div className="bg-gray-100 p-2 rounded whitespace-pre-wrap">
        <ReactMarkdown
          children={content}
          remarkPlugins={[remarkGfm]}
          components={{
            code({ inline, className, children, ...props }) {
              const match = /language-(\w+)/.exec(className || "");
              return !inline && match ? (
                <SyntaxHighlighter
                  children={String(children).replace(/\n$/, "")}
                  language={match[1]}
                  style={docco}
                  PreTag="div"
                  {...props}
                />
              ) : (
                <code className="bg-gray-200 px-1 rounded" {...props}>
                  {children}
                </code>
              );
            },
          }}
        />
      </div>
    </div>
  );
};

export default AgentMessage;
