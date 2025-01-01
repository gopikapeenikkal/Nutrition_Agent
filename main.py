from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import StreamingResponse
from nutrition_guide import nutrition_agent
from dotenv import load_dotenv
from typing import AsyncGenerator
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageRequest(BaseModel):
    image: str

@app.post("/captured_image")
async def image_analysis(request: ImageRequest):
    async def generate_response() -> AsyncGenerator[str, None]:
        try:
            async for chunk in nutrition_agent(request.image):
                if chunk:
                    yield f"data: {chunk}\n\n"
        except Exception as e:
            yield f"data: Error: {str(e)}\n\n"
        finally:
            yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate_response(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
        }
    )

