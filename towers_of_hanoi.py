# Towers of Hanoi
# move disks from one tower to another
# larger disks cannot be on smaller ones

# Things to think about
# What would be a good datastructure to use for this?
# How does the problem change if there is only 1 disk? 2 disks? 3? 4?

source = ([4,3,2,1], "source")
target = ([], "target")
helper = ([], "helper")



def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n -1, source, target, helper)

        if source[0]:
            target[0].append(source[0].pop())
            print_status(source, helper, target)
 
        hanoi(n-1, helper, source, target)
 
def print_status(source, helper, target):
    print source, helper, target


hanoi(len(source[0]), source, helper, target)
