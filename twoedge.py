import collections
time=0

def twoedge(adjlist,u,vis,start,pred):
    global time
    global sst
    vis[u]=1
    start[u]=time+1
    sst=start[u]
    for i in adjlist[u]:
        if(vis[i]==-1):
            pred[i]=u
            
            sst=min(sst,twoedge(adjlist,i,vis,start,pred))
        elif(pred[u]!=i):
            
            sst=min(sst,start[i])
    if(sst==start[u] and sst!=0):
        print("no and bridge edge is bw:",u,pred[u])
        
    
    return sst
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
    
    vis=[-1]*len(G)
    start=[-1]*len(G)
    pred=[0]*len(G)
    src=int(input("enter source"))
    twoedge(G,src,vis,start,pred)
    

main()
    
    
