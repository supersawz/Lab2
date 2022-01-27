# By Johannes Rosing and Oscar Ekehed

import array as arr

class ArrayQ:

    def __init__(self):
        self._array = arr.array('i', []) # choosing to work with integers
        self._size = 0 # the size of the array
        self._front = 0 
        
    def __len__(self):
        # returns the updated size of the array
        return self._size
    
    def isEmpty(self):
        # checks wether or not array is empty
        return self._size == 0
    
    def enqueue(self, data):
        # adds a chosen element to the array
        print('\nInserting in Queue: ', data)
        self._array.append(data) # adding a new element to the rear of queue
        self._size += 1   # increasing size of queue by one

    def dequeue(self):
        if self.isEmpty():
            # if empty - nothing happens
            print('\nQueue is empty.')
        else:
            # pops the FIRST element in the array, and returns that value
            print('\nRemoving first element from Queue and adding to deck...')
            value = self._array.pop(self._front)
            self._size -= 1
            return value

    def delete(self, data):
        # optional function that handles removal
        # of a certain element, without storing
        # any data
        if self.isEmpty():
            print('\nQueue is empty.')
        else:
            print('\nRemoving the first occurence of the value: ', data)
            self._array.remove(data)
            self._size -= 1

    def first(self):
        # if array not empty, method finds and 
        # returns the first element in array
        if self.isEmpty():
            print('\nQueue is empty.')
        return self._array[self._front]

