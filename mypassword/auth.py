#user creation, login authentication, and password hashing
import bcrypt
import getpass
from database import load_users, save_users
from utils import validate_password

def create_user():
    users = load_users()
    username = input("Enter your desired username: ").strip().lower()

    if username in users: 
        print("Username already exists, please try again.")
        return
    
    while True:
        password = getpass.getpass("Enter your desired password: ").strip()
        confirm_password = getpass.getpass("Confirm your password: ").strip()

        #confirms if passwords are the same and if the password is long enough
        if password != confirm_password:
            print("The passwords you entered do not match, please try again")
        elif len(password) < 8:
            print("Your password must be at least 8 characters long.")
        else:
            break

    #converts the user's passwords to bytes and then generates a random salt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    #converts to byte string then to string for storage
    users[username] = hashed_password.decode("utf-8")

    save_users(users)
    print("Account created successfully!")

def login():
    users = load_users()
    username = input("Enter your username: ").strip().lower()

    #if username is not found return
    if username not in users:
        print("User not found.")
        return
    
    password = getpass.getpass("Enter your password: ").strip()
    hashed_password = users[username].encode("utf-8")
    if bcrypt.checkpw(password.encode(), hashed_password):
        print("Login successful!")
    else:
        print("Invalid login credentials.")
