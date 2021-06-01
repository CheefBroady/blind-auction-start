from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bit_dict = {}
other_interests = True
highest = 0
winner = ""

while other_interests:
  name = input("What is your name? ")
  bit = int(input("What is your bit? € "))
  bit_dict[name] = bit
  decission = input("Are there others, who are interested to bit? Type 'yes' or 'no' ")
  if decission == "no":
    print("Thank`s")
    for value in bit_dict:
      if bit_dict[value] > highest:
        highest = bit_dict[value]
        winner = value
    print(f"The winner is {winner} with a bit of {highest} €.")
    other_interests = False
  else:
    clear()
    name = input("Whats your name? ")
    bit = int(input("whats your bit? € "))