from LinkedBinaryTree import LinkedBinaryTree
def min_and_max(bin_tree):
    if (bin_tree == None):
        raise Exception
    return subtree_min_and_max(bin_tree.root)
    
        
def subtree_min_and_max(root):
    if ( root.right and root.left == None): #base case
        min_max = (root.data,root.data)
        print(min_max)
        return min_max
    val_left = ()
    val_right = ()
    if (root.left !=None):
        val_left = subtree_min_and_max(root.left)
    if (root.right !=None):
        val_right = subtree_min_and_max(root.left)
    root_val = (root.data,root.data)

    minim = root.data
    maxim = root.data

    if len(val_left) >0:
        if val_left[0] < minim:
            minim = val_left[0]
            
        if val_left[1] > maxim:
            maxim = val_left[1]
            
    if len(val_right) >0:
        if val_right[0] < minim:
            minim = val_right[0]
            
        if val_right[1] > maxim:
            maxim = val_right[1]

    min_max = (minim, maxim)

    return min_max
            
            
def main():
    a = LinkedBinaryTree().Node(5,None,None)
    b = LinkedBinaryTree().Node(1,None,None)
    c = LinkedBinaryTree().Node(8,None,None)
    d = LinkedBinaryTree().Node(4,None,None)
    e = LinkedBinaryTree().Node(9,a,b)
    f = LinkedBinaryTree().Node(2,e,None)
    g = LinkedBinaryTree().Node(7,c,d)
    h = LinkedBinaryTree().Node(3,f,g)
    bin_tree = LinkedBinaryTree(h)
    i = min_and_max(bin_tree) #pass in the root node for the whole tree
    print(i)
    
main()
    
        
