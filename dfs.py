import collections 
time=0
def dfs(adjlist,src,vis,start,stop,parent):
    global time
    vis[src]=1
    start[src]=time
    
    
    
    for i in adjlist[src]:
        
        if vis[i]==-1:
            time+=1
            print("tree edge",src,i)
            dfs(adjlist,i,vis,start,stop,src)
        elif vis[i]==1 and stop[i]==-1 and parent!=i :
            print("back edges",src,i)
            
    time+=1
    stop[src]=time
    print(src ," " ,start[src]," ",stop[src])
    
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
    
    vis=[-1]*6
    start=[-1]*6
    stop=[-1]*6
    src=int(input("enter source"))
    dfs(G,src,vis,start,stop,-1)
main()

    