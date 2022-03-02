class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    if not root:
        return
    dit = {}
    q = []
    q.append([root,0])
    while q:
        p = q[0]
        n = p[0]
        val = p[1]
        q.pop(0)
        
        if val not in dit:
            dit[val] = n
        if n.right != None:
            q.append([n.right, val+1])
        if n.left != None:
            q.append([n.left, val-1])
    for i in sorted(dit.keys()):
        print(dit[i], end=' ')



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
