# Given we have 9 balls, find the heaviest one on a scale
# do it in only 2 tries (all the rest are tthe same weight)
# assume the scale only has 2 sides

#Things to ponder
# List comphresions
# how to store the data
ball_bin = []

class Ball:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

    def __repr__(self):
        return "id: %d, weight %d" % (self.id, self.weight)


for i in range(1, 9):
    ball_bin.append(Ball(i,1))

#now let's add the heavy one
ball_bin.append(Ball(9, 2))

def sum_of_weight(lst):
    return sum(i.weight for i in lst)

def find_heavy(ball_list, attempts):
    list_size = len(ball_list)
    
    if list_size == 1:
        print attempts
        return ball_list

    attempts = attempts + 1

    group_size = list_size / 3 

    group_a = ball_list[:group_size]
    group_b = ball_list[group_size:group_size * 2]
    group_c = ball_list[group_size * 2:]

    if sum_of_weight(group_a) == sum_of_weight(group_b):
        return find_heavy(group_c, attempts)
    elif sum_of_weight(group_a) > sum_of_weight(group_b):
        return find_heavy(group_a, attempts)
    elif sum_of_weight(group_b) > sum_of_weight(group_a):
        return find_heavy(group_b, attempts)



results =   find_heavy(ball_bin, 0)

print "Found the odd ball"
print results
