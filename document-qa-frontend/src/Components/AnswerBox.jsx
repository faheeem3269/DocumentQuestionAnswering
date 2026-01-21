import React, { useState } from "react";
import { useSelector } from "react-redux";


const AnswerBox = () => {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hi! How can I help you today?" },
  ]);
  const[loading,setloading]=useState(false);
  const[response,setresponse]=useState([]);
   const file = useSelector((state) => state.file.file)
  const [input, setInput] = useState("");
  const [question, setQuestion] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    setloading(true);
    const res = await fetch('http://127.0.0.1:8000/api/askquestion', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question: input }),
  });
   const data = await res.json();
   console.log(data.question);
   setresponse(prev=>([...prev,{"question":input,"answer":data.question}]));
   setloading(false);
  
    setQuestion((prev) => [...prev, input]);
    setInput("");
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
     <aside className="hidden md:flex w-64 bg-white border-r p-4 flex-col">
          <h2 className="text-lg font-semibold mb-6 justify-center">AI Chat</h2>

        <div className="flex flex-col flex-1 overflow-y-auto gap-2 text-sm font-normal">
          <div className="text-left p-2 rounded-lg hover:bg-gray-100 text-base font-normal">
            <h3 className="text-base font-semibold">Uploaded Docs</h3>
            <div className="mt-2 max-h-40 overflow-y-auto  p-2 text-sm font-normal">
              <p className="text-sm font-normal">{file?.name}</p>
            </div>
          </div>

          <div className="text-left p-2 rounded-lg hover:bg-gray-100 text-base font-normal mt-4">
            <h3 className="text-base font-semibold">Chat History</h3>
            <div className="mt-2 max-h-40 overflow-y-auto  text-sm font-semibold justify-center">
              <p className="text-base font-normal">Chat 1</p>
            

            </div>
          </div>
        </div>
    </aside>

      {/* Chat Area */}
      <main className="flex flex-col flex-1">
        {/* Messages */}
       <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {response.map((item, index) => (
          <div
            key={index}
            className="rounded border bg-gray-50 p-4"
          >
            {/* Question */}
            <p className="mb-2 font-semibold">
              Q: {item.question}
            </p>

            {/* Answer */}
            <div className="space-y-2">
              {item.answer.split("\n").map((line, i) => {
                // Heading
                if (line.startsWith("**") && line.endsWith("**")) {
                  return (
                    <h3 key={i} className="font-bold text-lg">
                      {line.replace(/\*\*/g, "")}
                    </h3>
                  );
                }

                // Bullet
                if (line.startsWith("-")) {
                  return (
                    <li key={i} className="ml-4 list-disc">
                      {line.slice(1).trim()}
                    </li>
                  );
                }

                // Normal paragraph
                return (
                  <p key={i} className="text-base text-gray-700">
                    {line}
                  </p>
                );
              })}
            </div>
          </div>
        ))}
      </div>


        {/* Input Area */}
        <div className="border-t bg-white p-8">
          <div className="flex gap-2 max-w-3xl mx-auto">
            <input
              className="flex-1 border rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-black"
              placeholder="Ask me anything..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            />

            <button
              onClick={sendMessage}
              disabled={loading}
              className="bg-black text-white px-4 rounded-xl flex items-center justify-center hover:bg-gray-800 disabled:opacity-50"
            >{loading ? "Sending..." : "Send"}
            </button>
          </div>
        </div>
      </main>
    </div>
  );
};

export default AnswerBox;
