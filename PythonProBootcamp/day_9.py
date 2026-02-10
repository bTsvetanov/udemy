biders = {}
while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    biders[name] = bid
    more_biders = input("Are there any other biders? Type 'yes' or 'no': ")
    if more_biders == "no":
        break
    else:
        print("\n" * 100)
max_bid = 0
winner = ""
for key in biders:
    if biders[key] > max_bid:
        max_bid = biders[key]
        winner = key
print(f"The winner is {winner} with a bid of ${max_bid}.")