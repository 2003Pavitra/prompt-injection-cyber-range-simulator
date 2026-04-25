def guardrail_filter(prompt):
    text = prompt.lower()

    blocked_patterns = [
        "ignore previous instructions",
        "jailbreak",
        "developer mode",
        "reveal system prompt",
        "you are now",
        "act as"
    ]

    for pattern in blocked_patterns:
        if pattern in text:
            return f"🚫 BLOCKED: detected pattern → '{pattern}'", True

    return "✅ SAFE: prompt accepted", False


def simulate_without_guardrails(prompt):
    return f"⚠️ UNSAFE EXECUTION: {prompt}"