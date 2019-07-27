class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.queue = [0] * k
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return True
            
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.queue[self.front] if self.size != 0 else -1
        
    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.queue[self.rear] if self.size != 0 else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.max_size == self.size:
            return True
        else:
            return False
    
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
