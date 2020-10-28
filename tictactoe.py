cp="0"
ch="X"
scr={cp: 10, ch: -10, "tie": 0}

def win(t):
    for i in range(3):
        k=3*i
        if(t[k]==t[k+1] and t[k]==t[k+2] and t[k]!="_"):
            return t[k]
    for i in range(3):
        if(t[i]==t[3+i] and t[i]==t[6+i] and t[i]!="_"):
            return t[i]
    if(t[0]==t[4] and t[0]==t[8] and t[4]!="_"):
        return t[0]
    elif(t[2]==t[4] and t[2]==t[6] and t[4]!="_"):
        return t[2]
    for i in t:
        if(i=="_"):
            return "None"
    return "tie"


def minmax(t,d,isMax):
    val=win(t)
    if(val!="None"):
        return scr[val]
        
    if(isMax):
        best=(-1000)
        for i in range(len(t)):
            if(t[i]=="_"):
                t[i]=cp
                score=minmax(t,d+1,False)
                t[i]="_"
                best=max(score,best)
        return best

    else:
        best=1000
        for i in range(len(t)):
            if(t[i]=="_"):
                t[i]=ch
                score=minmax(t,d+1,True)
                t[i]="_"
                best=min(score,best)
        return best

def findBestMove(t):
    best=(-1000)
    bestMove=-1
    for i in range(len(t)):
        if(t[i]=="_"):
            t[i]=cp
            move = minmax(t,0,False)
            t[i]="_"
            if(move>best):
                bestMove=i
                best=move
    return bestMove

def display(t):
    for k in range(3):
        i=3*k
        print("{0} | {1} | {2}".format(t[i],t[i+1],t[i+2]))

def first(t):
    while(True):
        display(t)
        print("choose the position 0-8")
        inp=int(input())
        while(t[inp]!="_"):
            print("Wrong position!")
            print("Enter another position")
            inp=int(input())
        t[inp]=ch
        i=findBestMove(t)
        t[i]=cp
        res=win(t)
        if(res!="None"):
            if(res==cp):   print("You Lose!")
            if(res==ch):   print("You Win!")
            if(res=="tie"):   print("Draw!")
            break

def second(t):
    while(True):
        i=findBestMove(t)
        t[i]=cp
        display(t)
        print("choose the position 0-8")
        inp=int(input())
        while(t[inp]!="_"):
            print("Wrong position!")
            print("Enter another position")
            inp=int(input())
        t[inp]=ch
        res=win(t)
        if(res!="None"):
            if(res==cp):   print("You Lose!")  
            if(res==ch):   print("You Win!")
            if(res=="tie"):   print("Draw!")
            break

if(__name__ == "__main__"):
    t=["_"]*9
    print("Who goes first human or computer?Y/N")
    choice=input()
    if(choice=="Y" or choice=="y"):
        first(t)
    else:
        second(t)
