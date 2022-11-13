#------------------------------------------------------------------
#----------------------BUBBLESORT ALGO  O(N2) ---------------
#------------------------------------------------------------------
#------------------------by Ginés Díaz-----------------------------

""""
Instructions (https://www.youtube.com/watch?v=kFeXwkgnQ9U&ab_channel=DerrickSherrill)

0 9 3 8 2 7 5

We swap elements by pairs starting from the left.

1st iteration --> [0 9] 3 8 2 7 5
2nd iteration --> 0 [3 9] 8 2 7 5
3rd iteration --> 0 3 [8 9] 2 7 5
.
.
.

"""


def bubblesort(sequence):

    for j in range(len(sequence)-1):
        for i in range(len(sequence)-1):
            if(sequence[i+1]<sequence[i]):
                #swap them
                sequence[i],sequence[i+1] = sequence[i+1],sequence[i]
    
    return sequence




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


for x in tests:
    print(bubblesort(x['sequence'])==x['output'])
    print(bubblesort(x['sequence']))
