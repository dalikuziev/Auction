import os
from emoji import logo

bids = {}
play = "yes"
i = 1

while play == "yes":
  print(logo)
  name = input(f"{i}-ishtirokchi ismingizni kiriting: ")
  price = int(input("necha dollorga baxolaysiz: $"))
  bids[name] = price
  play = input("yana ishtirokchi qo'shasizmi yes/no: ")
  if play == "yes":
    os.system('cls')
    i += 1

def highest_bid(bids):
  highest_bid = 0
  winner = ""
  for name in bids:
    amount = bids[name]
    if amount > highest_bid:
      highest_bid = amount
      winner = name
  print(f"Bu auksionda ${highest_bid} taklif qilgan {winner.title()} g'olib bo'ldi")
highest_bid(bids)
