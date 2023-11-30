import random

record_num = 30
record_element_num = 30



def reset_radom_file():
    file_name = "dane.txt"

    with open(file_name, 'w') as file:
        # Write content to the file
        for i in range(0,record_num):
            for j in range(0,record_element_num):
                random_number = random.randint(0, 9)
                file.write(str(random_number )+" ")
            file.write("\n")


reset_radom_file()