# print("Enter day of week: ")


# while True:
#     day = input()

#     print("Transport: ")
#     exp = int(input())
#     print("Food: ")
#     exp = int(input())

#     print(day)
#     exp1_list = ["Transport: ", exp, "Food: ", exp]
#     print(exp1_list)

    

#     print("Expanses of the day 1: ", sum1)

# day = week[0]

# week = [['Mon', [['Transport', 2000]]], ['Tue', [['Food', 500], ['Charity', 1000]]], ['Wed', [['Birthday Gift', 10000], ['Charity', 1000], ['Transport', 200]]], ['Thu', []], ['Fri', []], ['Sat', []], ['Sun', []]]
#         [             day            ]
#          day[0] [       day[1]      ]
#                 [      expense      ]
#                  expense[0]expense[1]


week = [
    ["Mon", [
        ['Transport', 2000]
    ]],
    ["Tue", [
        ['Food', 500],
        ['Charity', 1000]
    ]],
    ["Wed", [
        ['Birthday Gift', 10000],
        ['Charity', 1000]
    ]],
    ["Thu", []],
    ["Fri", []],
    ["Sat", []],
    ["Sun", []]
]

def addExp(dayName, expName, expCost):
    for day in week:
        if(day[0] == dayName):
            isChanged = False
            for expense in day[1]:
                if(expense[0] == expName):
                    expense[1]+=expCost
                    isChanged = True
                    break
            if(isChanged == False):
                day[1].insert(len(day[1]), [expName, expCost])
            print("Expense added")
    print("\n")

def showDayExp(dayName):
    for day in week:
        if(day[0] == dayName):
            print("Day: ", day[0])
            for expense in day[1]:
                print(expense[0], ": ", expense[1])
    print("\n")

def showWeekDaySum():
    for day in week:
        sum = 0
        print("Day: ", day[0])
        for expense in day[1]:
            sum+=expense[1]
        print("Total expenses: ", sum)
    print("\n")
    
def showWeekSum():
    print("Week Outlay Summary")
    sum = []
    for day in week:
        for expense in day[1]:
            isChanged = False
            for item in sum:
                if(item[0] == expense[0]):
                    item[1]+=expense[1]
                    isChanged = True
                    break
            if(isChanged == False):
                sum.insert(len(sum), expense)
    for item in sum:
        print(item[0], ": ", item[1])
    print("\n")

def total():
    sum = 0
    for day in week:
        for expense in day[1]:
            sum+=expense[1]
    print("Total expenses: ", sum)
    print("\n")
    

addExp("Wed", "Transport", 200)
addExp("Fri", "Housekeeping", 2100)
showWeekSum()
showDayExp("Wed")
showWeekDaySum()
total()
