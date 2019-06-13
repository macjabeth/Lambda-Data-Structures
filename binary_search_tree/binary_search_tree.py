class BinarySearchTree:
  def __init__(self, value):
    print(f'creating bst: {value}')
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # check if the new node's value is less than our current node's value
    if value < self.value:
      # if there's no left child here already, place the new node here
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        # otherwise, repeat the process!
        self.left.insert(value)
    # check if the new node's value is greater than or equal to our current node's value
    elif value >= self.value:
      # if there's no right child here already, place the new node here
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        # otherwise, repeat the process!
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif self.left and target < self.value:
      return self.left.contains(target)
    elif self.right and target > self.value:
      return self.right.contains(target)
    return False

  def get_max(self):
    node = self
    current_max = node.value
    while node.right:
      node = node.right
      if node.value > current_max:
        current_max = node.value
    return node.value

  def for_each(self, cb):
    cb(self.value)
    if self.right:
      print(f'right: calling cb on {self.right.value}')
      cb(self.right.value)
      self.right.for_each(cb)
    if self.left:
      print(f'left: calling cb on {self.left.value}')
      cb(self.left.value)
      self.left.for_each(cb)
