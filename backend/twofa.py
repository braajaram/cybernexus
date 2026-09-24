import pyotp

secret = pyotp.random_base32()

totp = pyotp.TOTP(secret)

print("Secret Key:", secret)

otp = totp.now()

print("Generated OTP:", otp)

user_otp = input("Enter OTP: ").strip()

if totp.verify(user_otp, valid_window=1):
    print("✅ 2FA Verification Successful!")
else:
    print("❌ Invalid OTP!")