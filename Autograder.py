
def findTargets(target, numarray):
    for i in range(0, len(numarray)-1):
        for j in range(i,len(numarray)):
            if (numarray[i]+numarray[j]) == target :
                return (i,j)





def main():
    tartget = 42
    numbers = [3,7,9,18,22,36,6]
    print(findTargets(tartget,numbers))
    
    

if __name__ == "__main__":
    main()
