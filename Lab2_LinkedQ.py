# By Johannes Rosing and Oscar Ekehed

from linkedQFile import LinkedQ # importing neccessary Array-Queue Class
import array as arr

# The correct starting-order for the cards are: 7 1 12 2 8 3 11 4 9 5 13 6 10 
# 1 represents an ace, 11 a knight, 12 a queen, and 13 a king

a = LinkedQ()
deck = arr.array('i', []) # creates an empty deck which will store output

# Queue elements in correct order

a.enqueue(7)
a.enqueue(1)
a.enqueue(12)
a.enqueue(2)
a.enqueue(8)
a.enqueue(3)
a.enqueue(11)
a.enqueue(4)
a.enqueue(9)
a.enqueue(5)
a.enqueue(13)
a.enqueue(6)
a.enqueue(10)

def transfer_cards():
    # function that handles the 
    # transfering of the cards

    while a._size > 0:
        # while size of the array is
        # LARGER than zero...
        if a._size != 1:
            print('\nQueue: ', a._array)
            a.enqueue(a.first()) # putting the first card in deck last
            a.dequeue() # removing first card so that we don't have duplets
            print('\nQueue: ', a._array)
            deck.append(a.dequeue()) # popping the front card and
                                 # storing in our output deck
            print('\nDeck: ', deck)

        elif a._size == 1:
            # handling the case when we
            # only have one element in Queue
            print('\nQueue: ', a._array)
            deck.append(a.dequeue())
            print('\nDeck: ', deck)
            
    print('\nQueue is now empty, and we have completed the magic trick.')
    print()

transfer_cards()   # calling on function
