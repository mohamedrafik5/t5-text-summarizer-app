from TextSummarizer.core.model_invoking import TextSummarizer
from fastapi import APIRouter
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str
class SummaryResponse(BaseModel):
    summary: str

router = APIRouter()

summarizer = TextSummarizer()

@router.post("/text_summarizer/",response_model=SummaryResponse)
async def text_summarizer(request: TextRequest):
    """
    Generate a concise summary from the input text using a T5 transformer model.

    This endpoint processes long-form text input and returns a shorter,
    more readable summary while preserving the original meaning.
    It uses a pre-trained T5-based text summarization model loaded at startup.

    ---
    ### Request Body:
    - **texts** (str): The input text to summarize.

    ### Returns:
    - **summary** (str): A generated summary of the provided text.

    ### Response Model:
    `SummaryResponse`:
    ```json
    {
        "summary": "shortened version of the input text"
    }
    ```
    """
    text = request.text
    summary = summarizer.summarize_text(text)
    return {"summary": summary}
