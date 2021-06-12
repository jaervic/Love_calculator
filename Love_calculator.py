print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n = name1.lower() + name2.lower()

true_name = n.count("t") + n.count("r") + n.count("u") + n.count("e")
love_name = n.count("l") + n.count("o") + n.count("v") + n.count("e")

score = int(str(true_name) + str(love_name))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

