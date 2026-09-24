from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Simple educational training data
emails = [
    "Hello, your meeting is scheduled for tomorrow",
    "Please find the assignment attached",
    "Your class timetable has been updated",
    "Reminder: submit your project before Friday",
    "Congratulations, you won a free prize click here",
    "Urgent! Your account will be closed verify now",
    "You have won a lottery claim your reward",
    "Click this link immediately to receive your money"
]

labels = [
    "Safe",
    "Safe",
    "Safe",
    "Safe",
    "Phishing",
    "Phishing",
    "Phishing",
    "Phishing"
]

# Convert email text into numerical features
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(emails)

# Train classifier
model = MultinomialNB()

model.fit(X, labels)

print("🛡️ CyberNexus Phishing Email Classifier")
print("----------------------------------------")

email = input("Enter email text: ")

email_vector = vectorizer.transform([email])

prediction = model.predict(email_vector)[0]

print("\nPrediction:", prediction)

if prediction == "Phishing":
    print("⚠️ This email looks suspicious.")
else:
    print("✅ This email looks safe.")