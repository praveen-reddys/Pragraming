student_id=int(input("enter student id : "))
student_name=input("enter student name : ")
attendence=float(input("enter student attendence : "))
no_of_subjects=0
total_score=0
while True:
    score=int(input(f"enter score for individual subject{no_of_subjects +1} : "))
    total_score+=score
    no_of_subjects+=1
    another_score=input("do you want to enter another score?(yes/no)")
    if another_score!="yes":
        break
average_score=total_score/no_of_subjects
if attendence>=85:
    performance="excellent"
elif attendence>=70 and attendence<=84:
    performance="good"
elif attendence>=50 and attendence<=69:  
    performance="average" 
else:
    performance="need's improvement"
if attendence<=75:
    print("warning low attendence")
else:
    print("attendence satisfied")        
    
print(f"student name : {student_name}") 
print(f"student id : {student_id}")            
print(f"average score : {average_score}")
print(f"student attendence : {attendence}")    
print(f"no of subjects : {no_of_subjects}")
print(f"total score : {total_score}")
print(f"performance : {performance}")