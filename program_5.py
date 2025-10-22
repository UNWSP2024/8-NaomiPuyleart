# Naomi Puyleart
# 10/22/25
# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

course_pairs = {}

n = int(input("Enter the number of courses you would like to input. "))

for courses in range(n):
    course_id = input('Enter the course ID (ex. "COS 2005"). ')
    course_name = input('Enter the course name (ex. "Python Programming"). ')
    course_pairs[course_id] = course_name

subject = (input('Enter a subject (ex. "COS"). '))

print("These are the courses you entered that fall under the subject ", subject, ".", sep="")
for course_id, course_name in course_pairs.items():
    if course_id.startswith(subject):
        print(f"{course_id}: {course_name}")