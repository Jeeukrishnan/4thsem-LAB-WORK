import collections
def bfs(adjlist,src,vis,grp):
    deque=collections.deque()
    deque.append(src)
    vis[src]=True
    grp[src]=True
    while (len(deque)!=0):
        temp=deque.popleft()
        
        for i in adjlist[temp]:
            if vis[i]==False:
               deque.append(i)
               vis[i]=True
               grp[i]= not grp[temp]
            elif grp[temp]==grp[i]:
               return False
        print(temp)
    return True 
def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                first=False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)

    file.close()
    print(G)
    
    vis=[]
    grp=[]
    for i in range(6):
        vis.append(False)
        grp.append(False)
    src=int(input("enter source"))
     
    if(bfs(G,src,vis,grp)==True):
        print("bipartite ")
    else:
        print("not bipartite") 
    
main()
    
    
    
    
    