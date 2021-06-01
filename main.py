from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bit_dict = {}
other_interests = True


def fing_highers_bidder(bit_dict):
  # bit_dict = {"Anglea". 123, "James": 321}
  highest = 0
  winner = ""
  for bidder in bit_dict:
    bid_amount = bit_dict[bidder]
    if bid_amount > highest:
      highest = bit_dict[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bit of {highest} €.")



while other_interests:
  name = input("What is your name? ")
  bit = int(input("What is your bit? € "))
  bit_dict[name] = bit
  decission = input("Are there others, who are interested to bit? Type 'yes' or 'no' ")
  if decission == "no":
    print("Thank`s")
    fing_highers_bidder(bit_dict)
    other_interests = False
  else:
    clear()