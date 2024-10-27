import re

#This will check if the sentences are correctly written. 
def sentence_check(sentences):

#The pattern the sentneces have to be in. 
    check = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    number = re.findall(check, sentences, flags=re.DOTALL | re.MULTILINE)


#Prints the sentence count
    sentenceNum = len(number)
    print(f"{sentenceNum} sentence(s): ")
    print(" ")


#Prints the correct sentences
    for i in number:
        print("->", i)


def main():

#Tell the user to write the sentneces
    print("Make sure there is a capital and a period.")
    sentences = input("Write your senences and then press enter: ")
    sentence_check(sentences)


main()
