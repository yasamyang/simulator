for i in range(1,11):
    for j in range (1,2):
        str='result(io%d,%d%d%d).txt' %(i,j,j+3,j+6)
        print str
fileopen = open(str,'r')
    ASi=0
    while True:             
        line = fileopen.readline()
        print line
