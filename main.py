from threading import *
from doubleLinkList import DoubleLinkedList

dllist = DoubleLinkedList()

th_first = Thread()
th_second = Thread()

th_first.start()

th_first.join()
