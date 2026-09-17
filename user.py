users = {}


def register_user():
    print("\n========== REGISTER ==========")

    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return False

    if username in users:
        print("Username already exists.")
        return False

    password = input("Enter password: ").strip()

    if not password:
        print("Password cannot be empty.")
        return False

    users[username] = password

    print("Registration successful!")
    return True


def login_user():
    print("\n========== LOGIN ==========")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in users and users[username] == password:
        print("Login successful!")
        print("Welcome,", username)
        return username

    print("Invalid username or password.")
    return None


def guest_user():
    print("\nContinuing as Guest.")
    return "Guest"