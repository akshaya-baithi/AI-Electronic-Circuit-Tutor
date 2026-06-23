import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-pro")

# Streamlit Page Settings
st.set_page_config(
    page_title="AI Electronic Circuit Tutor",
    page_icon="🔌",
    layout="wide"
)

st.title("🔌 AI Electronic Circuit Tutor")
st.write("Learn Electronics and Communication Engineering circuits using AI.")


# ---------------- FUNCTION ----------------
def get_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- IMAGE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload Circuit Image (Optional)",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Circuit", use_container_width=True)


# ---------------- CIRCUIT SELECT ----------------
circuit_type = st.selectbox(
    "Select Circuit Type",
    [
        "Common Emitter Amplifier",
        "Common Base Amplifier",
        "Common Collector Amplifier",
        "Differential Amplifier",
        "Darlington Pair Amplifier",
        "Class A Amplifier",
        "Class B Amplifier",
        "Class AB Amplifier",
        "Class C Amplifier",
        "Half Wave Rectifier",
        "Full Wave Rectifier",
        "Bridge Rectifier",
        "Voltage Doubler",
        "Voltage Tripler",
        "Clipper Circuit",
        "Clamper Circuit",
        "Zener Voltage Regulator",
        "RC Coupled Amplifier",
        "Op-Amp Inverting Amplifier",
        "Op-Amp Non-Inverting Amplifier",
        "555 Timer Astable",
        "555 Timer Monostable",
        "Binary Counter",
        "IoT Smart Home Circuit",
        "Fire Alarm Circuit",
        "Burglar Alarm Circuit"
    ]
)


# ---------------- TOPIC ----------------
topic = st.selectbox(
    "Select Topic",
    [
        "Working Principle",
        "Components Used",
        "Applications",
        "Advantages",
        "Disadvantages",
        "Viva Questions",
        "Troubleshooting"
    ]
)

# ---------------- QUESTION ----------------
question = st.text_input("Additional Question (Optional)")


# ---------------- BUTTON ----------------
if st.button("Generate AI Response"):

    prompt = f"""
You are an expert Electronics and Communication Engineering professor.

Circuit:
{circuit_type}

Topic:
{topic}

Additional Question:
{question}

Provide a detailed, accurate, student-friendly explanation.

Use:
- Headings
- Bullet Points
- Examples where necessary
- Simple language
"""

    with st.spinner("Generating AI Response..."):
        result = get_response(prompt)

    st.subheader("📘 AI Response")
    st.write(result)