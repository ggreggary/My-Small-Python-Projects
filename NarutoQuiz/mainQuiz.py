print("Hi, and welcome to the ultimate Naruto fan quiz!")

play = input("Ready to begin? ")

if play != "yes":
    opp = input("why not?? ")
    quit()


print("Alrighty, let's start!\n\n")
score = 0

response = input("What clan is Sasuke apart of ? ")
if response.lower() == "uchiha":
    print('You got it!')
    score += 1
else:
    print("That's wrong :(")

response = input("Who is the sensei of team 7 ? ")
if response.lower() == "kakashi":
    print('You got it!')
    score += 1
else:
    print("That's wrong :(")

response = input("Who slaughtered the entire Uchiha clan ? ")
if response.lower() == "itachi":
    print('You got it!')
    score += 1
else:
    print("That's wrong :(")

response = input("Who did Rock Lee lose to during the second round of the Chunin exams ? ")
if response.lower() == "gaara":
    print('You got it!')
    score += 1
else:
    print("That's wrong :(")

response = input("What village is Orochimaru originally from ? ")
if response.lower() == "leaf village":
    print('You got it!')
    score += 1
else:
    print("That's wrong :(")

response = input("Who is the fourth hokage's son ? ")
if response.lower() == "naruto":
    print('You got it!')
    score += 1
else:
    print("That's wrong :(")

print("Your final score is " + str(score) + " !")
