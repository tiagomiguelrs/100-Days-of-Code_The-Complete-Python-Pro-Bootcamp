from art import logo

print(logo)
bidders_dict = {}

keep_bidding = True
while keep_bidding:
    # TODO-3: Whether if new bids need to be added
    make_bid = input("Do you want to make a bid? Answer 'yes' to continue or 'no' to end bidding.\n").lower()

    # TODO-1: Ask the user for input
    if make_bid == "yes":
        name = input("Please write your name: ")
        value = int(input("Please place the value of your bid: $"))
        print("\n" * 20)

        # TODO-2: Save data into dictionary {name: price}
        bidders_dict[name] = value
    else:
        keep_bidding = False

# TODO-4: Compare bids in dictionary

# if len(bidders_dict) > 0:
# # Sorting the bidders' dictionary from lowest to highest value into a list
#     sorted_keys = sorted(bidders_dict, key=lambda v: bidders_dict[v], reverse=True)
#
#     print(f"The highest bidder is {sorted_keys[0]} with ${bidders_dict[sorted_keys[0]]}.")
#
# else:
#     print("No bids were placed.")

# OR

# if len(bidders_dict) > 0:
# # Sorting the bidders' dictionary from lowest to highest value into a list
#     max_bidder = max(bidders_dict, key=bidders_dict.get)
#
#     print(f"The highest bidder is {max_bidder} with ${bidders_dict[max_bidder]}.")
#
# else:
#     print("No bids were placed.")

# OR

# highest_value = 0
# highest_name = ""
# if len(bidders_dict) > 0:
#     for n, v in bidders_dict.items():
#         if v > highest_value:
#             highest_value = v
#             highest_name = n
#
#     print(f"The highest bidder is {highest_name} with ${highest_value}")
# else:
#     print("No bids were placed.")

