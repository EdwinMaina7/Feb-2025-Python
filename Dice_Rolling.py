#Loop
import random

while True: 
  choice = input("Do you want to roll the Dice?, (y/n): ").lower()
  if choice == "y":
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f"({die1}, {die2})")

  elif choice == "n":
    print("Thank You For Playing")
    break
  else:
     print("Please input a valid choice")
