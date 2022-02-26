#출석과제 : 연습문제 7-3
#학생번호와 이름이 2개의 리스트로 주어졌을때,
#학생번호를 입력하면 학생번호에 해당하는 이름을
#순차탐색으로 찾아 돌려주는 함수 만들기.
#해당하는 학생 번호가 없으면 물음표(?)를 return

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

entry_num = int(input("찾고 싶은 학생 번호를 입력하세요:")) #번호 입력 받기

def search_student(number, name, entry_num):
    n = len(number) #stu_no 리스트의 크기
    for i in range(0, n): #탐색
        if entry_num == number[i]: #입력 값과 탐색 값이 같을 때 
            return name[i] #이름 리턴
    return "?" #없을 때는 ? 리턴

print(search_student(stu_no, stu_name, entry_num))

#-----------------------------------------------------------------------------

#실습평가 과제 :  1~100사이의 숫자중에 무작위로  20개의 정수를 생성하여
#이 값들을 이진 탐색트리(Binary Search Tree) 형태로 저장하여 저장된 값들 출력하고,
#이진 탐색트리에 저장되어 있는 값들을
#중위순회(Inorder Traversal)방식으로 탐색하여 그 결과를 출력하기

#클래스로 구현

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
            result.extend(self.inorder_traversalNode(currentNode.leftChild))
        if (currentNode is not None):
            result.extend([currentNode.val])
        if (currentNode.rightChild is not None):
            result.extend(self.inorder_traversalNode(currentNode.rightChild))
        return result

num_list = [random.randint(1,100) for i in range(20)]
print(num_list)

bst = BinarySearchTree()
for x in num_list:
    bst.insert(x)

print(bst.inorder_traversal())

search_num = int(input("찾으려는 번호를 입력하세요:"))
print(bst.find(search_num))

#list로 구현



