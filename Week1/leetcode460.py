class Node:
    def __init__(self, key=0, value=0, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeLast(self):
        if self.size == 0:
            return None
        last = self.tail.prev
        self.remove(last)
        return last

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        
        self.key_map = {}
        self.freq_map = {}

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        node = self.key_map[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._update(node)
        else:
            if self.size >= self.capacity:
                min_freq_list = self.freq_map[self.min_freq]
                removed_node = min_freq_list.removeLast()
                del self.key_map[removed_node.key]
                self.size -= 1
                
                if min_freq_list.size == 0:
                    del self.freq_map[self.min_freq]
            
            node = Node(key, value)
            self.key_map[key] = node
            
            self._addToFreqList(node, 1)
            
            self.size += 1
            self.min_freq = 1

    def _update(self, node):
        old_freq = node.freq
        freq_list = self.freq_map[old_freq]
        freq_list.remove(node)
        
        if freq_list.size == 0:
            del self.freq_map[old_freq]
            if old_freq == self.min_freq:
                self.min_freq += 1
        
        node.freq += 1
        self._addToFreqList(node, node.freq)

    def _addToFreqList(self, node, freq):
        if freq not in self.freq_map:
            self.freq_map[freq] = DLinkedList()
        self.freq_map[freq].add(node)