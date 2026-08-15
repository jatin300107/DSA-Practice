import sys
input = sys.stdin.readline
import  heapq
class Solution:
    

    def __init__(self):
        self.n = int(input())
        
        self.xs = []
        self.ys = []
        for _ in range(self.n):
            x, y = map(int, input().split())
            self.xs.append(x)
            self.ys.append(y)
        
        self.cost = list(map(int, input().split()))  
        self.k = list(map(int, input().split()))
    def main(self):
        n = self.n
        xs, ys = self.xs, self.ys
        cost_arr, k_arr = self.cost, self.k

        visited = [False] * (n + 1)
        heap = [(0, n, -1)]
        total_cost = 0
        stations = []
        lines = []

        while heap:
            cost, node, source = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            total_cost += cost

            if node == n:
                for i in range(n):
                    if not visited[i]:
                        heapq.heappush(heap, (cost_arr[i], i, n))
            else:
                if source == n:
                    stations.append(node + 1)
                else:
                    lines.append((source + 1, node + 1))

                ki = k_arr[node]
                xi = xs[node]
                yi = ys[node]
                for j in range(n):
                    if not visited[j]:
                        edge_cost = (ki + k_arr[j]) * (abs(xi - xs[j]) + abs(yi - ys[j]))
                        heapq.heappush(heap, (edge_cost, j, node))

        print(total_cost)
        print(len(stations))
        print(*stations)
        print(len(lines))
        for u, v in lines:
            print(u, v)


        



if __name__ == "__main__":
    sol = Solution()
    sol.main()

# Description:
# This program solves the AtCoder problem "D - Shichikuji and Power Grid" using a
# minimum spanning tree (MST) idea on a complete graph of cities.
#
# Each city can either be connected to the power plant directly or through a
# cable network. The cost of connecting city i to city j is:
# (k[i] + k[j]) * (|x[i] - x[j]| + |y[i] - y[j]|)
# where k stores the power cost per station and (x, y) stores the city location.
#
# The algorithm builds a minimum-cost graph using a priority queue (Dijkstra-like
# MST process) starting from the power plant node n. It keeps track of:
# - the total minimum cost,
# - the set of cities connected directly to the plant,
# - the set of cable links chosen between cities.
#
# The output prints the final minimum total cost, the number and list of direct
# plant connections, and the number plus list of selected cable edges.
# This is a classic MST-based optimization problem that minimizes the total cost
# while ensuring every city is eventually connected to the power supply.
