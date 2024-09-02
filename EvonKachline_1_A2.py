#Evon Kachline
#Programming Exercise 1A




#The Variable that tells the program how many tickets can be sold
total_tickets = 20

#The variable that tells the remaining tickets left. It starts off with the oringal.
remaining_tickets = total_tickets

#The variable that tells how many buyers. There is no buyers yet.
total_buyers = 0

#The whole code is in a while loop.
#This is used so that the program can figure out if the inputs of tickets arecorrect and when they run out

while remaining_tickets > 0:
    
#First we use a print function to tell the user how many are remaining.
#The function will start with our variabel of 20.
    print(f"There are currently {remaining_tickets} tickets remaining.")
    
#We then have our input for the user. They will have to input how many tickets they want.
    num_tickets = int(input("How many tickets would you like to purchase? "))
    
#The prompt said that only 4 tickets can be sold at a time.
#So we need to use an if function in order for the program to know if the user asked for too many tickets.
    if num_tickets > 4:
        
#This is what will print if the user ask for more then 4 tickets.
        print("Sorry, you cannot purchase more than 4 tickets.")
    
#We also need a conmand of if there is not enough tickets left.
#This will campart the amount of tickets to what is remaining.
    elif num_tickets > remaining_tickets:
        
        print("Sorry, there are not enough tickets remaining.")
        
#If the amount of tickets bought meets the amount still avaiable then the program will subtract it fromt he total remaining.
    else:
        remaining_tickets -= num_tickets
        total_buyers += 1
        
#Once all of the tickets are sold, this will display with how many buyers therewere.
print(f"The total number of buyers was {total_buyers}.")
