# Data Project Practice
# Oleg Balitskiy

import statistics 

def output_stats(list): 
    print("Mean:   ", statistics.mean(list))
    print("Median: ", statistics.median(list))
    print("STD:    ", statistics.stdev(list))
    print()


# Data variables
spring = []
fall = []

# Read in the file
csv = "sample_grades.csv"

file = open(csv)
for line in file: 
    # print(line.rstrip()) # will take out whitespace at the end (r = right) of each line
    list = line.rstrip().split(",")
    # print(list)
    if list[1] == "Spring 2016": 
        spring.append(eval(list[2]))
    else: 
        fall.append(eval(list[2]))

# print("Sprint: ", spring)
# print("Fall:   ", fall)
file.close()

print("Fall 2016:")
output_stats(fall)
print("Spring 1016:")
output_stats(spring)
