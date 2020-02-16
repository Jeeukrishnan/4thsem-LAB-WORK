import collections

def bfs(adjlist,src,vis,dist):
    deque=collections.deque([])
    deque.append(src)
    dist[src]=0
    vis[src]=True
    

    
    while (len(deque)!=0):
        temp=deque.popleft()
        for i in adjlist[temp]:
            if (vis[i]==False):
                deque.append(i)
                dist[i]=dist[temp]+1
                
                vis[i]=True
        
        print(temp,"dist: ",dist[temp])
    
                
    
    

    
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
    dist=[]
    for i in range(6):
        vis.append(False)
        dist.append(1000000)
    src=int(input("enter source"))
    bfs(G,src,vis,dist) 
    
main()
