# Stats - Modules & Functions - Griffin Hart - CSD110
# The following program will ask the user for 10 integer values, store them in a list, and call them to functions.
# The following functions are required: getAverage(data), getMin(data), getBelowAvgCount(data)

import funcbundle

def main():
    userList = []
    for i in range(0, 10):
        userInput = int(input("Please enter an integer value: "))
        userList.append(userInput)
    average = funcbundle.getAverage(userList)
    lowest = funcbundle.getMin(userList)
    belowAvgCount = funcbundle.getBelowAvgCount(userList, average)

    print(f'The average value from your list was {average}.')
    print(f'The lowest value from your list was {lowest}.')
    print(f'You had {belowAvgCount} values that were below the average.')


main()