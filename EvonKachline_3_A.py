#Evon Kachline
#Programming Exercise 3A



#This code will ask the user for their expenses and tell the total and which is the highest and lowest. 
from functools import reduce

#This function has the user write their expense and how much it is.
def what_expenses():

    #Variables that hold all of the expenses and their prices.  
    expenses = []
    
    #A while loop to confirm that the user want to keep adding expenses.
    while True:
        expense_item = input("What is the expense (type 'done' when finish): ")
        if expense_item.lower() == 'done':
            break
        amount = float(input("How much is the expense: "))

        expenses.append((expense_item, amount))
    return expenses


#This function will calculate teh totoal of the expenses and find out which ones are the highest and the lowest. 
def calculate_expenses(expenses):
    
    #Adding the total of the expenses.
    total_expense_amount = reduce(lambda x, y: x + y[1], expenses, 0)
    
    #Comparing the expenses to see which one is the highest. 
    highest_expense_amount = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)
    
    #Compering the expenese to see which one is the lowest.
    lowest_expense_amount = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)
    return total_expense_amount, highest_expense_amount, lowest_expense_amount


#The main funcation to display the totals and highest and lowest expense.
def main():
    expenses = what_expenses()
    total_expense_amount, highest_expense_amount, lowest_expense_amount = calculate_expenses(expenses)

    print("\nTotal Expense: $", total_expense_amount)
    print("Highest Expense: $", highest_expense_amount[1], "with", highest_expense_amount[0])
    print("Lowest Expense: $", lowest_expense_amount[1], "with", lowest_expense_amount[0])


if __name__ == "__main__":
    main()



