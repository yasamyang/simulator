def dfs(A_list,head,goal,stack,path,depth,limit,hight):    #graph list,start,goal,stack[],path[],depth[]=0
    #print 'depth[%d]=%d' %(head,depth[head]),'len(path)',len(path)
    path.append(head)
    try:
        path[depth[head]]=head
    except:
        pass
    #print path    
    if head == goal:    #goal test
        for x in path[depth[head]+1:]:    #remove path after goal
            path.pop()
        return path
    else:
        #flag=True    #control path pop, if head no other link (is leaf)
        if hight< limit:
            #print 'depth[%d]=%d' %(head,depth[head])
            for node in A_list[head]:
                if node != head:    # node doesn't link to self
                    stack.append(node)
                    depth[node]=depth[head]+1
                    #flag=False
        #if flag:
            #print 'before pop path=',path
            #for x in path[depth[head]:]:
                #path.pop()          
            #print 'path=',path
        if stack:
            #print 'stack',stack
            hight+=1
            path=dfs(A_list,stack.pop(),goal,stack,path,depth,limit,hight)
    #print 'path[%d]=%s'%(depth,path[depth])
    #print depth
    return path
#######################################################
def it_dfs(Alist,start,goal,limit):
    #Alist=[[1,2,3],[9,10],[4,5],[2,11],[],[],[7,8],[],[],[],[],[6]]
    #start=0
    #goal=1
    #limit=10
    #import time
    for i in xrange(limit):
        depth=[]
        [depth.append(0) for x in xrange(len(Alist))]
        #time.sleep(1)
        path=dfs(Alist,start,goal,[],[],depth,i,0)    
        if path and path[-1]==goal:
            return path
            #print 'out',i,path
            break
    return []
