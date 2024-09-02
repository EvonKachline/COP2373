#Evon Kachline
#Programming Exercise 1B



#This fuction will keep in the code, telling it to read the txt doc to get the repsonces.
def read_txt():
#This tells the program to pick a random repsonse form the file
    import random

#This varible is the file that we made with the responses
    filename = "8ball_responses.txt"

#This tells the program to open our txt file and to read it
    f=open(filename)

#This function will read all the lines into a list, with newline character at end of each line
    responses=f.readlines()

    f.close()



#This function tells the user what to put in if they have a question or want to quit
    ques=input("Enter your yes/no question or q to exit: ")

#This while loop will keep giving answers from the txt file until the user quits.
    while ques!='q':

        print(responses[random.randrange(0,len(responses))].strip())
    
        ques=input("Enter your yes/no question or q to exit: ")


read_txt()
