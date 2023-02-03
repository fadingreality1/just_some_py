import os
import sys
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bids = {}
c = True

while c:
    print(logo)
    print("Welcome to secret Auction program.")
    name = input("What is your name:- ")
    bid = int(input("What's your bid? :- ₹"))
    bids[name] = bid
    Ch = input("Are there any other bidders? Type 'yes' or 'no'.:-").lower()
    if Ch[0] != 'y':
        c = False
    else:
        os.system('cls')

os.system('cls')

Max : int = -1*sys.maxsize - 1

max_b : str = ''

for i in bids:
    if Max < bids[i] :
        Max = bids[i]
        max_b = i

print(f"The winner is {max_b} with the amount ₹{max}")
