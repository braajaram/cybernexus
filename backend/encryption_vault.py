from cryptography.fernet import Fernet
import os

KEY_FILE = "vault.key"


def create_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    return key


def load_key():
    if not os.path.exists(KEY_FILE):
        return create_key()

    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_file(filename):
    key = load_key()
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

    print("✅ File encrypted successfully!")


def decrypt_file(filename):
    key = load_key()
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    output_file = filename.replace(".encrypted", ".decrypted")

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print("✅ File decrypted successfully!")


print("🔐 CyberNexus Encryption Vault")
print("1. Encrypt file")
print("2. Decrypt file")

choice = input("Enter choice: ").strip()

if choice == "1":
    filename = input("Enter file name: ").strip()

    if os.path.exists(filename):
        encrypt_file(filename)
    else:
        print("❌ File not found.")

elif choice == "2":
    filename = input("Enter encrypted file name: ").strip()

    if os.path.exists(filename):
        decrypt_file(filename)
    else:
        print("❌ File not found.")

else:
    print("❌ Invalid choice.")