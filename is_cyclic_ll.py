def is_cyclic(head):
    if head==None or head.next==None:
        return False
        
    visited = [head]

    while head!=None:
        head = head.next 
        if head in visited:
            return True 
        visited.append(head)

    return False