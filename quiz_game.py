print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    exit()

print("Okey! Let's play! :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Central Processing Unit.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Graphics Processing Unit.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Random Access Memory.")

answer = input("What doeas PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Power Supply Unit.")

print(f"You got {score} questions right!")
print(f"You got {score / 4 * 100}% of the questions right!")
