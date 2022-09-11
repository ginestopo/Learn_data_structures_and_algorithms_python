#------------------------------------------------------------------
#----------------------QUICK SORT ALGO  O(N log(N)) ---------------
#------------------------------------------------------------------
#------------------------by Ginés Díaz-----------------------------

""""
Instructions (https://www.youtube.com/watch?v=kFeXwkgnQ9U&ab_channel=DerrickSherrill)

0 9 3 8 2 7 5

Pivot will be 5
We arrange the numbers on the left if they are lower and right if greater

0 3 2 [5] 9 8 7

and apply recursivity on the left and right side


"""

from cgi import test


def quicksort(sequence):
    length = len(sequence)

    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()  


    items_greater = []  
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)



#------------------------------------------------------------------
#--------------------------TESTING CASES---------------------------
#------------------------------------------------------------------

tests = []

tests.append({
    'sequence':[2,4,5,1,9,8],
    'output' : [1,2,4,5,8,9]
})

tests.append({
    'sequence':[2,23,41,5,64,100,0],
    'output':[0,2,5,23,41,64,100]
}
)


for x in tests:
    print(quicksort(x['sequence'])==x['output'])
    print(quicksort(x['sequence']))

    