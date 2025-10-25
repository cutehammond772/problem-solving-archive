import sys
sys.setrecursionlimit(1010)

def solution(nodeinfo):
    answer = [[]]
    
    # node: ((-y, x), x, y, node)
    # 1. 부모 노드부터 보이도록 정렬
    N = len(nodeinfo)
    NODE_X, NODE_Y, NODE_NUM = [1, 2, 3]
    ordered_nodes = []
    
    for i in range(N):
        x, y = nodeinfo[i]
        node = i + 1
        
        ordered_nodes.append(((-y, x), x, y, node))
    
    ordered_nodes.sort()
    
    # 2. 이진 트리 구성
    graph = [[] for _ in range(N + 1)]
    
    def construct(graph, nodes):
        if len(nodes) == 0:
            return None
        
        root_node = nodes[0]
        child_left, child_right = [], []
        
        for i in range(1, len(nodes)):
            child_node = nodes[i]
            
            if root_node[NODE_X] > child_node[NODE_X]:
                child_left.append(child_node)
            else:
                child_right.append(child_node)
        
        child_left_root = construct(graph, child_left)
        child_right_root = construct(graph, child_right)
        
        if child_left_root is not None:
            graph[root_node[NODE_NUM]].append(child_left_root[NODE_NUM])
        
        if child_right_root is not None:
            graph[root_node[NODE_NUM]].append(child_right_root[NODE_NUM])
        
        return root_node
    
    root = construct(graph, ordered_nodes)
    
    # 3. 전위, 후위 순회
    def preorder(node, graph, log):
        log.append(node)
        
        for next_node in graph[node]:
            preorder(next_node, graph, log)
    
    def postorder(node, graph, log):
        for next_node in graph[node]:
            postorder(next_node, graph, log)
        
        log.append(node)
    
    preorder_log, postorder_log = [], []
    
    preorder(root[NODE_NUM], graph, preorder_log)
    postorder(root[NODE_NUM], graph, postorder_log)
    
    return [preorder_log, postorder_log]