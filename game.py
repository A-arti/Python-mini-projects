import random
def get_choices():
  player_choice = input("Enter a Choice (rock, paper,scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player":player_choice,"computer":computer_choice}
  return choices
while True:
  def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player==computer:
      return "It is a tie"
    elif player== "rock":
      if computer == "scissors":
        return "Rock smashes scissors! You Win!"
      else:
        return "Paper cover rock! You lose."
    elif player== "paper":
      if computer == "rock":
        return "Paper cover rock!You Win!"
      else:
        return "Scissors cuts paper! You lose."
    elif player== "scissors":
      if computer == "paper":
        return "scissors cuts psper!You Win!"
      else:
        return "Rock smashes scissors! You lose." 
  
    
  choices = get_choices()
  result = check_win(choices["player"], choices["computer"])
  print(result)
  
  
  
  

  
