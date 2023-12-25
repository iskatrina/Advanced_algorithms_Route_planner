import heapq #using for priority queue implementation
import math

#defining priority queue class in conjunction with  heapq library
class Node:
    def __init__(self, map_point, g_cost=0, h_cost=0, parent = None):
        self.map_point = map_point
        self.g_cost = g_cost  # Cost from start node to current node
        self.h_cost = h_cost  # Heuristic (estimated cost from current node to goal node) = line
        self.f_cost = g_cost + h_cost  # Total estimated cost
        self.parent = parent

    # defining the order measurement for prioroty queue
    def __lt__(self, other):
        return self.f_cost < other.f_cost
    
    
    
def heuristic_estimate(x1,y1,x2,y2):
    # Using line(Euclidean distance) as the heuristic measure
    # where (x1,x2) - coordinates of first point and (x2,y2) - coordinates of second point

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     
    

def shortest_path(M, start, goal):
    #creating start and goal points on the map
    start_node = Node(start)
    goal_node = Node(goal)
    
    #Frontier:
    frontier = []
    #Explored points:
    explored = set()
    
    #Convert frontier into a Priority Queue since we will need the lowest cost estimate for the path
    heapq.heapify(frontier) 
    
    #Add the start node to the frontier priority queue
    heapq.heappush(frontier,start_node) 
  
    while len(frontier) > 0:
        # Pop the element with the smallest priority    
        current_node = heapq.heappop(frontier)

        if current_node.map_point == goal_node.map_point:
            # Reverse - engeneer the path which leaded to this point
            #----------------
            path = []
            while current_node:
                path.insert(0, current_node.map_point)
                current_node = current_node.parent         
            return path
            #-------------------
        #move currently explored/poped node from frontier to explored set
        explored.add(current_node.map_point)
        
        
        #exemine each neighbour point for current node
        for neighbor_point in M.roads[current_node.map_point]:
            

            if neighbor_point not in explored:
                neighbor_node = Node(neighbor_point)
                neighbor_node.parent = current_node    
       
#                print(current_node.map_point,'=current node')
#                print(neighbor_node.map_point,'=neighbor node')
    
                current_node_x,current_node_y = M.intersections[current_node.map_point]
                neighbor_node_x,neighbor_node_y = M.intersections[neighbor_node.map_point]
                goal_node_x,goal_node_y = M.intersections[goal_node.map_point]
            
                neighbor_node.g_cost = current_node.g_cost + heuristic_estimate(current_node_x,current_node_y, neighbor_node_x,neighbor_node_y)
                neighbor_node.h_cost = heuristic_estimate(neighbor_node_x,neighbor_node_y, goal_node_x,goal_node_y)
                neighbor_node.f_cost = neighbor_node.g_cost + neighbor_node.h_cost

       
                if neighbor_node not in frontier:
                    heapq.heappush(frontier, neighbor_node)
                
    # If the frontier is empty and goal is not reached, there is no path
    return None

