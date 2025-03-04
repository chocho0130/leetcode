class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1  # counter
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop(self, node=None):
        if self.size == 0:
            return None
        if not node:
            node = self.head.next
        self.remove(node)
        return node

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.minfreq = 0  
        self.key_to_node = {}  # key -> Node
        self.freq_to_dll = {}  # freq -> DoublyLinkedList

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity <= 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update(node)
        else:
            if self.size == self.capacity:
                # 淘汰最少使用的節點，從最低頻率的 DLL 中移除最舊的節點
                dll = self.freq_to_dll[self.minfreq]
                node_to_remove = dll.pop()
                del self.key_to_node[node_to_remove.key]
                self.size -= 1
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            if 1 not in self.freq_to_dll:
                self.freq_to_dll[1] = DoublyLinkedList()
            self.freq_to_dll[1].append(new_node)
            self.minfreq = 1  # 新加入的節點頻率為 1，所以最小頻率更新為 1
            self.size += 1

    def _update(self, node):
        freq = node.freq
        dll = self.freq_to_dll[freq]
        dll.remove(node)
        if dll.size == 0:
            del self.freq_to_dll[freq]
            if self.minfreq == freq:
                self.minfreq += 1
        node.freq += 1
        if node.freq not in self.freq_to_dll:
            self.freq_to_dll[node.freq] = DoublyLinkedList()
        self.freq_to_dll[node.freq].append(node)
