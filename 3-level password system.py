import random
import getpass
def generate_otp():
    return random.randint(100000, 999999)
def check_basic_password(stored_password):
    user_password = getpass.getpass("Enter your password: ")
    return user_password == stored_password
def check_security_question(stored_answer):
    user_answer = input("What is your favorite color? ").strip().lower()
    return user_answer == stored_answer.lower()
def check_otp(stored_otp):
    user_otp = input("Enter the OTP sent to your phone: ")
    return user_otp == str(stored_otp)
def authenticate():
    basic_password = "MySecretPassword"
    security_answer = "blue"
    otp = generate_otp()
    print(f"An OTP has been generated (For testing purposes, it's {otp})")
    print("Welcome to the three-level authentication system")
    if not check_basic_password(basic_password):
        print("Basic password is incorrect.")
        return False
    if not check_security_question(security_answer):
        print("Security answer is incorrect.")
        return False
    if not check_otp(otp):
        print("OTP is incorrect.")
        print("Authentication failed!")
        return False
    print("Authentication successful!")
    return True
if __name__ == "__main__":
    authenticate()