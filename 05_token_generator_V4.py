import random 

# main routine goes here

STRARTING_BALANCE = 100

balance = STRARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range (0,10):
    chosen = random. randint (1,100)

    # Adjust balance
     if 1 <= chosen_num <= 5:
    if chosen = "unicorn" 
        balance += 4
    elif 6 <= chosen_num <= 36:    
       chosen = "donkey":
       balance -= 1
    else:
        if chosen_num % 2 == 0:
         chosen = "horse"
        else:
            chosen = "zebra"     
        balance -= 0.5 

print ("You got a {}. your balance is
       "$ {:.2f}".format(chosen, balance))
                                                                                                                                                                                               
