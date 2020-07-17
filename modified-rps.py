import random
user_name = input("Enter you name: ")
print("Hello,", user_name)
scores = open("rating.txt", "r")
names_and_ratings = scores.read().split()
scores.close()

scores = open("rating.txt", "a")
if user_name not in names_and_ratings:
    print(f"\n{user_name} 0", file=scores, flush= True)
scores.close()

scores = open("rating.txt", "r")
lines = scores.readlines()
for line in lines:
    if user_name in line:
        user_score = int(line.split()[1])

scores.close()
version = input().split(",")
if version == ['']:
    version = ["rock", "paper", "scissors"]
print("Okay, let's start")

while True:
    user_turn = input()
    if user_turn in version:
        index_of_user_turn = version.index(user_turn)
        new_version = version[index_of_user_turn + 1:] + version[:index_of_user_turn]
        winners = new_version[:int(len(new_version) / 2)]
        loosers = new_version[int(len(new_version) / 2):]
        computer_turn = random.choice(version)
        if user_turn == computer_turn:
            print(f"There is a draw ({user_turn})")
            user_score += 50
        elif computer_turn in winners:
            print(f"Sorry, but computer chose {computer_turn}")
        else:
            print(f"Well done. Computer chose {computer_turn} and failed")
            user_score += 100
    elif user_turn == "!exit":
        print("Bye!")
        break
    elif user_turn == "!rating":
        print("Your rating", user_score)
    else:
        print("Invalid input")
