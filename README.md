
# 📝 T5 Text Summarizer App

A full-stack AI text summarization tool built with:

- T5 Transformer (Hugging Face)
- FastAPI backend
- Streamlit frontend
- YAML-based configuration

This app takes long text and returns a concise summary while preserving meaning.

---

## 📌 Tech Stack

| Layer | Technology |
|-------|-------------|
| Model | T5 (Hugging Face Transformers) |
| Backend | FastAPI |
| Frontend | Streamlit |
| Language | Python |
| Config | YAML |

---

## 📂 Project Structure

```

TextSummarizer/
│
├── api/
│   └── endpoint.py           # FastAPI endpoint
│
├── config/
│   └── config.yaml           # Model & app config
│
├── core/
│   └── model_invoking.py     # T5 model logic
│
├── utils/
│   └── load_config.py        # Loads YAML config
│
├── main.py                   # FastAPI entry point
├── streamlit.py              # Streamlit UI
├── requirements.txt          # Dependencies for this project
└── README.md

````

---

## 🧠 Model Used

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer
````

---

## 🚀 Setup Instructions

### Clone the repository:

```bash
git clone https://github.com/mohamedrafik5/t5-text-summarizer-app.git
cd t5-text-summarizer-app
```

### Create & activate a virtual environment (with uv):

```bash
uv venv
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows
```

### Install dependencies:

```bash
uv pip install -r requirements.txt
```

---

## ▶ Run the FastAPI backend

```bash
python -m TextSummarizer.main
```

API runs at:

```
http://localhost:8000
```

---

## ▶ Run the Streamlit frontend

```bash
streamlit run TextSummarizer/streamlit.py
```

Streamlit runs at:

```
http://localhost:8501
```

---

## 🧪 API Example

**POST**
`/summarizer/text_summarizer/`

Request:

```json
{
  "text": "Your long text here."
}
```

Response:

```json
{
  "summary": "Shortened version of the input text."
}
```

---

## ⚙️ Configuration

Edit:

```
config/config.yaml
```

Example:

```yaml
model_name: "t5-small"
max_input_length: 512
max_output_length: 150
```

---

## 📌 Roadmap

* PDF / text file upload
* Multiple model options
* GPU acceleration
* Long document support

---

## 🤝 Contributing

Pull requests are welcome!

---

## 📄 License

MIT License

```
free to use, modify, & distribute.
```
