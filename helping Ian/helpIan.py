# code is meant to take 2 text documents, one with lbs broke and reason code
# as parameters and creates table from these. Second text has only reason codes parameter
# and assignes lbs broke, if able, based on previous table built.

reason_broke_file1 = {}
reason_broke_file2= {}
my_list1 = []
my_list2 = []

# requires file with both reason code and lbs broke
def set_primary_table(list):
    first_line_check = 0
    for line in list:
        a = line.split()
        # x_1 is reason code, set as key in dictionary
        # x_2 is value, set value to key (x_1)        
        x_1 = a[0]
        x_2 = a[1]

        # creates a key check to see if a key exists, if so, appends value
        # to reason code key's list, else creates aq new key with new value list
        key_check = 0
        for key in reason_broke_file1:
            if key == x_1:
                reason_broke_file1[x_1].append(int(x_2))
                key_check = 1
            else:
                continue
        if key_check == 0:
            if first_line_check == 0:
                reason_broke_file1[x_1] = [x_2]
                first_line_check = 1
            else:
                reason_broke_file1[x_1] = [int(x_2)]

# parses the reason codes from second document and adds corresponding lists
# of lbs broke and total
def fileParser(file):
    for line in file:
        x_1 = line.strip()
        for key in reason_broke_file1:
            if key == x_1:
                reason_broke_file2[x_1] = reason_broke_file1[x_1]

def main():
    
    # opens and sets text files to variables
    file1 = open("Small Projects\helping Ian\message.txt", mode="r")
    file2 = open("Small Projects\helping Ian\message2.txt", mode="r")

    # sets all text in text files to string
    line1 = file1.readlines()
    line2 = file2.readlines()

    # closes the text files variables
    file1.close()
    file2.close()

    # splits the text string variables on new lines into list
    for line in line1:
        my_list1.append(line)
    for line in line2:
        my_list2.append(line)

    # function to set table using first document with the two parameters
    set_primary_table(my_list1)
    #for key in reason_broke_file1:
    #    print(reason_broke_file1[key])

    # function to assign correct lbs broke to second document with only reason codes
    fileParser(my_list2)
    #for key in reason_broke_file2:
    #    print(reason_broke_file2[key])

    export_file = open("Small Projects\helping Ian\\finalReasons.txt", "w")

    for line in my_list2:
        does_code_have_broke = 0
        x_1 = line.strip()
        for key in reason_broke_file2:
            if key == x_1:
                export_file.write(key + " " + str(reason_broke_file2[key]) + " " + str(sum(reason_broke_file2[key])) + "\n")
                does_code_have_broke = 1
        if does_code_have_broke == 0:
            export_file.write(x_1 + " NA" + "\n")

    export_file.close()

main()