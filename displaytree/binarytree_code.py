#B PRAJEETH
#original final copy 20/5/22
#THIS CODE HAS EVERYTHING IN TERMS OF FUNCTION, YOU CAN USE THE printree FUNCION OF THIS CODE AND PRINT THE BINARY TREE SUCCESSFULLY


def Preorder(root,right,left,val,n,ar,y,x,max_width):
    #print("inside")
    #for i in range(3):
    #  print(ar[i])
    if root:
        ar[2*y][x-1]=getattr(root,val)
        if(len(str(getattr(root,val))) > max_width[0]):
            max_width[0] = len(str(getattr(root,val)))        
        
        if(n > y+1):
            for i in range(1, (2**(n-y-2)) +1):
                ar[2*y][x-1+i]="_"
                ar[2*y][x-1-i]="_"
            ar[2*y +1][x-1 - (2**(n-y-2))]="|"
            ar[2*y +1][x-1 + (2**(n-y-2))]="|"
        y=y+1
        if(y <= n-1):
            ar[2*y][x-1 - (2**(n-y-1)) ]="?"
            ar[2*y][x-1 + (2**(n-y-1)) ]="?" 
            
        Preorder(getattr(root,left),right,left,val,n,ar,y,x-(2**(n-y-1)),max_width)
        Preorder(getattr(root,right),right,left,val,n,ar,y,x+(2**(n-y-1)),max_width)
        y=y-1
 
def maxDepth(node,left,right):  #function to calculte the maximum depth of a tree
    if node is None:
        return -1 ;
 
    else :

        lDepth = maxDepth(getattr(node,left),left,right)
        rDepth = maxDepth(getattr(node,right),left,right)

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1  

def binarytree(r,right,left,val):
    ar=[]
    n=maxDepth(r,left,right) +1 # height of tree
    for i in range(2*n):
      ls=[]
      for j in range((2**n)-1):
        ls.append("")
      ar.append(ls)    
    
    y=0
    x=2**(n-y-1)
    #print("printing tree ... \n")
    max_width=[0]
    Preorder(r,right,left,val,n,ar,y,x,max_width)
    
    for i in range(2*n):
        ct=0
        ct1=0
        for j in range((2**n)-1):
            if(ar[i][j]==""):
                print(" "*max_width[0],end="")
            else:
                width=max_width[0] - len(str(ar[i][j]))
                if(ar[i][j] != "_" and ar[i][j]!="?" and ar[i][j]!="|" and width>0):
                    ct1 = ct1 +1
                    if(i != 2*n - 2):
                        if(ct1%2 == 0):
                            print("_"*(width) + str(ar[i][j]),end="")
                        else:
                            print(str(ar[i][j]) + "_"*(width) ,end="")
    
                    else:  
                        if(ct1%2 == 0):
                            print(" "*(width) + str(ar[i][j]),end="")
                        else:
                            print(str(ar[i][j])+" "*(width) ,end="")   
                elif(ar[i][j]=="?"):
                    ct1=ct1+1
                    if(ct1 %2 == 0):
                        print(" "*width + str(ar[i][j]),end="")  
                    else:
                        print(str(ar[i][j]) + " "*width ,end="")  
                elif(ar[i][j] == "_"):
                    print(ar[i][j]*max_width[0],end="")
                else:
                    ct=ct+1
                    if(ct%2 == 0):
                        print(" "*(width) + str(ar[i][j]),end="") 
                    else:
                        print(str(ar[i][j]) + " "*(width),end="")   

        print()   



