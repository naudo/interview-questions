# Given a list of lists, find the largest average and list

# things to think about
# what if there are 2 lists with the same average
# what if the length of the list is 0?

#questions to ask
# can I assume the lists are sorted?

l = [ [1,2,3], [2,3,4], [6,99,101], [3,64,2] ]


def find_largest_avg(l):
    largest = []
    for lst in l:
        if avg(largest) < avg(lst):
            largest = lst

    return largest

def avg(l):
    if len(l) > 0: return sum(l) / len(l)
    
    return 0


print find_largest_avg(l)
