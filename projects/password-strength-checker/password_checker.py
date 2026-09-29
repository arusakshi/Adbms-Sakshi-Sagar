import re
import sys

def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 12: score += 1
    else: suggestions.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password): score += 1
    else: suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password): score += 1
    else: suggestions.append("Add a lowercase letter.")

    if re.search(r"\d", password): score += 1
    else: suggestions.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password): score += 1
    else: suggestions.append("Add a special character.")

    labels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
    return labels[score], suggestions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python password_checker.py '<password>'")
        sys.exit(1)

    strength, suggestions = check_password(sys.argv[1])
    print(f"Strength: {strength}")
    for item in suggestions:
        print(f"- {item}")
