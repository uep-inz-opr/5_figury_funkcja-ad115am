import math
valid_input=True
def calculate_area(*args):

    args = args[0]
    area = 0
    if(len(args)) == 1:
        area = math.pi*(args[0]**2)
    if (len(args)) == 2:
        area = args[0]*args[1]
    if (len(args)) == 3:
        p = sum(args)/2
        area = math.sqrt(p*(p-args[0])*(p-args[1])*(p-args[2]))
    if (len(args)) >= 4:
        global valid_input
        valid_input=False

    return area
def calculate_sum_of_areas():
    sum = 0
    error="Błąd: można podać maksymalnie 3 liczby"
    number_of_figures = int(input())
    for figure in range (number_of_figures):
        numbers=list(map(float,(input().split())))
        sum += calculate_area(numbers)
        if(valid_input==False):
            break


    if(valid_input):
        print(str(round(sum, 2)))
    else:
        print(error)
calculate_sum_of_areas()
