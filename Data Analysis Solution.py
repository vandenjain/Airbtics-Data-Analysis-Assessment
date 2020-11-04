'''
PROBLEM STATEMENT - 1. Write a program which reads comma-separated floating-point numbers in a single line from stdin
and prints the filtered data to stdout in the same format.

APPROACH - input is divided into 5 intervals of size 0.2. The intervals are [0, 0.2), [0.2, 0.4), ... [0.8, 1.0)

Instructions - Run the program and it will ask for input array, Give an array as input and it will generate the expected
output.
'''
#SOLUTION -
def Floating_points(arr, interval1, interval2 , interval3, interval4, interval5):
    for i in range(len(arr)):
        if arr[i] >= float(0.0) and arr[i] < float(0.2):        #interval [0.0,0.2)
            interval1.append(arr[i])
        if arr[i] >= float(0.2) and arr[i] < float(0.4):        #interval [0.2,0.4)
            interval2.append(arr[i])
        if arr[i] >= float(0.4) and arr[i] < float(0.6):        #interval [0.4,0.6)
            interval3.append(arr[i])
        if arr[i] >= float(0.6) and arr[i] < float(0.8):        #interval [0.6,0.8)
            interval4.append(arr[i])
        if arr[i] >= float(0.8) and arr[i] < float(1.0):        #interval [0.8,1.0)
            interval5.append(arr[i])

    if len(interval1) == len(interval2) and len(interval2) == len(interval3) and len(interval3) == len(interval4) and len(interval4) == len(interval5):  #if lenght of all the intervals are same, then do nothing.
        return True
    else:
        return False

arr = list(map(float, input().split(",")))  #input array
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
answer = Floating_points(arr, l1, l2, l3, l4, l5)

A,B,C,D,E = len(l1), len(l2), len(l3), len(l4), len(l5)


if answer:
    res = l1 + l2 +l3 +l4 +l5
    for i in range(len(res)-1):
        print(res[i], end=',')
    print(res[len(res)-1])

else:
    if (A != 0 and B !=0 and C != 0 and D !=0 and E != 0):
        min_lenght_of_an_interval = min(A,B,C,D,E)
        for i in range(min_lenght_of_an_interval):
            print(l1[i], end=',')
        for i in range(min_lenght_of_an_interval):
            print(l2[i], end=',')
        for i in range(min_lenght_of_an_interval):
            print(l3[i], end=',')
        for i in range(min_lenght_of_an_interval):
            print(l4[i], end=',')
        for i in range(min_lenght_of_an_interval-1):
            print(l5[i], end=',')
        print(l5[min_lenght_of_an_interval-1])

    else:
        print("None")
'''
PROBLEM STATEMENT 2 - Provide one automated test case for your program:

when we give '0.1, 0.15, 0.25, 0.39, 0.51, 0.45, 0.63, 0.71, 0.85, 0.99' as an input, 
output received is 0.1,0.15,0.25,0.39,0.51,0.45,0.63,0.71,0.85,0.99

when we give '0.1, 0.15, 0.25, 0.39, 0.51, 0.45, 0.63, 0.71, 0.85' as an input,
output received is 0.1,0.25,0.51,0.63,0.85

when we give '0.1, 0.15, 0.25, 0.39, 0.51, 0.45, 0.63, 0.71' as an input,
output received is None.
'''