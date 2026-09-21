from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
        
        if source not in stop_to_routes or target not in stop_to_routes:
            return -1
        
        visited_routes = [False] * len(routes)
        visited_stops = set([source])
        queue = deque()
        
        for r in stop_to_routes[source]:
            visited_routes[r] = True
            queue.append(r)
        
        buses = 1
        
        while queue:
            for _ in range(len(queue)):
                route_idx = queue.popleft()
                for stop in routes[route_idx]:
                    if stop == target:
                        return buses
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        for next_route in stop_to_routes[stop]:
                            if not visited_routes[next_route]:
                                visited_routes[next_route] = True
                                queue.append(next_route)
            buses += 1
        
        return -1