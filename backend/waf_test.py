import re


def detect_threat(user_input):

    patterns = [
        r"('|--|;)",
        r"\bOR\b\s+\d+\s*=\s*\d+",
        r"<script.*?>",
        r"javascript:",
        r"onerror\s*="
    ]

    for pattern in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True

    return False


user_input = input("Enter input: ")

if detect_threat(user_input):
    print("🚨 Threat detected! Request blocked.")
else:
    print("✅ Input is safe.")