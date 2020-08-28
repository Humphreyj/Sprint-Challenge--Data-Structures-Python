class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None#Either a BSTNode or none
        self.right: BSTNode = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else: 
                right_child = self.right
                right_child.insert(value)
        #Right Side
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                left_child = self.left
                left_child.insert(value)
    def contains(self, target):
        if target == self.value:
            return True

        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        else:
            if self.right is None:
                return False