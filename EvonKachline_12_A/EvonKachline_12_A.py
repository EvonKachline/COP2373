import numpy as np
import csv

#Load and read the CSV document.
def load_CSV(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  
        CSV = []
        for row in reader:
            CSV.append(row[2:])  
    return np.array(CSV, dtype=int)

#Tells the program to print the first 5 sets. 
def first_few_rows(CSV, num_rows=5):
    print("First few rows of the grade document:")
    print(CSV[:num_rows])

# Calculate and print statistics for each exam
def exam_statistics(CSV):
    print("\nExam Statistics:")
    num_exams = CSV.shape[1]
    for n in range(num_exams):
        exam_scores = CSV[:, n]
        print(f"Exam {n+1}:")
        print(f"    Mean: {np.mean(exam_scores):.2f}")
        print(f"    Median:: {np.median(exam_scores):.2f}")
        print(f"    Standard Deviation: {np.std(exam_scores):.2f}")
        print(f"    Minimum: {np.min(exam_scores)}")
        print(f"    Maximum: {np.max(exam_scores)}")

# Calculate and print overall statistics for all exams combined
def overall_statistics(CSV):
    all_scores = CSV.flatten()
    print("\nOverall statistics for all exams:")
    print(f"    Mean: {np.mean(all_scores):.2f}")
    print(f"    Median: {np.median(all_scores):.2f}")
    print(f"    Standard Deviation: {np.std(all_scores):.2f}")
    print(f"    Minimum: {np.min(all_scores)}")
    print(f"    Mamimum: {np.max(all_scores)}")

# Determine and print the number of students who passed and failed each exam
def pass_fail(CSV, passing_grade=60):
    num_exams = CSV.shape[1]
    for n in range(num_exams):
        exam_scores = CSV[:, n]
        passed = np.sum(exam_scores >= passing_grade)
        failed = np.sum(exam_scores < passing_grade)
        print(f"\nExam {n+1}:")
        print(f"    Passed: {passed}")
        print(f"    Failed: {failed}")

# Calculate and print the overall pass percentage across all exams
def pass_percentage(CSV, passing_grade=60):
    total_students = CSV.shape[0] * CSV.shape[1]
    passed_students = np.sum(CSV >= passing_grade)
    pass_percentage = (passed_students / total_students) * 100
    print(f"\nOverall pass percentage: {pass_percentage:.2f}%")

# Main function to run all tasks
def main():
    filename = 'grades.csv'
    CSV = load_CSV(filename)
    first_few_rows(CSV)
    exam_statistics(CSV)
    overall_statistics(CSV)
    pass_fail(CSV)
    pass_percentage(CSV)

if __name__ == '__main__':
    main()
