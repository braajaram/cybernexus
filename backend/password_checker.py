import re
import hashlib
import requests


def check_password_strength(password):

    checks = {
        "length": len(password) > 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "number": bool(re.search(r"[0-9]", password)),
        "symbol": bool(re.search(r"[^A-Za-z0-9]", password))
    }

    score = sum(checks.values())

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return checks, strength


def check_password_breach(password):

    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    response = requests.get(url)

    if response.status_code != 200:
        return "Breach check unavailable"

    for line in response.text.splitlines():

        hash_suffix, count = line.split(":")

        if hash_suffix == suffix:
            return f"Found in {count} breaches"

    return "Not found in known breaches"


password = input("Enter password: ")

checks, strength = check_password_strength(password)

print("\nPassword Checks:")

for check, result in checks.items():
    print(f"{check}: {'✓' if result else '✗'}")

print("Strength:", strength)

print("Breach Check:", check_password_breach(password))