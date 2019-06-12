"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # create new node...
    new_node = ListNode(value)

    # if list is currently empty...
    if self.head is None:
      # set head and tail to new node
      self.head = new_node
      self.tail = new_node
    else:
      # current head's previous value should be set to the new node
      self.head.prev = new_node
      # new node next value should be set to existing head.
      new_node.next = self.head
      # current head should be replaced
      self.head = new_node

  def remove_from_head(self):
    # store reference to head node
    current_head = self.head
    # set the next node as the head...
    self.head = current_head.next
    # prev value for new head should be none
    self.head.prev = None
    # return the removed head value
    return current_head

  def add_to_tail(self, value):
    # create new node...
    new_node = ListNode(value)

    # if list is currently empty...
    if self.tail is None:
      # set head and tail to new node
      self.head = new_node
      self.tail = new_node
    else:
      # current tail's next value should be set to the new node
      self.tail.next = new_node
      # new node prev value should be set to existing tail.
      new_node.prev = self.tail
      # current tail should be replaced
      self.tail = new_node

  def remove_from_tail(self):
    # store reference to tail node
    current_tail = self.tail
    # set the prev node as the tail...
    self.tail = current_tail.prev
    # next value for new tail should be none
    self.tail.next = None
    # return the removed tail value
    return current_tail

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    node.delete()

  def get_max(self):
    pass
