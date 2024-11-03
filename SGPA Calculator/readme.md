
# UGC Uniform Grading System

## Overview

The UGC Uniform Grading System is a Python program designed to calculate the Semester Grade Point Average (SGPA) for students based on their course credits and grades. This system implements a grading scale and provides academic results, including the total credits taken, SGPA, and remarks based on the calculated SGPA.

## Features

- Displays a grading scale with corresponding grade points.
- Allows input of student information such as name and ID.
- Accepts multiple courses, their credits, and the corresponding grade points.
- Calculates and displays individual course results.
- Computes the SGPA based on course credits and grades.
- Provides overall academic remarks based on the SGPA.

## Grading Scale

The grading scale used in the system is as follows:

| Marks Obtained | Letter Grade | Grade Point |
|----------------|--------------|-------------|
| 80-100         | A+           | 4.00        |
| 75-79          | A            | 3.75        |
| 70-74          | A-           | 3.50        |
| 65-69          | B+           | 3.25        |
| 60-64          | B            | 3.00        |
| 55-59          | B-           | 2.75        |
| 50-54          | C+           | 2.50        |
| 45-49          | C            | 2.25        |
| 40-44          | D            | 2.00        |
| 0-39           | F            | 0.00        |

## Usage

1. Run the Python script in a suitable Python environment (Python 3.x recommended).
2. Input the required student details:
   - Name
   - ID
   - Total number of courses
3. For each course, input:
   - Course Name
   - Course Credit
   - Course Grade Point
4. The program will output the academic results, including:
   - Individual course grades and grade points.
   - Total credits taken.
   - Calculated SGPA.
   - Total Grade and Remarks based on the SGPA.

## Code Structure

```python
# Grading System Code
print("     ----- UGC Uniform Grading System -----\n <-------------------------------------------->\n")
# Grading scale display
print("Marks_Obtain --- Latter_Grade --- Grade_Point\n  80-100            A+              4.00\n  75-79             A               3.75\n  70-74             A-              3.50\n  65-69             B+              3.25\n  60-64             B               3.00\n  55-59             B-              2.75\n  50-54             C+              2.50\n  45-49             C               2.25\n  40-44             D               2.00\n  00-39             F               0.00")
# User input for student details
name = input("Name: ")
id = input("ID: ")
total_course = int(input("Total Course: "))
# Course data storage
course_name = []
credit = []
point = []
count = 0
course_result_multiply = 0

# Loop for course input
for i in range(total_course):
    c_name = input("Course Name: ")
    c_credit = int(input("Course Credit: "))
    Grade = float(input("Course Grade Point:"))
    count += c_credit
    course_result_multiply += (c_credit * Grade)
    course_name.append(c_name)
    credit.append(c_credit)
    point.append(Grade)
    print()

# Displaying academic results
print("----- A C A D E M I C  R E S U L T ----- \n\n")
print("Name: ", name)
print("ID: ", id)
print("------------------------------------------------------------------------")
# Course result output
for i in range(total_course):
    # Determining letter grades and displaying results
    if(point[i] == 4.00):
        grade = "A+"
    elif(point[i] == 3.75):
        grade = "A"
    elif(point[i] == 3.50):
        grade = "A-"
    elif(point[i] == 3.00):
        grade = "B+"
    elif(point[i] == 2.75):
        grade = "B-"
    elif(point[i] == 2.25):
        grade = "C"
    elif(point[i] == 2.00):
        grade = "D"
    else:
        grade = "F"
        
    print("Course title: {}".format(course_name[i]), "\tCredit: {}".format(credit[i]), "\tGrade: {}".format(grade), "\tGrade Point: {}".format(point[i]), "\n--------------------------------------------------------------------------")

# SGPA calculation and output
sgpa = course_result_multiply / count
print("Total Credits Taken: {}".format(count))
print("SGPA: %.2f" % (sgpa))

# Remarks based on SGPA
if(sgpa == 4.00):
    print("Total Grade: A+")
    print("Remarks : Outstanding")
elif(sgpa >= 3.75 and sgpa <= 3.99):
    print("Total Grade: A")
    print("Remarks : Excellent")
elif(sgpa >= 3.50 and sgpa <= 3.74):
    print("Total Grade: A-")
    print("Remarks : Very Good")
elif(sgpa >= 3.00 and sgpa <= 3.49):
    print("Total Grade: B+")
    print("Remarks : Satisfactory")
elif(sgpa >= 2.75 and sgpa <= 2.99):
    print("Total Grade: B")
    print("Remarks : Above Average")
elif(sgpa >= 2.50 and sgpa <= 2.74):
    print("Total Grade: B-")
    print("Remarks : Average")
elif(sgpa >= 2.25 and sgpa <= 2.49):
    print("Total Grade: C")
    print("Remarks : Below Average")
elif(sgpa >= 2.00 and sgpa <= 2.24):
    print("Total Grade: D")
    print("Remarks : Pass")
elif(sgpa >= 0.00 and sgpa <= 1.99):
    print("Total Grade: F")
    print("Remarks : Fail")
