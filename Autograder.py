
def findTargets(target_int, numarray_list_int):
    for i in range(0, len(numarray_list_int)-1):
        for j in range(i+1,len(numarray_list_int)):
            if (numarray_list_int[i]+numarray_list_int[j]) == target_int :
                tuple_end = (i,j)
                return tuple_end


def anylizeprogram(programfile):
    f = open("demofile.txt", "r")
    feedback= []
    i = 0
    for line in f.readlines:
        holder = eml(line)
        if(holder):
            feedback.append((eml(holder),i))
        i+=1
    return feedback
        


def main():
    tartget = 42
    numbers = [3,7,21,9,18,22,36,6]
    print(findTargets(tartget,numbers))
    
    
def eml(lineToAnylize):
    #define common rules
    pass


if __name__ == "__main__":
    main()
