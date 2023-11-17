import random2;
user_choose = str(input("Please enter your shape (paper, rock, scissors)"))
random_choose = ["paper", "rock", "scissors"]
pc_choose = str(random2.choice(random_choose))

input(pc_choose)

if user_choose == pc_choose:
  print("Equality")

elif user_choose == "paper" and pc_choose == "rock":
  print("You are won!")

elif user_choose == "rock" and pc_choose == "scissors":
  print("You are won!")

elif user_choose == "scissors" and pc_choose == "paper":
  print("You are won!")

else:
  print ("You are loser!")