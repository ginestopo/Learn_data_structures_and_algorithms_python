def locate_card(cards, query):
    lo, hi = 0, len(cards)-1

    while lo<=hi:
        mid = (lo+hi)//2 #floor division

        print("mid",mid,"lo",lo,"hi",hi)

        if cards[mid] == query:
            return mid
        elif(query > cards[mid]):
            hi = mid-1
        elif(query < cards[mid]):
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
