import tkinter as tk
from datetime import datetime
from main import simulate

attack_count = 0
blocked_count = 0
success_count = 0


def run_simulation():
    global attack_count, blocked_count, success_count

    prompt = entry.get().strip()
    attack = attack_type.get()
    guard_enabled = guard_var.get()

    if not prompt:
        output_label.config(text="⚠️ Please enter a prompt")
        return

    result, status = simulate(prompt, guard_enabled, attack)

    # Update counters
    attack_count += 1
    if status == "BLOCKED":
        blocked_count += 1
    else:
        success_count += 1

    # Update UI
    output_label.config(text=f"{result} | Status: {status}")

    score_label.config(
        text=f"Total: {attack_count} | Blocked: {blocked_count} | Allowed: {success_count}"
    )

    # Logs
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_box.insert(
        tk.END,
        f"[{timestamp}] {attack}\n{prompt}\n{result} ({status})\n\n"
    )
    log_box.see(tk.END)


# ---------------- UI ----------------
root = tk.Tk()
root.title("AI Cyber Range Simulator")
root.geometry("700x600")
root.configure(bg="black")

tk.Label(
    root,
    text="AI Cyber Range Simulator",
    fg="lime",
    bg="black",
    font=("Courier", 16)
).pack(pady=10)

tk.Label(root, text="Enter Prompt:", fg="white", bg="black").pack()

entry = tk.Entry(root, width=80, bg="black", fg="lime", insertbackground="lime")
entry.pack(pady=10)

attack_type = tk.StringVar(value="Prompt Injection")

tk.Label(root, text="Attack Type:", fg="white", bg="black").pack()

tk.OptionMenu(
    root,
    attack_type,
    "Prompt Injection",
    "Data Exfiltration",
    "Jailbreak Attempt"
).pack()

guard_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Enable Guardrails",
    variable=guard_var,
    fg="white",
    bg="black",
    selectcolor="black"
).pack(pady=5)

tk.Button(
    root,
    text="Run Simulation",
    command=run_simulation,
    bg="gray",
    fg="black"
).pack(pady=10)

output_label = tk.Label(
    root,
    text="",
    fg="red",
    bg="black",
    font=("Courier", 11),
    wraplength=650
)
output_label.pack(pady=10)

score_label = tk.Label(
    root,
    text="Total: 0 | Blocked: 0 | Allowed: 0",
    fg="cyan",
    bg="black"
)
score_label.pack(pady=5)

tk.Label(root, text="Logs:", fg="white", bg="black").pack()

log_box = tk.Text(
    root,
    height=15,
    width=85,
    bg="black",
    fg="lime"
)
log_box.pack(pady=10)

root.mainloop()