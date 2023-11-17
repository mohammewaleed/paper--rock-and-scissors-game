import random2;
user_choose = input("Please enter your shape (paper, rock, scissors)")
random_choose = ["paper", "rock", "scissors"]
pc_choose = random2.randint(random_choose)

if user_choose == pc_choose:
  print("Equality")
elif user_choose == "paper" & pc_choose == "rock":
  print("You are won!")

elif user_choose == "rock" & pc_choose == "scissors":
  print("You are won!")

elif user_choose == "scissors" & pc_choose == "paper":
  print("You are won!")

else:
  print ("You are loser!")