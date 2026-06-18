import streamlit as st
import ollama
from PIL import Image

st.set_page_config(
    page_title="AI Electronic Circuit Tutor",
    page_icon="🔌",
    layout="wide"
)

st.title("🔌 AI Electronic Circuit Tutor")

st.write(
    "Select a circuit and topic to learn Electronics concepts using AI."
)

uploaded_file = st.file_uploader(
    "Upload Circuit Image (Optional)",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Circuit", use_container_width=True)

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
        "Transformer Coupled Amplifier",
        "Direct Coupled Amplifier",
        "Op-Amp Inverting Amplifier",
        "Op-Amp Non-Inverting Amplifier",
        "Op-Amp Voltage Follower",
        "Op-Amp Integrator",
        "Op-Amp Differentiator",
        "Op-Amp Summing Amplifier",
        "Op-Amp Comparator",
        "555 Timer Astable",
        "555 Timer Monostable",
        "555 Timer Bistable",
        "RC Phase Shift Oscillator",
        "Wien Bridge Oscillator",
        "Hartley Oscillator",
        "Colpitts Oscillator",
        "Crystal Oscillator",
        "Emitter Follower",
        "Current Mirror",
        "Voltage Divider Circuit",
        "AND Gate",
        "OR Gate",
        "NOT Gate",
        "NAND Gate",
        "NOR Gate",
        "XOR Gate",
        "XNOR Gate",
        "Half Adder",
        "Full Adder",
        "Half Subtractor",
        "Full Subtractor",
        "SR Flip Flop",
        "JK Flip Flop",
        "D Flip Flop",
        "T Flip Flop",
        "Encoder",
        "Decoder",
        "Multiplexer",
        "Demultiplexer",
        "Binary Counter",
        "Ring Counter",
        "Shift Register",
        "Buck Converter",
        "Boost Converter",
        "Buck Boost Converter",
        "SMPS",
        "UPS Circuit",
        "Arduino LED Control",
        "Arduino Temperature Monitoring",
        "Arduino Ultrasonic Distance Sensor",
        "IoT Smart Home Circuit",
        "IoT Health Monitoring System",
        "MOSFET Switch Circuit",
        "BJT Switch Circuit",
        "LDR Based Automatic Street Light",
        "IR Sensor Circuit",
        "Ultrasonic Sensor Circuit",
        "Traffic Light Controller",
        "Water Level Indicator",
        "Fire Alarm Circuit",
        "Burglar Alarm Circuit"
    ]
)

topic = st.selectbox(
    "Select Topic",
    [
        "Working Principle",
        "Components Used",
        "Applications",
        "Advantages",
        "Disadvantages",
        "Formulae",
        "Viva Questions",
        "Troubleshooting",
        "Interview Questions",
        "Mini Project Ideas"
    ]
)

question = st.text_input(
    "Additional Question (Optional)",
    ""
)

if st.button("Generate AI Explanation"):

    prompt = f"""
You are an expert Electronics and Communication Engineering professor.

Circuit:
{circuit_type}

Topic:
{topic}

Additional Question:
{question}

Provide a detailed, accurate, student-friendly explanation.
Use headings and bullet points wherever appropriate.
"""

    with st.spinner("Generating response..."):

        response = ollama.chat(
            model="gemma2:2b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.subheader("AI Response")
        st.write(response["message"]["content"])