import re

def validate_email(email):
    if not email:
        return "Invalid: Email cannot be empty"

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return "Valid Email" if re.fullmatch(pattern, email) else "Invalid Email Format"


def validate_mobile(mobile):
    if not mobile:
        return "Invalid: Mobile number cannot be empty"

    pattern = r'^(?:\+91|91)?[6-9]\d{9}$'
    return "Valid Indian Mobile Number" if re.fullmatch(pattern, mobile) else "Invalid Mobile Number"


def validate_password(password):
    if not password:
        return "Invalid: Password cannot be empty"

    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return "Strong Password" if re.fullmatch(pattern, password) else "Weak Password"


def main():
    email = input("Enter Email: ")
    print(validate_email(email))

    mobile = input("Enter Mobile Number: ")
    print(validate_mobile(mobile))

    password = input("Enter Password: ")
    print(validate_password(password))


if __name__ == "__main__":
    main()
