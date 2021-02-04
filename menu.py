# Author: James Underwood
# Github: https://github.com/JimNastic316
# Date:   2/4/2021
# Description: generic Python menu

menu_choices = "12"
choice = "-"     # initialize variable choice

while choice != "0":
    if choice in menu_choices:
        print(f"{choice} is a valid choice")
    else:
        print("Please select an option from below, or 0 to quit")
        print("\t1 - Enter an album title\n"
              "\t2 - Enter a song title\n"
              "\t0 - Quit")
    choice = input("Enter you selection: ")
print("Goodbye")

# selection = "-"
# while selection != "0":
#     if selection in "123456789":
#         print("You chose {}".format(selection))
#     else:
#         print("Please select an option from {} to {}, or 0 to quit"
#               .format(1, 9))
#         print("\t1. One\n\t2. Two\n\t3. Three\n\t4. Four\n\t5. Five\n"
#               "\t6. Six\n\t7. Seven\n\t8. Eight\n\t9. Nine\n\t0. Quit")
#     selection = input("Enter your selection: ")
#
# print("User ended")


