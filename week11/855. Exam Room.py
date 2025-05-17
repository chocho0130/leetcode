import bisect

class ExamRoom:

    def __init__(self, n: int):
        """
        初始化考場。
        :param n: 座位總數
        """
        self.n = n
        # 使用list 存有人坐的座位編號
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            # 沒人，坐在座位 0
            seat_to_take = 0
        else:
            # 找到最大的距離和對應的座位

            # 1. 從座位 0 到第一個已入座學生之間的距離
            max_dist = self.seats[0]
            seat_to_take = 0

            # 2. 相鄰已入座學生之間的距離
            for i in range(len(self.seats) - 1):
                p1 = self.seats[i]
                p2 = self.seats[i+1]
    
                dist = (p2 - p1) // 2
                if dist > max_dist:
                    max_dist = dist
                    seat_to_take = p1 + dist 

            # 3. 從最後一個已入座學生到座位 n-1 之間的距離
            last_seat = self.seats[-1]
            dist_to_end = (self.n - 1) - last_seat
            if dist_to_end > max_dist:
                max_dist = dist_to_end
                seat_to_take = self.n - 1 # 坐最後一個座位

        # 將最佳座位加入到已入座list中，並保持排序
        bisect.insort(self.seats, seat_to_take)

        return seat_to_take

    def leave(self, p: int) -> None:
        self.seats.remove(p)
