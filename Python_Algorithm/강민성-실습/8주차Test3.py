
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def find(self, val):
        if (self.findNode(self.root, val) is False):
            return False
        else:
            return True

    def findNode(self, currentNode, val):
        if (currentNode is None):
            return False
        elif (val == currentNode.val):
            return currentNode
        elif (val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    def insert(self, val):
        if (self.root is None):
             self.setRoot(val)
        else:
             self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if (val <= currentNode.val):
            if (currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif (val > currentNode.val):
            if (currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)
    def inorder_traversal(self):
        return self.inorder_traversalNode(self.root)

    def inorder_traversalNode(self, currentNode):
        result = []
        if (currentNode.leftChild is not None):
            result.extend(self.traverseNode(currentNode.leftChild))
        if (currentNode is not None):
            result.extend([currentNode.val])
        if (currentNode.rightChild is not None):
            result.extend(self.traverseNode(currentNode.rightChild))
        return result

num_list = [random.randint(1,100) for i in range(20)]
print(num_list)

bst = BinarySearchTree()
for x in num_list:
    bst.insert(x)

print(bst.inorder_traversal())

search_num = int(input("찾으려는 번호를 입력하세요:"))
print(bst.find(search_num))
