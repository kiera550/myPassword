#handles user input and routes functions
from auth import create_user, login

#for user interaction
def main():
    while True:
        print("\n Welcome to myPassword Manager")
        print("1 Create an account")
        print("2 Login")
        print("3 Exit")

        choice = input("Enter the number corresponding to desired action: ")
        if choice == "1":
            create_user()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()