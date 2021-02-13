import math;
import string;
longwords = []

def getwords():
    file1 = open('hw1Input.txt', 'r')
    Lines = file1.readlines()


    for line in Lines:
        if line.strip():
            for a in line:
                if a in string.punctuation:
                    line = line.replace(a," ")
            line = line.split()
            longwords.append(sorted(line, key=len))
        else:
            '''do nothing'''
    file1.close()
    return longwords

def writedictionary(longwords):
    file2 = open('hw1Output.txt', 'w')
    sorteddict = []
    for x in range(len(longwords)):
        try:
            sorteddict.append((longwords[x][-1].lower() + ": " + longwords[x][-2].lower() + ", " + longwords[x][-3].lower() + ", " + longwords[x][-4].lower() + ", " + longwords[x][-5].lower() + ", " + longwords[x][-6].lower()))
        except IndexError:
            pass
        continue

    sorteddict.sort()
    #print sorteddict
    for y in range(len(sorteddict)):
        try:
            file2.write(sorteddict[y] + "\n")
        except IndexError:
            pass
        continue

    file2.close()


def main():
    thedict = getwords()
    writedictionary(thedict)

if __name__ == '__main__':
    import sys;
    main()