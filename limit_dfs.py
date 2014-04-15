import numpy

def dfs(A_list,head,goal,stack,path,depth,limit):    #graph list,start,goal,stack[],path[],depth[]=0
    path.append(head)
    path[depth[head]]=head
    #print path    
    if head == goal:    #goal test
        for x in path[depth[head]+1:]:    #remove path after goal
            path.pop()
        return path
    else:
        flag=True    #control path pop, if head no other link (is leaf)
        if depth[head]< limit:
            for node in A_list[head]:        
                stack.append(node)
                depth[node]=depth[head]+1
                flag=False
        if flag:
            #print 'before pop path=',path
            for x in path[depth[head]:]:
                path.pop()          
            #print 'path=',path
        if stack:
            #print 'stack',stack
            path=dfs(A_list,stack.pop(),goal,stack,path,depth,limit)
    #print 'path[%d]=%s'%(depth,path[depth])
    print depth
    return path
#######################################################
Alist=[[1,2,3],[9,10],[4,5],[2,11],[],[],[7,8],[],[],[],[],[6]]
depth=[]
[depth.append(0) for x in range(12)]
limit=4
for i in range(12):
    path=dfs(Alist,0,i,[],[],depth,limit)
    print 'out',i,path

