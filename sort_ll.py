def to_list(head):
    nums = []
    while head != None:
        nums.append(head.val)
        head = head.next
    
    return nums 

def sort_list(head):

    nums = to_list(head)
    nums.sort()
    curr = head
    k = 0

    while curr!=None:
        curr.val = nums[k]
        k += 1
        curr = curr.next

    return head
