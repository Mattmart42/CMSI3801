"""String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string a a b c c c c c a a a would become a 2 b l c 5 a 3 , If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z)."""

def compress(string: str) -> str:
    res = ""
    letters = list()
    nums = list()
    letter = 0

    for i in range(len(string)):
        letter += 1
        if i+1 < len(string) and string[i] == string[i+1]: continue
        else:
            letters.append(string[i])
            nums.append(str(letter))
            letter = 0

    for i in range(len(letters)):
        res += letters[i]
        res += nums[i]
    
    return res

print("-----------------------------------")
print("aabcccccaaa")
print(compress("aabcccccaaa"))
print("-----------------------------------")

"""Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node."""

class Node:
    def __init__(self, next, data):
        self.next = next
        self.data = data
    
    def append(self, data):
        child = Node(None, data)
        current = self
        while current.next != None:
            current = current.next
        current.next = child

    def remove(self, data):
        current = self
        previous = None
        while current.data != data and current.next != None:
            if current.next.data == data:
                previous = current
                current = current.next
                break
            current = current.next
        previous.next = current.next
        current = None

    def __str__(self):
        res = ""
        current = self
        while current.next != None:
            res += str(current.data)
            current = current.next
        res += str(current.data)
        return res
    
testNode = Node(None, "A")
testNode.append("B")
testNode.append("C")
print(testNode)
testNode.remove("B")
print(testNode)
print("-----------------------------------")

"""Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: ( 7 - > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295,
Output:9 -> 1 -> 2,Thatis,912."""

def sum(node, other):
    current = node
    node_str = ""
    while current.next != None:
        node_str += str(current.data)
        current = current.next
    node_str += str(current.data)
    node_str = node_str[::-1]

    current = other
    other_str = ""
    while current.next != None:
        other_str += str(current.data)
        current = current.next
    other_str += str(current.data)
    other_str = other_str[::-1]
    res = int(node_str) + int(other_str)
    
    print(node_str,"+",other_str,"=",res)

testNode1 = Node(None, 7)
testNode1.append(1)
testNode1.append(6)
print(testNode1)
testNode2 = Node(None, 5)
testNode2.append(9)
testNode2.append(2)
print(testNode2)
sum(testNode1, testNode2)
print("-----------------------------------")

"""Stack Min: How would you design a stack which, in addition to p u s h and pop, has a function m i n
which returns the minimum eiement? Push, p o p and m i n should ail operate in 0 ( 1 ) time."""

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if not len(self.data) == 0:
            return self.data.pop()
        
    def min(self):
        if not len(self.data) == 0:
            return min(self.data)
    
stack = Stack()
stack.push(78)
stack.push(6)
stack.push(90)
stack.push(-13)
print(stack.min())
print("-----------------------------------")