
print("     ----- UGC Uniform Grading System -----\n <-------------------------------------------->\n")
print("Marks_Obtain --- Latter_Grade --- Grade_Point\n  80-100            A+              4.00\n  75-79             A               3.75\n  70-74             A-              3.50\n  65-69             B+              3.25\n  60-64             B               3.00\n  55-99             B-              2.75\n  50-54             C+              2.50\n  45-49             C               2.25\n  40-44             D               2.00\n  00-39             F               0.00")

print()
name = input("Name: ")
id = input("ID: ")
total_course= int(input("Total Course: "))
print()

course_name = []
credit = []
point = []

count = 0
course_result_multiply = 0

for i in range(total_course):
    c_name = input("Course Name: ")
    c_creadit = int(input("Course Creadit: "))
    Grade = float(input("Course Grade_Point:"))
    
    count += c_creadit
    course_result_multiply += (c_creadit * Grade)
    
    course_name.append(c_name)
    credit.append(c_creadit)
    point.append(Grade)
    
    print()
print("----- A C A D E M I C  R E S U L T ----- \n\n")  
print("Name: ",name)
print("ID: ",id)

print("------------------------------------------------------------------------")
for i in range(total_course):
    
    if(point[i]==4.00):
         print("Course title: {}".format(course_name[i]),"\tCreadit: {}".format(credit[i]),"\tGrade: A+","\tGrade Point: {}".format(point[i]),"\n--------------------------------------------------------------------------")
    elif(point[i]==3.75):
         print("Course title: {}".format(course_name[i]),"\tCreadit: {}".format(credit[i]),"\tGrade: A","\tGrade Point: {}".format(point[i]),"\n--------------------------------------------------------------------------")
    elif(point[i]==3.50):
         print("Course title: {}".format(course_name[i]),"\tCreadit: {}".format(credit[i]),"\tGrade: A-","\tGrade Point: {}".format(point[i]),"\n--------------------------------------------------------------------------")
    elif(point[i]==3.00):
        print("Course title: {}".format(course_name[i]),"\tCreadit: {}".format(credit[i]),"\tGrade: B+","\tGrade Point: {}".format(point[i]),"\n--------------------------------------------------------------------------")
    elif(point[i]==2.50):
        print("Course title: {}".format(course_name[i]),"\tCreadit: {}".format(credit[i]),"\tGrade: B-","\tGrade Point: {}".format(point[i]),"\n--------------------------------------------------------------------------")
    elif(point[i]==	2.25):
        print("Course title: {}".format(course_name[i]),"\tCreadit: {}".format(credit[i]),"\tGrade: C","\tGrade Point: {}".format(point[i]),"\n--------------------------------------------------------------------------")
    elif(point[i]==2.00):
        print("Course title: {}".format(course_name[i]),"\tCreadit: {}".format(credit[i]),"\tGrade: D","\tGrade Point: {}".format(point[i]),"\n--------------------------------------------------------------------------")
    else:
        print("Course title: {}".format(course_name[i]),"\tCreadit: {}".format(credit[i]),"\tGrade: F","\tGrade Point: {}".format(point[i]),"\n--------------------------------------------------------------------------")
    
    
sgpa = course_result_multiply/count
print("Total Creadits Taken: {}".format(count))
print("SGPA: %.2f"%(sgpa))

if(sgpa==4.00):
    print("Total Grade: A+")
    print("Remarks : Outstanding")
elif(sgpa>=3.75 and sgpa<=3.99):
    print("Total Grade: A")
    print("Remarks : Excellent")
elif(sgpa>=3.50 and sgpa<=3.74):
    print("Total Grade: A-")
    print("Remarks : Very Good")
elif(sgpa>=3.00 and sgpa<=3.49):
    print("Total Grade: B+")
    print("Remarks : Satisfactory")
elif(sgpa>=2.75 and sgpa<=2.99):
    print("Total Grade: B")
    print("Remarks : Above Average")
elif(sgpa>=2.50 and sgpa<=2.74):
    print("Total Grade: B-")
    print("Remarks : Average")
elif(sgpa>=2.25 and sgpa<=2.49):
    print("Total Grade: C")
    print("Remarks : Bellow Average")
elif(sgpa>=2.00 and sgpa<=2.24):
    print("Total Grade: D")
    print("Remarks : Pass")
elif(sgpa>=0.00 and sgpa<=1.99):
    print("Total Grade: F")
    print("Remarks : Fail")
    
    
    
    
