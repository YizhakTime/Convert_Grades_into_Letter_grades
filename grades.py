import csv
import sys


def get_command_line_input():
    arr = []
    length = len(sys.argv)
    if length <= 1:
        print("Add arguments!")
    else:
        for i in range(1, length):
            if float(sys.argv[i]) <= 99.9:
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


def read_from_csv(file):
    my_list = []
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        next(reader, None)
        for row in reader:
            my_list.append(row)
    return my_list


def write_csv(file, csv_list):
    header = ["Names", "Grades"]
    csv_list.insert(0, header)
    with open(file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=" ")
        for i in range(0, len(csv_list)):
            writer.writerow(csv_list[i])


def print_list(test):
    print(test)


def convert_num_to_letter(arr):
    grades = []
    if any(isinstance(el, list) for el in arr) is True:
        # any() returns true if ANY of elements in the tuple, list are true
        # isinstance() returns true if ANY of the elements in the object (list in this case) is a list
        for i in range(0, len(arr)):
            for j in range(1, len(arr[i])):
                if float(arr[i][j]) <= 59.9:
                    arr[i][j] = "F"
                    # print("You got a F")
                elif 60 <= float(arr[i][j]) <= 62.9:
                    arr[i][j] = "D-"
                    # print("You got a D-")
                elif 63 <= float(arr[i][j]) <= 66.9:
                    arr[i][j] = "D"
                    # print("You got a D")
                elif 67 <= float(arr[i][j]) <= 69.9:
                    arr[i][j] = "D+"
                    # print("You got a D+")
                elif 70 <= float(arr[i][j]) <= 72.9:
                    arr[i][j] = "C-"
                    # print("You got a C-")
                elif 73 <= float(arr[i][j]) <= 76.9:
                    arr[i][j] = "C"
                    # print("You got a C")
                elif 77 <= float(arr[i][j]) <= 79.9:
                    arr[i][j] = "C+"
                    # print("You got a C+")
                elif 80 <= float(arr[i][j]) <= 82.9:
                    arr[i][j] = "B-"
                    # print("You got a B-")
                elif 83 <= float(arr[i][j]) <= 86.9:
                    arr[i][j] = "B"
                    # print("You got a B")
                elif 87 <= float(arr[i][j]) <= 89.9:
                    arr[i][j] = "B+"
                    # print("You got a B+")
                elif 90 <= float(arr[i][j]) <= 92.9:
                    arr[i][j] = "A-"
                    # print("You got a A")
                elif 93 <= float(arr[i][j]) <= 99.9:
                    arr[i][j] = "A"
    else:
        for i in range(len(arr)):
            if arr[i] <= 59.9:
                grades.append("F")
                # print("You got a F")
            elif 60 <= arr[i] <= 62.9:
                grades.append("D-")
                # print("You got a D-")
            elif 63 <= arr[i] <= 66.9:
                grades.append("D")
                # print("You got a D")
            elif 67 <= arr[i] <= 69.9:
                grades.append("D+")
                # print("You got a D+")
            elif 70 <= arr[i] <= 72.9:
                grades.append("C-")
                # print("You got a C-")
            elif 73 <= arr[i] <= 76.9:
                grades.append("C")
                # print("You got a C")
            elif 77 <= arr[i] <= 79.9:
                grades.append("C+")
                # print("You got a C+")
            elif 80 <= arr[i] <= 82.9:
                grades.append("B-")
                # print("You got a B-")
            elif 83 <= arr[i] <= 86.9:
                grades.append("B")
                # print("You got a B")
            elif 87 <= arr[i] <= 89.9:
                grades.append("B+")
                # print("You got a B+")
            elif 90 <= arr[i] <= 92.9:
                grades.append("A-")
                # print("You got a A")
            elif 93 <= arr[i] <= 99.9:
                grades.append("A")
                # print("You got a A")
    return grades


# A = 93-100
# A- = 90-92
# B+ = 87-89
# B = 83-86
# B- = 80-82
# C+ = 77-79
# C = 73-76
# C- = 70-72
# D+ = 67-69
# D = 63-66
# D- = 60-62
# F = 0-59


if __name__ == "__main__":
    choice = ""
    print("To enter user input, type U")
    print("To load a csv file, type C")
    try:
        choice = str(input("Enter your choice:\n"))
        if choice == "U":
            user_inp = get_user_input()
            print_list(user_inp)
            grades = convert_num_to_letter(user_inp)
            print_list(grades)
        elif choice == "C":
            try:
                file_name = str(input("Enter name of csv file:\n"))
                csv_data = read_from_csv(file_name)
                convert_num_to_letter(csv_data)
                write_csv(file_name, csv_data)
                # print_list(csv_data)
            except ValueError:
                print("CSV file does not exist or is corrupted")
    except ValueError:
        print("Enter valid choice")
