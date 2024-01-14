### in the design of hasMap (or hashSet), we need single Link list and hashMap (or hashSet) datastructures:

# Define the calss ListNode
class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hashMap = [ListNode() for i in range(1000)]
    
    def hashIndex(self, key):
        return key % len(self.hashMap)

    def put(self, key: int, value: int) -> None:
        # check if the entry at the index hashIndex(key) 
        # exist in hashMap where this single linkedList 
        # elements reside 
        cur = self.hashMap[self.hashIndex(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        # the entry is new and need to be added to the 
        # linkedList
        cur.next = ListNode(key, value)
        
    def get(self, key: int) -> int:
        cur = self.hashMap[self.hashIndex(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
        
    def remove(self, key: int) -> None:
        cur = self.hashMap[self.hashIndex(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    ### Time complexity is most of the time O(1), Space O(n) ###

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)