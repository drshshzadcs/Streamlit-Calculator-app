import streamlit as st

# ============================
# 🧠 Streamlit Calculator App
# ============================

st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Smart Calculator")
st.markdown("Perform quick calculations easily with this interactive Streamlit app.")

# --- Input fields ---
col1, col2, col3 = st.columns(3)

with col1:
    num1 = st.number_input("Enter first number", value=0.0, step=1.0)
with col3:
    num2 = st.number_input("Enter second number", value=0.0, step=1.0)

with col2:
    operation = st.selectbox("Select Operation", ("Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"))

# --- Calculate result ---
def calculate(a, b, op):
    if op == "Add (+)":
        return a + b
    elif op == "Subtract (-)":
        return a - b
    elif op == "Multiply (×)":
        return a * b
    elif op == "Divide (÷)":
        if b != 0:
            return a / b
        else:
            return "Error: Division by Zero"

# --- Perform calculation ---
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"**Result:** {result}")

# --- Optional history feature ---
if "history" not in st.session_state:
    st.session_state["history"] = []

if st.button("Save to History"):
    st.session_state["history"].append(f"{num1} {operation} {num2} = {calculate(num1, num2, operation)}")

if st.session_state["history"]:
    st.markdown("### 🧾 Calculation History")
    for entry in st.session_state["history"]:
        st.write("•", entry)

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
