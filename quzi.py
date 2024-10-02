score = 0

user_name = input("Enter your name: ")
print(user_name + "Welcome to my Big Brain Python Quiz")
answer_1 = input("Ehrrm How many brains does an octopus have")
right_answer = "4"
got_it_right = right_answer == answer_1
print(user_name + "It's " + str(got_it_right) + " that octopi have " + answer_1 + " brains.")
print(user_name + " It's " + str(got_it_right) + " that you have  at least one brain.")

score = score + int(got_it_right)

print("your score is " + str(score))
