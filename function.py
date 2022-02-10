from random import choice,randint

def rand_block():
    random_block = [
        [[1,0],[1,1],[1,2],[0,2]],    #jblock
        [[1,0],[1,1],[1,2],[2,2]],          #lblock
        [[1,0],[0,1],[1,1],[2,1]],   #tblock
        [[1,1],[1,2],[0,2],[2,1]],    #sblock
        [[1,1],[1,2],[0,1],[2,2]],      #zblock
        [[1,0],[1,1],[1,2],[1,3]],      #iblock
        [[0,0],[0,1],[1,0],[1,1]]        #oblock
    ]
    return choice(random_block)

def creatDic(rows):
    dic = {}
    for r in range(rows):
        dic[r]=[[],[]]
    return dic

def a_direction(yAxis,xAxis,which_block,dic,cell_size=30,rows=20,cols=10):
    '''cheak is there space for the next given step
    '''
    for r in which_block:
        if not ((xAxis+r[0])*cell_size <cell_size*cols and (xAxis+r[0])*cell_size>-1 and (yAxis+r[1])*cell_size<cell_size*rows): 
            return False
        elif yAxis+r[1] in dic:
            if xAxis+r[0] in dic[yAxis+r[1]][0]:
                return False

    return True

def rotate_block(block,dic,velocity,change):
    t_block = []
    if block==[[0,0],[0,1],[1,0],[1,1]]:
        return block
    for r in block[::-1]:
        lis = [r[1],r[0]]
        if lis[1]==0:
            lis[1]=2
        elif lis[1]==2:
            lis[1]=0
        t_block.insert(0,lis)
    
    if a_direction(velocity,change,t_block,dic):
        return t_block
    return block

def newBlock(block,dic,velocity,change,color,scoreBoard,rows=20):
    '''create the new block and update the settled blocks
    return the new block, updated dic, updated velocity and change
    '''
    for r in block:
        if r[1]+velocity>=0:
            dic[r[1]+velocity][0].append(r[0]+change)
            dic[r[1]+velocity][1].append(color)
        else:
            return 0
    
    count = 0
    for r in range(len(dic))[::-1]:
        if len(dic[r][0]) == 10:
            dic[count].append(1)
            count+=1
        else:
            dic[r+count]=dic[r]
            if len(dic[r]) == 3:
                dic[r+count]=[[],[]]
    # print("score is: ",count)
    return [rand_block(),dic,-2,0,scoreBoard+count]


