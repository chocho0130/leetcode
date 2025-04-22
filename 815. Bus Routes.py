from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 如果起點和終點相同，不需要搭公車
        if source == target:
            return 0

        # 建立 bus stop 到可搭乘的 bus 編號的對應關係
        # 例如：stop_to_buses[7] = {0, 1} 表示第 0 和 1 號 bus 都有經過 stop 7
        stop_to_buses = defaultdict(set)
        for bus_index, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].add(bus_index)

        # 記錄已經拜訪過的 bus stop，避免重複拜訪
        visited_stops = set()
        # 記錄已經搭過的 bus 編號，避免重複搭乘同一路 bus
        visited_buses = set()
        # BFS queue，裡面放的是 (目前所在的 bus stop, 已經搭乘的 bus 數量)
        queue = deque()
        queue.append((source, 0))

        # 開始進行 BFS 搜尋
        while queue:
            current_stop, buses_taken = queue.popleft()

            # 檢查所有從 current_stop 可搭的 bus
            for bus in stop_to_buses[current_stop]:
                # 如果這台 bus 已經搭過就跳過
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)

                # 檢查這台 bus 上的每一個停靠站
                for stop in routes[bus]:
                    # 如果有到達目標站點，回傳已搭公車數量 +1（現在這台 bus）
                    if stop == target:
                        return buses_taken + 1
                    # 如果這個 stop 沒拜訪過，就加入 queue 等待下一輪擴展
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop, buses_taken + 1))

        # 如果整個 BFS 結束都找不到目標站點，就代表無法到達
        return -1