# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 建立虛擬節點，並將其 next 指向 head
        dummy = ListNode(-1) #虛擬節點
        dummy.next = head
        current = dummy #在交換過程中它會移動，最終失去了指向虛擬節點的參考
        
        # 當有至少兩個節點可供交換時
        while current.next and current.next.next:
            first = current.next          # 第一個節點
            second = current.next.next    # 第二個節點
            
            # 執行交換:
            # 1. 將第一個節點的 next 指向第二個節點的下一個節點
            first.next = second.next
            # 2. 將第二個節點的 next 指向第一個節點
            second.next = first
            # 3. 讓 current.next 指向第二個節點，完成連接
            current.next = second
            
            # 移動 current 到剛才交換後的第一個節點（也就是下一次待交換對的前一個節點）
            current = first
        
        # dummy.next 為新的 head
        return dummy.next