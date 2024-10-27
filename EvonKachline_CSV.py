import csv

def main():
    
#Ask how many students are being tested
    student_amount = int(input("How many students took the exam? "))

#Create grades.csv
    with open('grades.csv', 'w', newline='') as exc:
        writer = csv.writer(exc)

# Write the names for each column
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

#Write the first and last names of the students, and their exam scores
        for i in range(student_amount):

            first_name = input("Enter first name of student: ")
            
            last_name = input("Enter last name of student: ")
            
            exam1 = int(input("Enter exam 1 score: "))
                      
            exam2 = int(input("Enter exam 2 score: "))
                      
            exam3 = int(input("Enter exam 3 score: "))
                      
            writer.writerow([first_name, last_name, exam1, exam2, exam3])


        print("All grades have been entered. ")
        
main()






import csv

def main():

    # Open grades.csv excal file
    with open('grades.csv', 'r') as csv_exc:
        csv_reader = csv.reader(csv_exc, delimiter=',')

        #What to print in each row according to the grades.csv file 
        for row in csv_reader:
            print(f'{row[0]:<16} {row[1]:<16} {row[2]:<8} {row[3]:<8} {row[4]:<8}')

main()

