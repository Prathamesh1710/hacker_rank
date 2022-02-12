'''
Reversing a doubly linked list
'''
def reverse(llist):
    if llist == None:
        return(llist)
    elif llist.next == None:
        llist.next, llist.prev = llist.prev, None
        return(llist)
    else:
        rdl = reverse(llist.next)
        llist.prev, llist.next = llist.next, llist.prev
        return(rdl)
