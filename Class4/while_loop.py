# answer = ""
#
# # while answer != "Q":
# #     answer = input("Give a value or string, enter Q to stop")
# #     if answer != "Q":
# #         print(answer)
#
# while True:
#     answer = input("Please enter the tip amount, A B C or D")
#     if answer.upper() in "ABCD" and len(answer) == 1:
#         break
#         print("Please re-enter the value")
#     else:
#         break
#
# print("Entered tip value " + answer)
#
# while True:
#     answer = input("Please enter the tip amount, A B C or D")
#     match answer:
#         case "A" | "B" | "C" | "D":
#             print(answer)
#             break
#         case _:
#             continue


# person_age = 17
#
# if person_age >= 18:
#     print("\nThis person is an adult.\n")
# else:
#     print("\nThis person is not an adult.\n")
#
# favorite_colour = "Red"
#
# if favorite_colour == "Blue":
#     print("Agreed.")
# elif favorite_colour == "Purple":
#     print("Still Agree.")
# else:
#     print("Not liking this colour.")

invoice = float(input("How much did you spend? "))


def discount():
    if invoice < 100:
        return 0
    elif 100 <= invoice < 250:
        return 0.1
    elif 250 >= invoice < 500:
        return 0.2
    elif 250 < invoice < 500:
        return 0.4
    elif invoice >= 500:
        return 0.5


def customer():
    if 0 > invoice < 500:
        return str("R")
    else:
        return str("W")


print(f"Customer type: {customer()}\n" + f"Discount percent: {discount()}")
