import csv

def write_into_csv(student_info_list):
    with open("student_info.csv", "a") as csv_file:
        writer = csv.writer(csv_file)

        if(csv_file.tell() == 0):
            writer.writerow(["Name", "Age", "Contact Number", "Email-ID"])
        
        writer.writerow(student_info_list)

condition = True
student_num = 1

while(condition):
    student_info = input("Enter the information of student #{} in the following format: (Name Age Contact Email) - ".format(student_num))
    print(student_info)

    student_info_list = student_info.split(' ')
    print("Name: {}\nAge: {}\nContact: {}\nEmail: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    confirmation = input("Please verify the student information. Do you wish to proceed? (yes/no): ")
    
    if confirmation == "yes":
        student_num += 1
        write_into_csv(student_info_list)
        condition_check = input("Do you want to enter another student information? (yes/no): ")
        if condition_check == "no":
            condition = False
    elif confirmation == "no":
        print("Please re-enter the values!\n")


    
    