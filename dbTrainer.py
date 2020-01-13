import random
import math
import time

baseNum = [2**0,2**1,2**3,2**4/10,2**5/10,2**6/10,2**7/100,2**8/100,10/2,10/4,10/8,100/16,4]
multiP = [0.01,0.1,1,10,100]
prefix = [1e-12,1e-9,1e-6,1e-3,1e0,1e3]
prefixLetter = ['p','n','u','m','','k']

baseNumDBM = [0,3,9,2,5,8,1,4,7,4,1,8,6]
multiPDBM = [-20,-10,0,10,20]
prefixDBM = [-90,-60,-30,0,30,60]

baseNumDBUV = baseNumDBM
multiPDBUV = multiPDBM
prefixDBUV = [-60,-30,0,30,60,90]

#Settings
method = 0 #0 ->dbm, 1 ->dbuV
direction = 0 #0 ->db, 1 ->val
randomize = 1

while(True):
    baseNumIndex = random.randint(0, len(baseNum)-1)
    multiPIndex = random.randint(0, len(multiP)-1)
    prefixIndex = random.randint(0, len(prefix)-1)

    num = baseNum[baseNumIndex]*multiP[multiPIndex]*prefix[prefixIndex]

    if (randomize):
        method = random.randint(0,1)
        direction = random.randint(0,1)

    if (method):
        db = baseNumDBUV[baseNumIndex]+multiPDBUV[multiPIndex]+prefixDBUV[prefixIndex]
        db = db*2
    else:
        db = baseNumDBM[baseNumIndex]+multiPDBM[multiPIndex]+prefixDBM[prefixIndex]

    if (direction):
        print(str(db), end='')

        if (method):
            print(" dbuV", end='')
        else:
            print(" dbm", end='')

        input()

        print(str(round(baseNum[baseNumIndex]*multiP[multiPIndex],4))+" "+prefixLetter[prefixIndex], end='')

        if (method):
            print("V\n")
        else:
            print("W\n")
            
    else:
        print(str(round(baseNum[baseNumIndex]*multiP[multiPIndex],4))+" "+prefixLetter[prefixIndex], end='')

        if (method):
            print("V", end='')
        else:
            print("W", end='')
        
        input()

        if (method):
            print(str(db)+" dbuV\n")
            #print(str(db)+" dbuV"+"\t"+str(20*math.log10(num/1e-6))+" dbuV\n")
        else:
            print(str(db)+" dbm\n")
            #print(str(db)+" dbm"+"\t"+str(10*math.log10(num/1e-3))+" dbm\n")