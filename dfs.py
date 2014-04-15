import numpy

def dfs(A_list,head,goal,stack,path,depth):
    path.append(head)
    path[depth[head]]=head
    #print path    
    if head == goal:
        for x in path[depth[head]+1:]:
            path.pop()
        return path
    else:
        flag=True
        for node in A_list[head]:        
            stack.append(node)
            depth[node]=depth[head]+1
            flag=False
        if flag:
            #print 'before pop path=',path
            for x in path[depth[head]:]:
                #print 'x=',x
                path.pop()          
            #print 'path=',path
        if stack:
            #print 'stack',stack
            path=dfs(A_list,stack.pop(),goal,stack,path,depth)
    #print 'path[%d]=%s'%(depth,path[depth])
    #print depth
    return path
#######################################################
Alist=[[1,2,3],[9,10],[4,5],[2,11],[],[],[7,8],[],[],[],[],[6]]
depth=[]
[depth.append(0) for x in range(12)]
#print depth
for i in range(12):
    path=dfs(Alist,0,i,[],[],depth)
    print 'out',i,path

