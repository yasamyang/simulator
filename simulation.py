# -*- coding: UTF-8 -*-
from __future__ import division
import sys
sys.setrecursionlimit(999999999)
import time
import random
import it_dfs

class aService():
	name=''
	inp=''	#input=''
	out=''	#output=''
	con=''	#condition=''
	eff=''	#effect=''

def findser(task,AS,Alist):
    inp=AS[int(task[0][2:])].inp
    out=AS[int(task[len(task)-1][2:])].out
    #print "inp",inp,"out",out
    start=[]
    goal=[]
    for aser in AS:
        if inp==aser.inp:
            if out==aser.out:
                return [int(aser.name[2:])]
            start.append(int(aser.name[2:]))
        if out==aser.out:
            goal.append(int(aser.name[2:]))
    #random.shuffle(start)
    #random.shuffle(goal)       
    #print 'start',[x for x in start]
    #print 'goal',[x for x in goal]
    limit=100
    for s in start:
        for g in goal:
            #print 's',s,'g',g
            path=it_dfs.it_dfs(Alist,s,g,limit)
            if path:
                return path
    return []
def main():
    tStart=time.time()
    ###read AS file###
    AS=[]
    fileopen = open('AS.txt','r')
    ASi=0
    while True:             
        line = fileopen.readline()  
        if not line: 
            break
        else:
            temp=line.split(',')
            AS.append(aService())
            AS[ASi].name=temp[0]
            AS[ASi].inp=temp[1]
            AS[ASi].out=temp[2]
            AS[ASi].con=temp[3]
            AS[ASi].eff=temp[4]
            #print AS[ASi].inp,AS[ASi].out
            ASi+=1
    fileopen.close()
    ###graph list###
    Alist=[]
    for as1 in AS:
        alist=[]
        for as2 in AS:
            if as1.out == as2.inp:
                alist.append(int(as2.name[2:]))    #trans into number
        Alist.append(alist)
    #print 'Alist',[x for x in Alist]
    ##########################################
    ###read testTasks file###
    testTasks=[]
    fileopen = open('testTasks.txt','r')
    ti=0
    while True:             
        line = fileopen.readline()  
        if not line: 
            break
        else:
            temp=line.split(',')
            testTasks.append([])
            [testTasks[ti].append(x) for x in temp[:-1]]
            ti+=1
    #print 'testTasks',testTasks
    fileopen.close()
    ###read ontology file###
    onTasks=[]
    fileopen = open('ontology.txt','r')
    oi=0
    while True:             
        line = fileopen.readline()  
        if not line: 
            break
        else:
            temp=line.split(',')
            onTasks.append([])
            [onTasks[oi].append(x) for x in temp[:-1]]
            oi+=1
    #print "onTasks",onTasks
    fileopen.close()
    nMatch=0
    nfs=0
    aim=0
    for task in testTasks:
        if task in onTasks:
            #time.sleep(1)
            nMatch+=1
            #print nMatch,task,'\n'
        else:
            #print task,'no match\n'
            as_path=findser(task,AS,Alist)        
            if as_path:
                i=0
                for p in as_path:
                    as_path[i]='AS'+str(as_path[i])
                    i+=1
                #print as_path
                if task == as_path:
                    #print "AI match"
                    aim+=1
            else:
                #print 'not find service'
                nfs+=1
    tot=len(testTasks)
    tEnd=time.time()
    print nMatch/tot,tot,nfs,aim,(tEnd-tStart),divmod((tEnd-tStart),60)
    return nMatch/tot,tot,nfs,aim,(tEnd-tStart),divmod((tEnd-tStart),60)
if __name__=='__main__':
    import service
    fileopen = open('result.txt','w')
    for i in range(10):
        ont_num=1000*i
        if i ==0:
            r_rate=0
        else:
            r_rate=i/10
        service.main(r_rate,ont_num)
        fileopen.write('ontology rate='+str(r_rate))
        fileopen.write('\n')
        for j in range(1):
            (rate,tot,nfs,aim,time_s,time_ms)=main()
            fileopen.write('rate='+str(rate)+' ')
            fileopen.write('tot='+str(tot)+' ') 
            fileopen.write('nfs='+str(nfs)+' ') 
            fileopen.write('aim='+str(aim)+' ') 
            fileopen.write('time_s='+str(time_s)+' ')    
            fileopen.write('time_ms='+str(time_ms)+' ')
            fileopen.write('\n')
    fileopen.close()  
        
