# hello.py CSC 110 Examples
# Program to prompt the user for their name, favorite color and more, 
# then say hello to the user
# By Zekarias Araya 
# April 9, 2014

after_study = "What would you like to be when you finish your study? "
name       = input('Please enter your name: ')
print("Hello {} Nice to meet you.".format(name))
print("Mine is Zekarias")
fav_color  = input("What's your favorite color? ")
print("Your favorite color is {0}. Many people like {0}.".format(fav_color))
your_major = input("What is your major? ")
print("Your major is {}. interesting.".format(your_major.upper()))
your_minor = input("What is your minor? ")
print("Your minor is", your_minor)
you_like_to_be = input(after_study)
print("You would like to be {} when you finish your study.".format(you_like_to_be))
important_to_you = input("What is important to you beside your school? ")
print("You are right {} is important too".format(important_to_you))
after_5_years = input("Where do you see yourself 5 years from now? ")
print("You would see yourself {} after 5 years".format(after_5_years))
your_goals = input("What are your goals for the next five years / ten years? ")
print("Your goals for the next 5 years / ten are {}".format(your_goals))
plan_to_achieve = input("How do you plan to achieve those goals? ")
print("You plan to achieve your those goals by {}".format(plan_to_achieve))

# assign all the user's reply to the variable 'replies'.
replies = (name, fav_color, your_major, your_minor, you_like_to_be, 
           important_to_you, after_5_years, your_goals, plan_to_achieve)

print("You have replyed", len(replies), "Quastions & here below are your answers: ")
print('')

# Iterate through the user reply and print those words(upper-case) out separately.
for r in replies: print(r.upper())
print('')

# input rate data from the user. 
rate = int(input("If you were to rate my application 1 up-to 5 what would it be: "))

# conditional: returns rate number and "thank you" message to the user.
if rate >= 5:
	print("Thank for rating {}".format(rate))
elif rate == 4:
	print("Thank for rating {}".format(rate))
elif rate == 3:
	print("Thank for rating {}".format(rate))
elif rate == 2:	
	print("Thank for rating {}".format(rate))
elif rate == 1:
	print("Thank for rating {}".format(rate))
elif rate == 1:
  print("Thank you for rating I will do my best next time")
else:
  print("Thank you for not rating")
print("Thank you.")