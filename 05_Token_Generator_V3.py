import random 

# main routine goes here
tokens = ["unicorn","horse", "horse","horse",
          "zebra","zebra","zebra",
          "donkey","donkey", "donkey",]
STRARTING_BALANCE = 100

balance = STRARTING_BALANCE
#Testing loop to generate 20 tokens
for item in range (0,500):
    chosen = random. choice (tokens)

    # Adjust balance
    if chosen == "unicorn": 
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5 


print ()
print("Starting Balance: ${:.2f}".format (STRARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
