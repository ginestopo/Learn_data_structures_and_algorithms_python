# Following this course:
# https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-1-binary-search-linked-lists-and-complexity

# The complexity is: log(N) because...
# Initial length - N

# Iteration 1 - N/2
#
# Iteration 2 - N/4 i.e. N/2^2
#
# Iteration 3 - N/8 i.e. N/2^3
#
# ...
#
# Iteration k - N/2^k
#
# Since the final length of the array is 1, we can find the
#
# N/2^k = 1
#
# Rearranging the terms, we get
#
# N = 2^k
#
# Taking the logarithm
#
# k = log N
#
# Where log refers to log to the base 2. Therefore, our algorithm has the time complexity O(log N)

#Auxiliary function in case the query is repeated in the array (we want the first appearance)
def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


# Given N number of cards, we are asked to guess the position of the card
# which contains the number "query". We must guess it by accessing the minimum
# number of cards possible (not using brute force)

def locate_card(cards, query):
    lo, hi = 0, len(cards)-1

    while lo<=hi:
        mid = (lo+hi)//2 #floor division

        #print("mid",mid,"lo",lo,"hi",hi)
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1

    return -1


#__________________TEST CASES___________________

tests = []

tests.append({
    "input" : {
        "cards" : [13, 11, 10, 7, 4, 3, 1, 0],
        "query" : 7
    },
    "output" : 3
})

tests.append({
    "input" : {
        "cards" : [4, 2, 1, -1],
        "query" : 4
    },
    "output" : 0
})

tests.append({
    "input" : {
        "cards" : [3, -1, -9, -127],
        "query" : -127
    },
    "output" : 3
})

tests.append({
    "input" : {
        "cards" : [6],
        "query" : 6
    },
    "output" : 0
})

#not contains query
tests.append({
    "input" : {
        "cards" : [9, 7, 5, 2, -9],
        "query" : 4
    },
    "output" : -1
})

#card is empty
tests.append({
    "input" : {
        "cards" : [],
        "query" : 7
    },
    "output" : -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

for x in tests:
    print(locate_card(**x["input"]) == x['output'])
