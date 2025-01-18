import random

number_of_choices = int(input("Please Give the number of Choices"))

Choices = []
count = 0
for choice in range(number_of_choices):
  count += 1
  choice = str(input(f"Please give your Choice {count}: "))
  Choices.append(choice)

print("Your Total number of Choices are: ", count)
print("This is just a funny project, Use at your own risk, /n  We are not responsible for any cause that happend to you by using this automated decision maker.")

def final_decision(Choices):
  decision = random.choice(Choices)
  statement = "Randomly choosen choice is: "
  print(statement + decision)

final_decision(Choices)

realesed = ""
