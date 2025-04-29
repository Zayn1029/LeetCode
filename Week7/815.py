from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):

        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        for route_idx, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(route_idx)

        if target not in stop_to_routes:
            return -1

        queue = deque([(source, 0)])  
        visited_stops = set([source])
        visited_routes = set()
        
        while queue:
            curr_stop, buses_taken = queue.popleft()

            for route_idx in stop_to_routes[curr_stop]:

                if route_idx in visited_routes:
                    continue
                
                visited_routes.add(route_idx)

                for next_stop in routes[route_idx]:

                    if next_stop == target:
                        return buses_taken + 1

                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))

        return -1