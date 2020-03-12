maxnumbers = 10

def main():
    outputLinear()
    outputFibonacci()
    outputGeometric()

def outputLinear():
    mylist = [1] 
    count = 0
    output = ""
    for x in mylist:
        if count < maxnumbers:
            mylist.append(count)
            output = output + str(x) + ","
            count = count + 1
        else:
            print("Lineare getallen reeks: " + output) 

def outputFibonacci():
    mylist = [1,2] 
    count = 0
    output = ""

    for x in mylist:
        if count < maxnumbers:
            mylist.append(mylist[count]+mylist[count + 1])
            output = output + str(x) + ", "
            count = count + 1
        else:
            print("Fibonacci getallen reeks: " + output)    

def outputGeometric():
    mylist = [1,2] 
    count = 0
    output = ""

    for x in mylist:
        if count < maxnumbers:
            mylist.append(mylist[-1]*2)
            output = output + str(x) + ", "
            count = count + 1
        else:
            print("Geometrische getallen reeks: " + output)   


if __name__ == '__main__':
  main()