from sys import stdin
from collections import defaultdict
import heapq

def BFS_SP(graph, start, goal): 
    explored = [] 
      
    queue = [[start]] 
      
    if start == goal:  
        return 0
      
    while queue: 
        path = queue.pop(0) 
        node = path[-1] 
          
        if node not in explored: 
            neighbours = graph[node] 
              
            for neighbour in neighbours: 
                new_path = list(path) 
                new_path.append(neighbour) 
                queue.append(new_path) 
                  
                if neighbour == goal:
                    new_path.remove(1)
                    new_path.remove(len(graph))
                    return new_path
            explored.append(node) 
    return -1

def dijkstra(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    pred = {}

    pred[starting_vertex]=-1

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                pred[neighbor] = current_vertex

    return distances, pred

def longestDistances(myGraph,hotels):
    sol = {x:[] for x in range(1,len(myGraph)+1)}
    visitados = []
    
    cola = []
    cola.append(1)

    while cola:
        node = cola.pop(0)
        d,p=dijkstra(myGraph,node)

        if node not in visitados:
            visitados.append(node)

            for i in hotels:
            
                if d[i] != float('inf') and d[i] < 601 and i != node:
                    if i not in sol[node]:
                        sol[node].append(i)
                    if node not in sol[i]:
                        sol[i].append(node)

                    cola.append(i)

            if d[len(myGraph)] < 601:
                if len(myGraph) not in sol[node]:
                        sol[node].append(len(myGraph))
                if node not in sol[len(myGraph)]:
                    sol[len(myGraph)].append(node)
    return sol


def main():
    myRawInput = stdin.readlines()

    myIndex = 0
    while myIndex < len(myRawInput)-1:
        
        numCities = int(myRawInput[myIndex].strip('\n'))
        hotels = list(map(int, myRawInput[myIndex+1][2:].strip('\n').split()))
        roads = int(myRawInput[myIndex+2].strip('\n'))
        myGraph = {x:{} for x in range(1,numCities+1)}

        for i in range(1,roads+1):
            case = list(map(int,myRawInput[myIndex+2+i].strip('\n').split()))
            myGraph[case[0]][case[1]] = case[2]
        
        reducedGraph = longestDistances(myGraph,hotels)
        sol = BFS_SP(reducedGraph,1,numCities)
        
        #print(f'grafo:{myGraph}')
        #print(f'grafo reducido:{reducedGraph}')
        if sol == -1:
            print(-1)
        else:
            print(len(sol))

        #print()
        
        myIndex += roads + 3

main()