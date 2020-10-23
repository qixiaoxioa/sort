class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.head = None
    def __repr__(self):
        return f"Node({self.data})"

def insertOrderlink(head:Node):
    dummy = Node(0)
    pre = dummy
    cur = head
    while cur:
        temp = cur.next
        while pre.next and pre.next.data < cur.data:
            pre = pre.next
        cur.next = pre.next
        pre.next = cur
        cur = temp
        pre = dummy
    return dummy.next
def printt(head):
    curr = head
    string = ""
    while curr:
        string += f"{curr}-->"
        curr = curr.next
    return string + "END"


if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(2)
    node3 = Node(5)
    node4 = Node(4)
    node5 = Node(8)
    node6 = Node(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = None
    print(printt(node1))
    print(printt(insertOrderlink(node1)))