# head={
#     'value':74,
#     'next':{
#         'value':34,
#         'next':{
#             'value':23,
#             'next':None
#         }
#     }
#
# }
#
# def printlinklist(head):
#
#     while head is not None:
#         print(head['value'],end='->')
#         head=head['next']
#     print('none')
#
# printlinklist(head)

# ===============================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linklist:
    def __init__(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next
        print("None")

    def append(self, value):
        newnode = Node(value)
        if self.length == 0:
            return None
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1
        return True

    def prepend(self, value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        pre = self.head
        temp = self.head

        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp

    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None

        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return print("index out of range")
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return print("index out of range")
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.get(index - 1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return print("index out of range")
        if index == 0:
            return self.popfirst()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length = -1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        befor = None

        for i in range(self.length):
            after = temp.next
            temp.next = befor
            befor = temp
            temp = after


linklist = Linklist(7)
linklist.append(66)
linklist.append(6)
linklist.append(44)
linklist.prepend(3)
linklist.printlist()
linklist.pop()
linklist.popfirst()
print(linklist.get(1).value)
linklist.set(2, 6)
linklist.printlist()
linklist.insert(1, 1)
linklist.remove(9)
linklist.reverse()
linklist.printlist()



