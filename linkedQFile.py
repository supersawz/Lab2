# by Johannes Rosing and Oscar Ekehed

import array as arr

class Node:
    def __init__(self, datavalue):
        # set datavalue in the allocated node and return it
        self.datavalue = datavalue   # can refer to value of chosen type
        self.next = None   # points to next object, initializes to None because
                           # we want our rear to always point to None
 
 
class LinkedQ:

    def __init__(self):
        # front is first item of queue,
        # rear_rear is rear_rear item of queue
        self._array = arr.array('i', [])
        self._front = None # initalized to None because we start with an empty Queue
        self._rear = None
        self._size = 0

    def __len__(self):
        # returns the updated size of the array
        return self._size

    def isEmpty(self):
        # checking wether or not front and rear BOTH are empty
        # returns True if empty, False otherwise
        return self._front == None and self._rear == None

    def enqueue(self, datavalue):   
        # method for adding item to queue
        # ADDS new node after rear,
        # MOVES rear to next node  
        
        node = Node(datavalue)  # our chosen node
        print('\nInserting in Queue: ', datavalue)
 
        if self._rear == None:
            # IF queue is empty
            # initialize both front and rear
            # so that both our pointers point to the chosen node.
            self._front = node
            self._rear = node
        else:
            # update rear
            self._rear.next = node # new node is added next to our rear
            self._rear = node   # we move our rear to the next node

        self._array.append(datavalue) # adding value to array
        self._size += 1  # increasing size of array by 1
 
   
    def dequeue(self): 
        # method for removing item from queue
        # removes front node, and moves 
        # front to next node 
       
        if self._front == None:
            # if front is None, Queue is empty
            # and dequeue cannot be performed
            print('\nQueue is empty')

        tmp = self._front   # temporarily equaling "tmp" with first element in queue
        print('\nPopping first element from queue...')
        
        self._front = self._front.next   # we make the front-pointer point to the element
                                         # AFTER our first element in queue.
        self._array.pop(0)  # then we simply pop our first element in queue.
 
        # if the list becomes empty
        if self._front == None:
            self._rear = None
 
        self._size -= 1  
 
        return tmp.datavalue  # return the removed item
 
    def first(self):
        # method to return the first element in a queue
        if self.first:   # check for an empty queue
            return self._front.datavalue



 