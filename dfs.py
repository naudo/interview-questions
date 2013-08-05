# Depth First Search
# Implement recursive depth first search to find a particular node given the data
# using a binary tree
# Step 1
# Define Depth first, search as far in a direction as possible before going back


# Things to thing about
# what if what you're looking for doesn't exist
# what would you do if the data was structured.




class BinaryTree:
    def __init__(data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def dfs(node, val):
    if node != none:
        if node.data == val
            return node.data
        dfs(node.left)
        dfs(node.right)

    #reached the end without finding what we were looking for
    return 0

