import re

def validate_password_regex(password):
    
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+\[\]{}|;:\'",.<>?/]).{8,}$'
    return re.match(pattern, password) is not None


if __name__ == "__main__":
    while True:
        password = input("Enter a password to validate (or type 'exit' to quit): ")
        if password.lower() == "exit":
            print("Exiting password validator.")
            break

        if validate_password_regex(password):
            print("✅ Password is strong and valid!")
        else:
            print("❌ Password is invalid. It must have:")
            print("- At least 8 characters")
            print("- At least one uppercase letter")
            print("- At least one lowercase letter")
            print("- At least one digit")
            print("- At least one special character (!@#$%^&* etc.)")
        print()