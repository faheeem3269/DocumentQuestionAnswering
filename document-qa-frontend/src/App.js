import logo from './logo.svg';
import './App.css';
import UploadForm from './Components/UploadForm';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AnswerBox from './Components/AnswerBox';

function App() {
  return (
   
     <BrowserRouter>
      <Routes>
        <Route path="/" element={<UploadForm />} />
        <Route path="/answerbox" element={<AnswerBox />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
