class Node:11
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.data)

    def print_tree(root, val="data", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, "data")
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle
    
            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, "left"))
                s = '%s' % getattr(root, "data")
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
    
            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, "right"))
                s = '%s' % getattr(root, "data")
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
    
            # Two children.
            left, n, p, x = display(getattr(root, "left"))
            right, m, q, y = display(getattr(root, "right"))
            s = '%s' % getattr(root, "data")
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
    
        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)

class BinarySearchTree:
    def __init__(self, root=None):
        self.root=root
        self.str=""
    def addNode(self, value=None):
        node=Node(value)
        par=None
        if self.root==None:
            print("Rood added ->",value)
            self.root=node
        else:
            curr=self.root
            while curr:
                
                if curr.data==value:
                    break
                elif curr.data>value:
                    par=curr
                    curr=curr.left
                else:
                    par=curr
                    curr=curr.right
            if value>par.data:
                print("Adding in right of ",par.data," new node ", value)
                par.right=node
            else:
                print("Adding in left of ",par.data," new node ", value)
                par.left=node
    def delNode(self, value=None):
        curr=self.root
        par=None
        
        while curr:
            if curr.data==value:
                if (curr.left!= None) and (curr.right!=None):
                    self.twochild(par,curr)
                    return
                else:    
                    self.onechild(par,curr)
                    return
            elif value>curr.data:
                par=curr
                curr=curr.right
            else:
                par=curr
                curr=curr.left

    def onechild(self, par=None,ptr=None):
        if ptr.left!=None:
            child=ptr.left
        elif ptr.right!=None:
            child=ptr.right
        else:
            child=None

        if ptr==par.left:
            par.left=child
        else:
            par.right=child
       
    def twochild(self, par=None,ptr=None):
        parsuc=ptr
        suc=ptr.right
        while suc.link:
            parsuc=suc
            suc=suc.link

        onechild(parsuc,suc)  

        suc.left=ptr.left
        suc.right=ptr.right
        if ptr==par.left:
            par.left=suc
        else:
            par.right=suc
            
                
    def InTrav(self, ptr=None):
        curr=ptr
        if (curr):
            self.InTrav(curr.left)
            print(curr.data, end = " ")
            self.InTrav(curr.right)
        
    def PreTrav(self, ptr=None):
        curr=ptr
        if (curr):
            print(curr.data, end = " ")
            self.InTrav(curr.left)
            self.InTrav(curr.right)   
        
    def PostTrav(self, ptr=None):
        curr=ptr
        if (curr):
            self.InTrav(curr.left)
            self.InTrav(curr.right)
            print(curr.data, end = " ")

    def display(self):
        self.root.print_tree(self.root)


bst= BinarySearchTree()
print("Tree traversal code:")
bst.addNode(int(input("Enter the root: ")))
bst.addNode
while(True):
    print("\nChoose to insert or remove value(Please don't insert or remove the root value: ")
    print("1: Add values")
    print("2: Remove value")
    print("3: Exit the program")
    choice = int(input("Enter your choice: "))
    if(choice == 3):
        print("\nThank You!!!")
        break
    elif(choice == 1):
        inval=str(input("Enter the values to insert: "))
        inarr=inval.split(" ")
        for i in range(len(inarr)):
            bst.addNode(int(inarr[i]))
        print("\nAfter insertion:")
        print("\nTree:")
        bst.display()
        
        print("\nTraversal in Inorder")
        bst.InTrav(bst.root)
        print("\n")
        print("\nTraversal in Preorder")
        bst.PreTrav(bst.root) 
        print("\n")
        print("\nTraversal in Postorder")
        bst.PostTrav(bst.root)
        print("\n")
        
    elif(choice == 2):
        inval=int(input("Enter the value to be deleted: "))
        bst.delNode(inval)
        print("\nAfter deletion:")
        print("\nTree:")
        bst.display()
        bst.PostTrav(bst.root)
        print("\nTraversal in Inorder")
        bst.InTrav(bst.root)
        print("Traversal in Preorder")
        bst.PreTrav(bst.root)            
        print("Traversal in Postorder")
        bst.PostTrav(bst.root)
    else: 
        print("\nSorry! Wrong choice!!")
        continue
        










