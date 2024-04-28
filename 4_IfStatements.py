temperature =25
if temperature > 30:
    print ("It is hot today")
    print ("Drink a lot of water today!")
elif temperature > 20: # (20, 30]
    print ("It is a nice day")
elif temperature > 10: # (10, 20]
    print ("It is a bit cold day")
else:
    print ("It is cold")
print ('Done')
