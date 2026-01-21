import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print(f"Correct! Attempts: {attempts}")
        break
users = {"admin": "1234"}

username = input("Username: ")
password = input("Password: ")

if users.get(username) == password:
    print("Login Successful")
else:
    print("Invalid Credentials")
