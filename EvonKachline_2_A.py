#Evon Kachline
#Programming Exercise 2A


#Defining the spam keywords that the program needs to catch. 
spam_keywords = [
    "Free", "Winner", "Congratulations", "Click here", "Apply now", "Limited time", "Urgent", "Offer", "Buy now",
    "Discount", "Cash", "Prize", "Risk-free", "Guarantee", "No obligation", "Special promotion", "Call now",
    "Order now", "100% free", "Credit card", "Dont Hesitate", "Deal", "Save big", "Earn money", "profit", "Lottery",
    "ACT Now", "Double Your Income", "Free trial", "Satisfaction guaranteed"
]

#Define the function that will find the score of spam in the message.
#It is made to find how many spam words are in the message. 
def find_spam_score(email_message):
    spam_score = 0
    found_keywords = []
    
    for keyword in spam_keywords:
        if keyword.lower() in email_message.lower():
            spam_score += 1
            found_keywords.append(keyword)
    
    return spam_score, found_keywords

#Define the fuction that will rate the likelihood of a spam message.
#This will take the score and see how likely it is a spam message.
def rate_spam_score(spam_score):
    if spam_score == 0:
        return "Not Spam"
    elif spam_score <= 5:
        return "Low chance of Spam"
    elif spam_score <= 15:
        return "could be spam Spam"
    else:
        return "Is a Spam message"


#Define the main fuction, this is main body of the program.
#This will display all the results of the other two functions. 
def main():
    email_message = input("Enter the email message: ")
    spam_score, found_keywords = find_spam_score(email_message)
    spam_rate = rate_spam_score(spam_score)
    
    print(f"Spam Score: {spam_score}")
    print(f"Likelihood of Spam: {spam_rate}")
    if found_keywords:
        print("Keywords found in the message:")
        for keyword in found_keywords:
            print(f"- {keyword}")

if __name__ == "__main__":
    main()
