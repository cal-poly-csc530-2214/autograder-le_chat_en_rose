from re import search


def findTargets(target_int, numarray_list_int):
    for i in range(0, len(numarray_list_int)-1):
        for j in range(i+1,len(numarray_list_int)):
            if (numarray_list_int[i]+numarray_list_int[j]) == target_int :
                tuple_end = (i,j)
                return tuple_end

#delapidated to use convert_to_Mpy and overwrite this if we can get sketch 
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

#apply eml rules to create mypy lang        
def convert_To_Mpy(program):
    f = open("myPyFile.txt","w")
    for line in program:
        f.write(eml(line))


def main():
    tartget = 42
    numbers = [3,7,21,9,18,22,36,6]
    print(findTargets(tartget,numbers))

    program = open("demofile.txt").readlines()
    convert_To_Mpy(program)

    
#eml rules applied to each line    
def eml(lineToAnylize):
    #define common rules
    # range(a1; a2) then range(a1 + 1; a2)
    # a0 == a1 then False
    # range ({ 0 ,1},len
    
    if "range" in lineToAnylize:
        after_range = lineToAnylize.find('(') + 1
        before_comma = lineToAnylize.find(',')
        to_be_update = lineToAnylize[after_range: before_comma]
        updated = "{"+to_be_update + " + 1}"
        lineToAnylize = lineToAnylize[: after_range] + updated + lineToAnylize[before_comma:]
    elif "==" in lineToAnylize:
        after_if = lineToAnylize.find('if') + 3
        before_end = lineToAnylize.find(':')
        updated = "{" + lineToAnylize[after_if: before_end] + ",False}"
        lineToAnylize = lineToAnylize[: after_if] + updated + lineToAnylize[before_end:]

    return lineToAnylize
    


            


if __name__ == "__main__":
    main()
