import streamlit as st
import requests

API_URL = "http://localhost:8000/summarizer/text_summarizer/"

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📝 Text Summarizer App")
st.write("Enter text below and get an AI-generated summary.")

# Initialize session state
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "clear_count" not in st.session_state:
    st.session_state.clear_count = 0


# Callback to clear text & summary
def clear_text():
    st.session_state.input_text = ""
    st.session_state.summary = ""
    st.session_state.clear_count += 1  # force text_area re-render


# Textarea (key changes after clearing!)
st.session_state.input_text = st.text_area(
    "Enter text to summarize:",
    value=st.session_state.input_text,
    height=250,
    key=f"input_text_area_{st.session_state.clear_count}"
)

# Buttons aligned
col1, col2 = st.columns([1, 1])

with col1:
    summarize_btn = st.button("Summarize", use_container_width=True)

with col2:
    clear_btn = st.button(
        "Clear",
        on_click=clear_text,
        disabled=(st.session_state.input_text.strip() == ""),
        use_container_width=True
    )

# Summarize logic
if summarize_btn:
    if not st.session_state.input_text.strip():
        st.warning("⚠ Please enter some text first.")
    else:
        with st.spinner("Summarizing..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"text": st.session_state.input_text}
                )

                if response.status_code == 200:
                    st.session_state.summary = response.json().get("summary", "")
                else:
                    st.session_state.summary = ""
                    st.error(f"Error: {response.status_code}")
                    st.json(response.json())

            except Exception as e:
                st.error("❌ Could not connect to API.")
                st.exception(e)

# Display summary
if st.session_state.summary:
    st.success("✔ Summary:")
    st.write(st.session_state.summary)
