#------------------------------------------------------------------
#----------------------BUBBLESORT ALGO  O(N2) ---------------
#------------------------------------------------------------------
#------------------------by Ginés Díaz-----------------------------

""""
Instructions (https://www.simplilearn.com/tutorials/data-structure-tutorial/bubble-sort-algorithm)

0 9 3 8 2 7 5

We swap elements by pairs starting from the left.

1st iteration --> [0 9] 3 8 2 7 5
2nd iteration --> 0 [3 9] 8 2 7 5
3rd iteration --> 0 3 [8 9] 2 7 5
.
.
.

We have to repeat this action N-1 because N is the length of the array,
hence N-1 is the number of times a comparison can occur.

"""


def bubblesort(sequence):

    for j in range(len(sequence)-1):
        for i in range(len(sequence)-1):
            if(sequence[i+1]<sequence[i]):
                #swap them
                sequence[i],sequence[i+1] = sequence[i+1],sequence[i]
    
    return sequence




            # TEST CASES



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

tests.append({
    'sequence':[1,3,4,6,9,8],
    'output':[1,3,4,6,8,9]
}
)

tests.append({
    'sequence':[1,-3,4,6,-9,8],
    'output':[-9,-3,1,4,6,8]
}
)

tests.append({
    'sequence':[],
    'output':[]
}
)

tests.append({
    'sequence':[1],
    'output':[1]
}
)


for x in tests:
    print(bubblesort(x['sequence'])==x['output'])
    print(bubblesort(x['sequence']))
