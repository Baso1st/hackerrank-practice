if __name__ == '__main__':
    x = [1, 2]
    y = [[2, 1], [2, 3], [3, 4]]
    #print(x in y)
    print(max(2, 2))


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return []
        if not node[0]:
            return [[]]
        
        q = []
        new_node = Node(node.val)
        node_table = {}
        node_table[node] = new_node
        q.append((node, new_node))
        visited = set()
        while q:
            node, new_node = q.pop(0)
            visited.add(node)
            for adj in node.neighbors:
                if adj not in visited:
                    new_adj = Node(adj.val)
                    node_table[adj] = new_adj
                    new_node.neighbours.append(new_adj)
                    new_adj.neighbours.append(new_node)
                    q.append((adj, new_adj))
                    visited.add(adj)
                    
        return new_node
                 
                 
                    