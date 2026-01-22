# 📄 DocumentQA – Full-Stack Document Question Answering System

A full-stack **Document Question Answering (DocumentQA)** application that allows users to upload documents and ask natural language questions. The system retrieves relevant context using embeddings and generates accurate answers using large language models.

The backend is built with **Python**, leveraging the **Groq API** for fast LLM inference and **Hugging Face embeddings** for semantic search, while the frontend is developed using **React** for a modern, interactive user experience.

---

## 🚀 Features

* Upload and process documents for question answering
* Semantic search using Hugging Face embeddings
* Fast and accurate responses powered by Groq LLM API
* RESTful backend API built with Python
* Interactive and responsive React frontend
* Modular and scalable architecture

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Groq API (LLM inference)
* Hugging Face Embeddings
* Vector storage (FAISS / Chroma / other – optional)

### Frontend

* React
* JavaScript / TypeScript
* HTML5 & CSS3
* Axios / Fetch API

---

## 📂 Project Structure

```
DocumentQA/
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   ├── main.py
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## ⚙️ Installation & Setup

### Prerequisites

* Python 3.11+
* Node.js 18+
* npm
* Groq API Key
* Hugging Face API Key (if required)

---

### 🔹 Backend Setup

1. Navigate to the backend directory:

```bash
cd backend
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

5. Start the backend server:

```bash
python main.py
```

The backend will run at:

```
http://localhost:8000
```

---

### 🔹 Frontend Setup

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm start
```

The frontend will run at:

```
http://localhost:3000
```

---

## 🔄 How It Works

1. User uploads a document via the React frontend
2. Backend processes and chunks the document
3. Hugging Face embeddings are generated and stored
4. User submits a question
5. Relevant document chunks are retrieved using semantic similarity
6. Context is sent to the Groq LLM API
7. Generated answer is returned to the frontend

---

## 📌 API Endpoints (Example)

| Method | Endpoint | Description     |
| ------ | -------- | --------------- |
| POST   | /upload  | Upload document |
| POST   | /query   | Ask a question  |
| GET    | /health  | Health check    |

---

## 🔐 Environment Variables

| Variable            | Description                 |
| ------------------- | --------------------------- |
| GROQ_API_KEY        | Groq API authentication key |
| HUGGINGFACE_API_KEY | Hugging Face API key        |

---

## 🧪 Future Improvements

* User authentication
* Support for multiple document formats (PDF, DOCX)
* Streaming responses
* Chat history and session management
* Dockerization for easy deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* Groq for high-performance LLM inference
* Hugging Face for embedding models
* Open-source community for inspiration and tools

---

⭐ If you find this project useful, consider giving it a star!
