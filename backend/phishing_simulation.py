print("🛡️ CyberNexus Phishing Awareness Simulation")
print("--------------------------------------------")

print("\nYou received this sample message:")
print()
print("Subject: Urgent Account Notice")
print("Message: Your account needs verification. Please review the message carefully.")
print()

print("What warning signs would you check?")
print("1. Unexpected request")
print("2. Urgency or pressure")
print("3. Unknown sender")
print("4. Suspicious links")
print("5. Request for password or personal information")

print()

score = 0

answer = input("Would you treat this message carefully? (yes/no): ").strip().lower()

if answer == "yes":
    score += 1
    print("✅ Good choice!")

else:
    print("⚠️ Remember to check unexpected messages carefully.")

print()
print("Safety Tips:")
print("- Check the sender address.")
print("- Don't click unexpected links.")
print("- Don't share passwords or OTPs.")
print("- Verify important requests through an official channel.")

print()
print("Simulation Score:", score, "/ 1")
print("🛡️ Awareness simulation completed.")