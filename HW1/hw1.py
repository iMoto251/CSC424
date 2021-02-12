import math;
import string;

def main():

    file1 = open('hw1Input.txt', 'r')
    Lines = file1.readlines()

    words = []
    longwords = []
    # = ['.',";",":","!","?","/","\\",",","#","@","$","&",")","(","'","\"", '"']
    #translation = {33: 32, 34: 32, 35: 32, 36: 32, 37: 32, 38: 32, 39: 32, 40: 32, 41: 32, 42: 32, 43: 32, 44: 32, 45: 32, 46: 32, 47: 32, 58: 32, 59: 32, 60: 32, 61: 32, 62: 32, 63: 32, 64: 32, 91: 32, 92: 32, 93: 32, 94: 32, 95: 32, 96: 32, 123: 32, 124: 32, 125: 32, 126: 32}
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
        
    #print(longwords[0][-1])
    #print(longwords[1][-1])
    #print(longwords[1][-2])





if __name__ == '__main__':
    import sys;
    main()