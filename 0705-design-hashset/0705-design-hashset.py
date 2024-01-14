
### Need to use a linked list for this hashSet class ###
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.hashSet = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.hashSet[key % len(self.hashSet)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.hashSet[key % len(self.hashSet)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.hashSet[key % len(self.hashSet)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
    ### Time complexity in most of the time is O(1). Space is O(n)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)