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
        choice = str(input("Enter whether you want to enter grades via user input or read from csv file\n"))   
    except ValueError:


def read_from_csv(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

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
    print("You can either enter grades via user input or via csv file\n")
    print("To enter via UI, enter U, or if you want to enter csv, enter C")
    try:
        choice = str(input("Enter whether you want to enter grades via user input or read from csv file\n"))   
        if(choice == "U"):
#            cmd = get_command_line_input()
#            print_list(cmd)
#            grades = convert_num_to_letter(cmd)
#            print_list(grades)
        elif(choice == "C"):

    except ValueError:
            print("Enter valid choice")

   
                # file_name = input("Enter csv file")
