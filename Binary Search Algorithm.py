# Binary Search Algorithm
# a func that takes a list and target parameter
# multiple variables: middle, start, end, steps
# recursion or while loop
# increase steps each time a split is done
# conditions to track target position

def bsf(list, element):
    middle=0
    start=0
    end=len(list)
    steps=0

    while(start<=end):
        print("Step",steps, ":", str(list[start:end+1]))

        steps=steps+1
        middle=(start+end) // 2

        if element == list[middle]:
            return middle
        if element<list[middle]:
            end=middle-1

        else:
            start=middle+1
        
    return -1

my_list=[1,4,6,9,12,15,18,19,21,24,38,47,89]
target= 21

bsf(my_list, target)