import math;
import string;

def main():

    file1 = open('hw1Input.txt', 'r')
    Lines = file1.readlines()

    words = []
    punc_list = ['.',";",":","!","?","/","\\",",","#","@","$","&",")","(","'","\"", '"']
    #translation = {33: 32, 34: 32, 35: 32, 36: 32, 37: 32, 38: 32, 39: 32, 40: 32, 41: 32, 42: 32, 43: 32, 44: 32, 45: 32, 46: 32, 47: 32, 58: 32, 59: 32, 60: 32, 61: 32, 62: 32, 63: 32, 64: 32, 91: 32, 92: 32, 93: 32, 94: 32, 95: 32, 96: 32, 123: 32, 124: 32, 125: 32, 126: 32}

    for line in Lines:
        if line.strip():
            line = line.translate(None, string.punctuation)
            words.append(line.strip())
        else:
            '''print("hello")'''
    
    print(words[0])


    #punc_list = ['.',";",":","!","?","/","\\",",","#","@","$","&",")","(","'","\"", '"']
    new_words = ''
    for i in words:
        if i not in punc_list:
            new_words += i
        else:
            new_words += ' '

    print(new_words)
    #tuple1 = tuple(words)
    #print(tuple1)


if __name__ == '__main__':
    import sys;
    main()