from typing import List, Optional

# 鏈結串列的定義
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 如果整個 lists 是空的，直接回傳 None
        if not lists:
            return None

        # 逐個合併所有鏈結串列
        while len(lists) > 1:
            merged_lists = []

            # 每次合併兩條串列
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                # 合併 l1 和 l2
                merged_lists.append(self.mergeTwoLists(l1, l2))

            # 更新 lists：把合併後的串列放回來繼續合併
            lists = merged_lists

        return lists[0]

    # 合併兩條已排序的鏈結串列
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        # 兩個串列都還有節點時
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # 把剩下的接上去
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next