import sys
import csv

def get_command_line_input():
    arr = []
    length = len(sys.argv)
    if(length <= 1):
        print("Add arguments!")
    else:
        for i in range(1, length):
            if(float(sys.argv[i]) <= 99.9):
                arr.append(float(sys.argv[i]))
            else:
                print("Need to enter decimal from 1 to 99.9!")
    return arr

def get_user_input():
    user_input = []
    try:
        user_input = list(map(float, input("Enter grades\n").split()))
        return user_input
    except ValueError:
        print("You entered a wrong value")


def read_from_csv_without_names(file):
    my_list = []
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            test = row
            my_list = row
            #print(', '.join(row))
    return my_list

def print_list(test):
    print(test)

def convert_num_to_letter(arr):
    grades = []
    for i in range(len(arr)):
        if(arr[i] <= 59.9):
            grades.append('F')
            # print("You got a F")
        elif(60 <= arr[i] <= 62.9):
            grades.append('D-')
            # print("You got a D-")
        elif(63 <= arr[i] <= 66.9):
            grades.append('D')
            # print("You got a D")
        elif(67 <= arr[i] <= 69.9):
            grades.append('D+')
            # print("You got a D+")
        elif(70 <= arr[i] <= 72.9):
            grades.append('C-')            
            # print("You got a C-")
        elif(73 <= arr[i] <= 76.9):
            grades.append('C')
            # print("You got a C")
        elif(77 <= arr[i] <= 79.9):
            grades.append('C+')
            # print("You got a C+") 
        elif(80 <= arr[i] <= 82.9):
            grades.append('B-')            
            # print("You got a B-")
        elif(83 <= arr[i] <= 86.9):
            grades.append('B')            
            # print("You got a B") 
        elif(87 <= arr[i] <= 89.9):
            grades.append('B+')            
            # print("You got a B+")
        elif(90 <= arr[i] <= 92.9):
            grades.append('A-')
            # print("You got a A")
        elif(93 <= arr[i] <= 99.9):
            grades.append('A')
            # print("You got a A")
    return grades

#A = 93-100
#A- = 90-92
#B+ = 87-89
#B = 83-86
#B- = 80-82
#C+ = 77-79
#C = 73-76
#C- = 70-72
#D+ = 67-69
#D = 63-66
#D- = 60-62
#F = 0-59

if __name__ == '__main__':
    choice = ""
    print("To enter user input, type U")
    print("To load a csv file, type C")
    try:
        choice = str(input("Enter your choice:\n"))   
        if(choice == "U"):
            user_inp = get_user_input()
            print_list(user_inp)
            grades = convert_num_to_letter(user_inp)
            print_list(grades)
#            cmd = get_command_line_input()
#            print_list(cmd)
#            grades = convert_num_to_letter(cmd)
#            print_list(grades)
        elif(choice == "C"):
            file_name = str(input("Enter name of csv file:\n"))
            read_from_csv_without_names(file_name)

    except ValueError:
            print("Enter valid choice")

                # file_name = input("Enter csv file")
