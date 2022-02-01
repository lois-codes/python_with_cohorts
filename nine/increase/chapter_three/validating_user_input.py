# (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. For any
# input, if the value entered is other than 1 or 2, keep looping until the user enters a correct
# value. Use one counter to keep track of the number of passes, then calculate the number
# of failures after all the user’s inputs have been received.

passes = 0
failure = 0
user_input = int(input('Enter result(1= pass, 2= failure):'))
for number in range(10):
    while user_input < 0 or user_input > 2:
        user_input = int(input('Invalid input...Try again!Enter result(1= pass, 2= failure):'))
    if user_input == 1 :
        passes = passes + 1
    if user_input == 2:
         failure = failure + 1

    user_input = int(input('Enter result(1= pass, 2= failure):'))
       
if passes > 0 or failure > 0 :
    print("passed :", passes)
    print("failed: ",failure )
else:
    print("No correct input...Try again!")

