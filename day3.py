# Store engineer profile as dictionary
engineer = {
    "name": input("what is your name? "),
    "city": input("what city are you from? "),
    "goal": input("what is your AI goal? "),
    "hours": int(input("How many hours a day will you study? "))
}

# Save Profile to a file
with open("profile.txt", "w") as f:
    f.write(f"name: {engineer['name']}\n")
    f.write(f"city: {engineer['city']}\n")
    f.write(f"goal: {engineer['goal']}\n")
    f.write(f"Daily Hours: {engineer['hours']}\n")

    print("profile saved!")

#Read it back
with open("profile.txt", "r") as f:
    print(f.read())
