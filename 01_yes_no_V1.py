# Ask the user if they have played before
show_instructions = input ("have you played this game before? ").lower()


# If they say yes, output 'program continues '
if show_instructions == "yes":
  print ("program continues")

elif show_instructions == "no":
  print("display instructions")

# If they say nom, output 'display instructions'
else:
  print ("please answer yes / no")

print ("you choose {}".format (show_instructions))