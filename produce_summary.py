def produce_summary():
    day_count = 1
    file_count = 19
    while file_count < 22 and day_count < 4:
        the_file = open("um-deliveries-201405" + str(file_count) + ".txt")
        file_count += 1
        print("Day " + str(day_count))
        day_count += 1
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')

            melon = words[0]
            count = words[1]
            amount = words[2]
            print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

produce_summary()