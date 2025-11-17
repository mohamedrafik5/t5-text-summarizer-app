from fastapi import FastAPI
from TextSummarizer.api.endpoint import router as summarizer_router
import uvicorn

main_app = FastAPI(
    title="Text Summarizer Service",
    description="A FastAPI service that summarizes text using a Transformer model.",
    version="1.0.0"
)

# include router instead of mount
main_app.include_router(summarizer_router, prefix="/summarizer")

# Uvicorn entry point
if __name__ == "__main__":
    uvicorn.run( "TextSummarizer.main:main_app", host="127.0.0.1", port=8000, reload=True )


# python -m TextSummarizer.main