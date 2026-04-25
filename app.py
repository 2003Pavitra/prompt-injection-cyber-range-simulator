import streamlit as st
from datetime import datetime
from guardrails import guardrail_filter

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Cyber Range Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- STATE ----------------
if "logs" not in st.session_state:
    st.session_state.logs = []

if "total" not in st.session_state:
    st.session_state.total = 0

if "blocked" not in st.session_state:
    st.session_state.blocked = 0

if "allowed" not in st.session_state:
    st.session_state.allowed = 0

# ---------------- TITLE ----------------
st.title("🛡️ AI Cyber Range: Prompt Injection Defense Lab")
st.markdown("Simulating Attack vs Guardrail AI Security System")

st.divider()

# ---------------- INPUT PANEL ----------------
col1, col2 = st.columns(2)

with col1:
    prompt = st.text_area("Enter Prompt (Attack Simulation)")

    attack_type = st.selectbox(
        "Attack Type",
        ["Prompt Injection", "Jailbreak", "Data Exfiltration"]
    )

    guardrails = st.toggle("Enable Guardrails", value=True)

    run = st.button("Run Simulation")

# ---------------- OUTPUT PANEL ----------------
with col2:
    st.subheader("🧠 Result Output")

    if run and prompt.strip():

        st.session_state.total += 1
        time = datetime.now().strftime("%H:%M:%S")

        if guardrails:
            result, blocked = guardrail_filter(prompt)
        else:
            result = f"⚠️ ATTACK EXECUTED: {attack_type}"
            blocked = False

        if blocked:
            st.session_state.blocked += 1
            status = "BLOCKED"
        else:
            st.session_state.allowed += 1
            status = "ALLOWED"

        risk_keywords = ["ignore", "jailbreak", "reveal", "system", "developer"]
        risk_score = sum(20 for k in risk_keywords if k in prompt.lower())

        st.success(result)
        st.write(f"**Status:** {status}")
        st.write(f"**Risk Score:** {risk_score}/100")

        # save log
        st.session_state.logs.append({
            "time": time,
            "type": attack_type,
            "prompt": prompt,
            "result": result,
            "status": status,
            "risk": risk_score
        })

    elif run:
        st.warning("Please enter a prompt")

# ---------------- DASHBOARD METRICS ----------------
st.divider()
st.subheader("📊 Cyber Range Statistics")

m1, m2, m3 = st.columns(3)

m1.metric("Total Attacks", st.session_state.total)
m2.metric("Blocked Attacks", st.session_state.blocked)
m3.metric("Allowed Attacks", st.session_state.allowed)

st.divider()

# ---------------- LOGS ----------------
st.subheader("📜 Attack Logs")

for log in reversed(st.session_state.logs):
    st.markdown(
        f"""
        **[{log['time']}] {log['type']}**  
        Prompt: `{log['prompt']}`  
        Result: {log['result']}  
        Status: **{log['status']}** | Risk: {log['risk']}  
        ---
        """
    )