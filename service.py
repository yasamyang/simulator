# -*- coding: UTF-8 -*-
import random

class task():
	start=''
	goal=''
	
class ontology():
	init=''
	goal=''
	task=[]
			
class aService():
	name=''
	inp=''	#input=''
	out=''	#output=''
	con=''	#condition=''
	eff=''	#effect=''

class cService(aService):
	rank=0	

###generate random tasks############################################################
def ranGenSer(length,simple,AS):
    #print simple
    gTask=[]
    r=random.randint(1,length-1) 
    rn=random.randint(0,simple-1)
    gTask.append(AS[rn]) #first AS
    init=AS[rn].inp	 #initial state
    for i in xrange(r):	#each task has 2~10 AS
        cand=[]
        for j in xrange(simple):
            if gTask[i].out==AS[j].inp:
                cand.append(AS[j]) #generate candidate set
		
        #print gTask[i].name,[x.name for x in cand]
        if cand:
            gTask.append(random.choice(cand))	#random choice one from canidate
        else:
            break
    goal=gTask[len(gTask)-1].out    #goal state
    return gTask
    #print [x.name for x in gTask],[x.inp for x in gTask],[x.out for x in gTask]
    #print init,goal
################################################################################
def main(r_rate,ont_num):
    #generate service
    iArray=[]
    oArray=[]
    cArray=[]
    eArray=[]
    iope=1000    #iope complex

    for i in xrange(iope):
	    iArray.append('inp'+str(i))
	    oArray.append('out'+str(i))
	    cArray.append('con'+str(i))
	    eArray.append('eff'+str(i))

    AS=[]
    CS=[]
    CSi=0
    ASi=10000  #services number
    fileopen = open('AS.txt','w') 
    for i in xrange(ASi):
	    AS.append(aService())
	    AS[i].name='AS'+str(i)
	    AS[i].inp=random.choice(iArray)
	    AS[i].out=random.choice(iArray)
	    AS[i].con=random.choice(iArray)
	    AS[i].eff=random.choice(iArray)
	    fileopen.write(AS[i].name+','+AS[i].inp+','+AS[i].out+','+AS[i].con+','+AS[i].eff+','+'\n')
	    r=random.randint(1,20) #each AS has 1~10 CS
	    for j in xrange(r):
		    CS.append(cService())
		    CS[CSi].name='CS'+str(CSi)
		    CS[CSi].inp=AS[i].inp
		    CS[CSi].out=AS[i].out
		    CS[CSi].con=AS[i].con
		    CS[CSi].eff=AS[i].eff
		    CS[CSi].rank=random.randint(0,5) #each CS has 0~5 random rank
		    CS[CSi].AS=AS[i]
		    #print CSi,CS[CSi].AS.name
		    CSi+=1
    #print CSi
    fileopen.close()
	
    aTask=[]
    for i in xrange(20): 
	    aTask.append(task())
	    aTask[i].start=random.choice(iArray)
	    aTask[i].goal=random.choice(oArray)
	    #print aTask[i].start


    ###generate Ontology & save in file###
    fileopen = open('ontology.txt','w') 
    onTask=[]
    for p in xrange(ont_num): #generate 100 task
	    gTask=ranGenSer(20,ASi,AS)	#random size & simple size
	    onTask.append(gTask)
	    [fileopen.write(x.name+',') for x in gTask]	#write AS.name into file
	    fileopen.write('\n')
    fileopen.close()                

    ###generate testTasks###
    fileopen = open('testTasks.txt','w') 
    for p in xrange(10000): #generate 100 task
	    ran=random.random()
	    #print ran
	    if ran>r_rate:   #control ontology ratio
		    testTask=ranGenSer(20,ASi,AS)	#random size & simple size
		    [fileopen.write(x.name+',') for x in testTask]	#write AS.name into file
		    fileopen.write('ran'+'\n')
	    else:
		    testTask=random.choice(onTask)
		    [fileopen.write(x.name+',') for x in testTask]
		    fileopen.write('ont'+'\n')
    fileopen.close()    
    fileopen = open('ontology.txt')
    while True:             
        line = fileopen.readline()  
        if len(line) ==0:           
            break
        #print (line)
    fileopen.close()

if __name__=='__main__':
    for i in range(1,10):
        r_rate=i/10
        ont_num=1000*i
        main(r_rate,ont_num)

