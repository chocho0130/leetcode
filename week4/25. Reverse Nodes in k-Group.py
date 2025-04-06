from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev_group = dummy
        
        while True:
            # 檢查是否有足夠的 k 個節點
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # 剩餘節點不足 k 個，直接返回
            
            # 翻轉 k 個節點
            prev = None
            curr = prev_group.next #1
            next_group = kth.next  # 下一組開始的節點 3
            
            for _ in range(k):
                next_node = curr.next #2
                curr.next = prev #0
                prev = curr #1
                curr = next_node #2
            
            # 連接翻轉後的部分
            temp = prev_group.next  # 這是翻轉前的第一個節點，它會變成最後一個
            prev_group.next = prev  # 連接翻轉後的第一個節點
            temp.next = next_group  # 連接下一組節點
            prev_group = temp  # 移動 prev_group 到新的前一個節點
        
        return dummy.next