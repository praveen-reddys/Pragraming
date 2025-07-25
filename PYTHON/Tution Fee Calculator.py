student_name=input("ENTER YOUR NAME:    ")
student_class=int(input("ENTER YOUR CLASS:  "))
base_tution_fee=int(input("ENTER TUTION FEE:  "))
academic_topper=input("ACADEMIC TOPPER YES OR NO:  ")
discount_percentage=0

if student_class>=1 and student_class<=12:
    if student_class>=9 and student_class<=12:
        if academic_topper=="YES":
            total_discount=20
        else:
            total_discount=10
    elif student_class>=6 and student_class<=8:
        total_discount=5
    else:
        total_discount=0
        
    if student_class == 10:
        total_discount = total_discount + 3
    elif student_class == 12:
        total_discount = total_discount + 5
    else:
        total_discount = total_discount + 0

    if discount_percentage > 0:
        total_discount = total_discount + discount_percentage

    discount_amount = (base_tution_fee * total_discount) / 100
    final_fee = base_tution_fee - discount_amount

    print(f"student name: {student_name}")
    print(f"Grade: {student_class}")
    print(f"academic topper: {academic_topper}")
    print(f"base tuition fee: {base_tution_fee}")
    print(f"total discount: {total_discount}%")
    print(f"discount amount: {discount_amount}")
    print(f"final tuition fee: {final_fee}")
else:
    print("invalid grade")
        
        
