def produce_summary(): # function to print daily produce summary from files
    day_count = 1 # day to start count on
    file_count = 19 # file to start count on
    while file_count < 22 and day_count < 4: # while the file count is less than 22 and the day count is less than 4 do something
        the_file = open("um-deliveries-201405" + str(file_count) + ".txt") # open file that includes file_count variable
        file_count += 1 # increase variable counter by 1
        print("Day " + str(day_count)) # print day number
        day_count += 1 # increase variable counter by 1
        for line in the_file: # for each line in file
            line = line.rstrip() # remove white space from line
            words = line.split('|') # split the line by delimiter

            melon = words[0] # store words at index 0 in variable melon
            count = words[1] # store words at index 1 in variable count
            amount = words[2] # store words at index 2 in variable amount
            print(f"Delivered {count} {melon}s for total of ${amount}") # print summary line containing variables
    the_file.close() # close the file

produce_summary() # call function