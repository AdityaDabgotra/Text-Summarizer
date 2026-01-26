from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Text_Summarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/predict")
async def predict_route(data: TextInput):
    obj = PredictionPipeline()
    summary = obj.predict(data.text)
    return {"summary": summary}