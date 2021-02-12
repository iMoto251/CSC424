import math;
import string;

def main():

    file1 = open('hw1Input.txt', 'r')
    Lines = file1.readlines()

    words = []
    longwords = []
    #punc = '''!()-[]{};:'"\,= <>./?@#$%^&*_~'''
    punc = string.punctuation


    for line in Lines:
        if line.strip():
            for ele in line:
                if ele in punc:
                    line = line.replace(ele," ")
            line = line.split()
            longwords.append(sorted(line, key=len))
        else:
            '''do nothing'''
    
    #print(longwords)
    
    for x in range(len(longwords)):
        try:
            print (longwords[x][-1].lower())
            print (longwords[x][-2].lower())
            print (longwords[x][-3].lower())
            print (longwords[x][-4].lower())
            print (longwords[x][-5].lower())
            print (longwords[x][-6].lower())
        except IndexError:
            pass
        print(" ---------- ")
        continue

if __name__ == '__main__':
    import sys;
    main()