from collections import deque

def is_solved(config):
    "Return whether input config is solved"
    ##################
    # YOUR CODE HERE #
    ##################
    k=len(config)
    for i in range(0,k):
        for j in range(0,k):
            if config[i][j] != k*i + j + 1:
                return False
    return True 

def move(config, mv):
    "Return a new configuration made by moving config by move mv"
    k = len(config)
    (s, i) = mv         # s in ("row", "col") and i in range(k)
    ##################
    # YOUR CODE HERE #
    ##################
    config1=[]
    for l in range(k):
        config1.append(list(config[l]))
    config=config1
    if s=="row":
        config[i].reverse()
        for j in range(k):
            config[i][j]=-config[i][j]
    else:
        col=[]
        for j in range(k):
            col.append(config[j][i])
        col.reverse()
        for j in range(k):
            config[j][i]=-col[j]
    return tuple([tuple(row) for row in config])

def solve_ksquare(config):
    "Return a list of moves that solves config"
    ##################
    # YOUR CODE HERE #
    ##################
    parent, solved = bfs(config)
    i=solved
    path=[]
    while i!=config:
        path.append(parent[i][1])
        i=parent[i][0]        
    return path[::-1]

def bfs(config):
    k=len(config)
    parent={config:[config,()]}
    q = deque([])
    q.append(config)
    while q:
        curr=q.popleft()
        for i in range(k):
            nex = move(curr,('row',i))
            if nex not in parent:
                parent[nex]= [curr,('row',i)]
                if is_solved(nex):
                    return parent, nex
                q.append(nex)
        for i in range(k):
            nex = move(curr,('col',i))
            if nex not in parent:
                parent[nex]= [curr,('col',i)]
                if is_solved(nex):
                    return parent, nex
                q.append(nex)
    return parent , config


