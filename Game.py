import random2;

random_choose = ["paper", "rock", "scissors"]

while True :
  user_choose = str(input("Please enter your shape (paper, rock, scissors): "))
  if user_choose in random_choose:
    break
  else:
    print("Your choose is not exist")

pc_choose = str(random2.choice(random_choose))
input(pc_choose)
print( "Pc choose Is: ", pc_choose)
print( "Your choose Is: ", user_choose)

if user_choose == pc_choose:
  print("Equality")

# that I do  before i watched the video
elif user_choose == "paper" and pc_choose == "rock":
  print("You are won!")

elif user_choose == "rock" and pc_choose == "scissors":
  print("You are won!")

elif user_choose == "scissors" and pc_choose == "paper":
  print("You are won!")

else:
  print ("You are a loser!")