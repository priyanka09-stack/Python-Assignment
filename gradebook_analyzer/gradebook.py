# Priyanka Singh
# 22/11/2025
# Gradebook Analyzer CLI

import csv

print("Welcome to Gradebook Analyzer CLI! This mini project will help you analyze and grade student scores.")

#Task 3 
#average marks
def calculate_average(marks_dict):
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)

#median marks
def calculate_median(marks_dict):
    if not marks_dict:
        return 0

    median_marks = sorted(marks_dict.values())
    n = len(median_marks)
    mid = n // 2
#using if-else conditionals for calculating median for even and odd numbers
    if n % 2 == 0:
        return (median_marks[mid - 1] + median_marks[mid]) / 2                      #even no.
    else:
        return median_marks[mid]                                                #odd  no.

#maximum marks
def find_max_marks(marks_dict):
    if not marks_dict:
        return None, None
    name = max(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

#min marks
def min_marks(marks_dict):
    if not marks_dict:
        return None, None
    name = min(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]


# Statistical Output
#defining statistical output 
def statistical_output(marks_dict):

    avg = calculate_average(marks_dict)
    med = calculate_median(marks_dict)
    max_name, max_score = find_max_marks(marks_dict)
    min_name, min_score = min_marks(marks_dict)
#printing analysis
    print("\n--- Analysis Summary ---")
    print(f"1 - Average Marks : {avg}")
    print(f"2 - Median Marks  : {med}")
    print(f"3 - Highest Marks : {max_score} ({max_name})")
    print(f"4 - Lowest Marks  : {min_score} ({min_name})")


#Task 2

#entering data manually

def manual_input():
    marks_ = {}
    n = int(input("Enter the number of student data you want to enter: "))
    for _ in range(n):
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        marks_[name] = marks
    return marks_

#function to define csv input
def csv_input():
    marks_ = {}
    file_name = input("Enter CSV file name with extension: ")
    try:
        with open(file_name, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            print("Detected columns:", reader.fieldnames)
            for row in reader:
                marks_[row['name']] = int(row['marks'])
        print("csv file loaded.")
        return marks_
    except FileNotFoundError:
        print("Error")
        return {}

#definning function to assign grades

def assign_grades(marks_dict):
    grades = {}                          #empty dictionary
    for name, score in marks_dict.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

#defininig function for grade distribution
def grade_distribution(grades_dict):
    distribution = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for grade in grades_dict.values():
        if grade in distribution:
            distribution[grade] += 1
    return distribution

#defining function for pass and fail students list

def pass_fail_lists(marks_dict):
    passed_students = [name for name, score in marks_dict.items() if score >= 40]
    failed_students = [name for name, score in marks_dict.items() if score < 40]
    print("\nPassed Students (>=40):", len(passed_students), passed_students)
    print("Failed Students (<40):", len(failed_students), failed_students)

#defining function to print results in table form

def print_results_table(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("-"*30)
    for name, marks in marks_dict.items():
        grade = grades_dict.get(name, "-")
        print(f"{name:<10}\t{marks:<5}\t{grade}")

#Bonus - Export  report to a CSV file

def export_to_csv(marks_dict, grades_dict):
    file_name = input("Enter filename for exporting results (e.g., output.csv): ")
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Grade"])
        for name, marks in marks_dict.items():
            writer.writerow([name, marks, grades_dict[name]])
    print("Results exported successfully!")


#Main Loop to execute above functions

while True:
    input_method = input("Enter Marks- Manually(M) or csv file(C), or Q to quit: ").upper()

    if input_method == "M":
        student_data = manual_input()

    elif input_method == "C":
        student_data = csv_input()

    elif input_method == "Q":
        print("Exit.")
        break

    else:
        print("Invalid Input .Enter eitherM , C or Q")
        continue

    if not student_data:
        print("No student data available. Returning to main menu.")
        continue

    print("\nStudent Data:", student_data)

    grades = assign_grades(student_data)
    distribution = grade_distribution(grades)
    print("\n Grade Distribution:", distribution)

 #passed and failed students
    pass_fail_lists(student_data)
#statiscal anlysis
    statistical_output(student_data)
#Table 
    print_results_table(student_data, grades)

    export_choice = input("\n Do you want to export the results to CSV? (Y/N): ").upper()
    if export_choice == "Y":
        export_to_csv(student_data, grades)


#Loop to repeat the whole process
    repeat = input("\n Enter another data set? (Y/N): ").upper()
    if repeat != "Y":
        print("Exiting program")
        break




    