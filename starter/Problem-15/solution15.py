

lstudent_1 = [40, 35, 70, 90, 56]


student_2 = [57, 35, 80, 98, 46]


def avg(marks):
    if any(mark < 40 for mark in marks):
        return "FAILED"
    else:
        avg =sum(marks)/len(marks)
        return avg
    

print("Student 1 Average: ", avg(lstudent_1)) # FAILED
print("Student 2 Average: ", avg(student_2)) # FAILED
