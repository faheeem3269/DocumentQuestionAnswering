from fastapi import  APIRouter, UploadFile, File, HTTPException,FastAPI
from pathlib import Path
import shutil
from services.questionanswer import read_file_content, startEmbedding, StartQA
from fastapi.middleware.cors import CORSMiddleware
router = APIRouter()
from pydantic import BaseModel
app = FastAPI()
origins = [
    "http://localhost:3000",
    # You can add other allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class QuestionRequest(BaseModel):
    question: str

UPLOAD_DIR = Path("data/documents")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)  # Ensure folder exists

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Only allow certain file types
    print("Received file:", file.filename)
    allowed_extensions = ["pdf", "docx", "txt"]
    ext = file.filename.split(".")[-1].lower()
    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="File type not allowed only pdf, docx, txt are allowed")

    # Define file path
    file_path = UPLOAD_DIR / file.filename

    # Save file to disk
    with file_path.open("wb") as buffer:
       shutil.copyfileobj(file.file, buffer)
    text_content = read_file_content(file.filename)
    startEmbedding(text_content)
    return {"filename": file.filename, "message": "Upload successful"}

@router.post("/askquestion")
async def ask_question(question: QuestionRequest): 
    print("Received question:", question.question)
    try:
         answer = StartQA(question.question)
        ## answer = "Maecenas sed eget nunc et faucibus donec pulvinar velit ut. Amet vulputate sem vulputate ut blandit diam eleifend sed amet turpis quam nibh. Ac eros dolor amet etiam maecenas vel adipiscing sapien. Leo quam nibh quam vel ipsum eros vulputate. Vitae maecenas sem odio ligula pulvinar ut risus. Sapien ut nec ipsum leo libero nam tincidunt eleifend condimentum ut. Vitae neque donec sit amet amet ipsum et donec augue sapien. Quis nam sodales tincidunt in praesent adipiscing rutrum. Scelerisque ut sagittis pellentesque faucibus luctus purus ut bibendum risus sit aliquet feugiat. Leo sem elit sed sem nibh consectetur a maecenas sit sit condimentum sit etiam. Maecenas semper sodales ligula amet amet bibendum adipiscing elit faucibus eleifend nunc lorem. Donec nam nibh sed eleifend rhoncus purus nunc leo donec ante libero semper tincidunt. Dolor dolor tincidunt ipsum sit purus maecenas ligula ipsum. Tempus ante hendrerit consequat sapien praesent vitae tincidunt tellus maecenas sagittis sit. Sit hendrerit mauris pellentesque fusce odio consectetur praesent nunc magna. Sed eros et vitae sed a ipsum eleifend odio nam. Quam nunc nibh laoreet eleifend eros bibendum vitae nam eros sagittis. Eget mi vel tempus maecenas eros feugiat donec risus augue tincidunt consequat vitae. Bibendum scelerisque urna eget odio sed mauris integer etiam leo faucibus justo.Id eget etiam adipiscing sit sed pellentesque faucibus amet. Tincidunt eget in donec tempus in tempus duis gravida ante pellentesque quam libero hendrerit magna. Adipiscing vestibulum nunc tincidunt amet quam blandit donec id tempus purus amet sed amet. Ut nibh eleifend vel nam nibh laoreet justo quis. Tincidunt laoreet gravida sed tempus sed quam sit ac quam urna. Id vestibulum ante augue id ante magna leo etiam luctus tincidunt eget. Urna lorem dolor sit rhoncus orci dolor tortor sem justo sit praesent blandit. Nec vitae dolor in sodales condimentum sodales purus consectetur. Diam augue mauris blandit urna sapien sapien consequat. Vulputate auctor sed scelerisque amet turpis diam duis eros ac. Auctor faucibus nullam rutrum libero eros sodales nunc. Consequat eleifend sapien integer a amet quam sagittis. Ut tempus consectetur etiam urna tincidunt risus augue quam quam vestibulum tincidunt. Quam nullam sodales ut sem dolor sapien odio nam quam orci sem. Blandit feugiat leo in libero lorem sapien eleifend nunc aliquet id adipiscing sagittis rhoncus dictum. Eleifend turpis ante risus leo sem donec consequat ante. Fusce gravida vitae fringilla mauris dictum donec libero blandit ipsum. Maecenas nunc dictum praesent mauris augue gravida vitae quam bibendum aliquet sapien. Scelerisque nullam magna maecenas dolor ac sem justo sapien libero donec."

         return {"question": answer}
   
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
   
  