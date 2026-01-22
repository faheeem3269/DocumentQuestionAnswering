from fastapi import FastAPI
from app.upload import router as upload_router  # <-- import router, not upload
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/savedoc")
def savedoc():
    return {"status": "ok"}

# Include your upload router under /api
app.include_router(upload_router, prefix="/api")
