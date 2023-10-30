import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")

    # Get user input for the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a valid positive length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Generate and display the password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
