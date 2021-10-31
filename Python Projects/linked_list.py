class ListNode:
	def __init__(self, val=0, next=None):
	    self.val = val
	    self.next = next

def addTwoNumbers(l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node
        return tolist(toint(l1) + toint(l2))


def tolist(n):
	node = ListNode(n % 10)
	if n > 9:
	    node.next = tolist(n / 10)
	return node

y = tolist(547)
print(y.next.next.val)