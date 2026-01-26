from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from Text_Summarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
async def predict_route(data: TextInput):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(data.text)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)