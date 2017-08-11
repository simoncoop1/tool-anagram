import string
import itertools
import math

class MyCrossword:
    __doc__ = "helper to solve crossword puzzles"
    
    def __init__(self):
        return

    def GeneratePermutation(self,A=None,B=None,C=None,D=None,E=None,F=None,G=None,H=None,I=None,J=None,K=None):
        if K is not None:
            for perm in self.GeneratePermutation(B,C,D,E,F,G,H,I,J,K):
                yield A + perm
            for perm in self.GeneratePermutation(A,C,D,E,F,G,H,I,J,K):
                yield B + perm
            for perm in self.GeneratePermutation(A,B,D,E,F,G,H,I,J,K):
                yield C + perm
            for perm in self.GeneratePermutation(A,B,C,E,F,G,H,I,J,K):
                yield D + perm
            for perm in self.GeneratePermutation(A,B,C,D,F,G,H,I,J,K):
                yield E + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,G,H,I,J,K):
                yield F + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,H,I,J,K):
                yield G + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G,I,J,K):
                yield H + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G,H,J,K):
                yield I + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G,H,I,K):
                yield J + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G,H,I,J):
                yield K + perm
        elif J is not None:
            for perm in self.GeneratePermutation(B,C,D,E,F,G,H,I,J):
                yield A + perm
            for perm in self.GeneratePermutation(A,C,D,E,F,G,H,I,J):
                yield B + perm
            for perm in self.GeneratePermutation(A,B,D,E,F,G,H,I,J):
                yield C + perm
            for perm in self.GeneratePermutation(A,B,C,E,F,G,H,I,J):
                yield D + perm
            for perm in self.GeneratePermutation(A,B,C,D,F,G,H,I,J):
                yield E + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,G,H,I,J):
                yield F + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,H,I,J):
                yield G + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G,I,J):
                yield H + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G,H,J):
                yield I + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G,H,I):
                yield J + perm
        elif I is not None:
            for perm in self.GeneratePermutation(B,C,D,E,F,G,H,I):
                yield A + perm
            for perm in self.GeneratePermutation(A,C,D,E,F,G,H,I):
                yield B + perm
            for perm in self.GeneratePermutation(A,B,D,E,F,G,H,I):
                yield C + perm
            for perm in self.GeneratePermutation(A,B,C,E,F,G,H,I):
                yield D + perm
            for perm in self.GeneratePermutation(A,B,C,D,F,G,H,I):
                yield E + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,G,H,I):
                yield F + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,H,I):
                yield G + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G,I):
                yield H + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G,H):
                yield I + perm
        elif H is not None:
            for perm in self.GeneratePermutation(B,C,D,E,F,G,H):
                yield A + perm
            for perm in self.GeneratePermutation(A,C,D,E,F,G,H):
                yield B + perm
            for perm in self.GeneratePermutation(A,B,D,E,F,G,H):
                yield C + perm
            for perm in self.GeneratePermutation(A,B,C,E,F,G,H):
                yield D + perm
            for perm in self.GeneratePermutation(A,B,C,D,F,G,H):
                yield E + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,G,H):
                yield F + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,H):
                yield G + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F,G):
                yield H + perm
        elif G is not None:
            for perm in self.GeneratePermutation(B,C,D,E,F,G):
                yield A + perm
            for perm in self.GeneratePermutation(A,C,D,E,F,G):
                yield B + perm
            for perm in self.GeneratePermutation(A,B,D,E,F,G):
                yield C + perm
            for perm in self.GeneratePermutation(A,B,C,E,F,G):
                yield D + perm
            for perm in self.GeneratePermutation(A,B,C,D,F,G):
                yield E + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,G):
                yield F + perm
            for perm in self.GeneratePermutation(A,B,C,D,E,F):
                yield G + perm
        elif F is not None:
            for perm in self.GeneratePermutation(B,C,D,E,F):
                yield A + perm
            for perm in self.GeneratePermutation(A,C,D,E,F):
                yield B + perm
            for perm in self.GeneratePermutation(A,B,D,E,F):
                yield C + perm
            for perm in self.GeneratePermutation(A,B,C,E,F):
                yield D + perm
            for perm in self.GeneratePermutation(A,B,C,D,F):
                yield E + perm
            for perm in self.GeneratePermutation(A,B,C,D,E):
                yield F + perm
        elif E is not None:
            for perm in self.GeneratePermutation(B,C,D,E):
                yield A + perm
            for perm in self.GeneratePermutation(A,C,D,E):
                yield B + perm
            for perm in self.GeneratePermutation(A,B,D,E):
                yield C + perm
            for perm in self.GeneratePermutation(A,B,C,E):
                yield D + perm
            for perm in self.GeneratePermutation(A,B,C,D):
                yield E + perm
        elif D is not None:
            for perm in self.GeneratePermutation(B,C,D):
                yield A + perm
            for perm in self.GeneratePermutation(A,C,D):
                yield B + perm
            for perm in self.GeneratePermutation(A,B,D):
                yield C + perm
            for perm in self.GeneratePermutation(A,B,C):
                yield D + perm
        elif C is not None:
            for perm in self.GeneratePermutation(B,C):
                yield A + perm
            for perm in self.GeneratePermutation(A,C):
                yield B + perm
            for perm in self.GeneratePermutation(A,B):
                yield C + perm
        elif B is not None:
            for perm in self.GeneratePermutation(B):
                yield A + perm
            for perm in self.GeneratePermutation(A):
                yield B + perm
        elif A is not None:
            yield A
        else:
            #self.permutations.append(Baked)
            print("error")
            
    def PermutationGenerator(self,input):
        for char in input:
            yield char.upper()
        
    def GeneratePermutation_Test(self):
        chars =["a","b","c","d","e","f","g","h","i"]
        baked = ""        
        self.GeneratePermutation(baked,chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8])
        return
        
    def GeneratePermutation_Jun28_1(self):
        #chars =["c","a","r","t","o","o","t","e","d"]
        #baked = ""        
        #self.GeneratePermutation(baked,chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8])
        return
        
    def GeneratePermutation_Jun28_2(self):
        chars =["c","e","p","s","p","r","o","u","t","s"]
        baked = ""        
        self.GeneratePermutation(baked,chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9])
        return
        
    def GeneratePermutation_Jun28_3(self):
        chars =["b","r","u","i","s","e","d","l","o","f","t"]
        baked = ""        
        self.GeneratePermutation(baked,chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9],chars[10])
        return
    
    def CrossReference_Jun28_1(self):
        words = self.LoadWords()
        self.GeneratePermutation_Jun28_1()
        
        #indexs = self.IndexPermutation()
        
       
        chars =["c","a","r","t","o","o","t","e","d"]
        
        
        wordsDictionary = self.DictionaryOfWords()       
        
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8]):
            if perm.lower() in wordsDictionary:            
                print(perm + " in Dictionary " + "And permutation " + perm)
                
        
        ##for perm in self.permutations:
        
        ##    startat = indexs[perm[0].lower()]
        
        ##    for word in itertools.islice(words,startat,len(words)-1):
        ##        if word[:7].lower() == perm[:7].lower():
        ##            print("Dictionary word is: " + word + " Permutation is: " + perm)
                    
        ##        if word[0] > perm[0]:
        ##            break;
                    
        return
        
        
    def CrossReference_Jun28_2(self):
        words = self.LoadWords()
        self.GeneratePermutation_Jun28_2()
        
        #indexs = self.IndexPermutation()
        
        wordsDictionary = self.DictionaryOfWords()       
        
        for perm in self.permutations:
            if perm.lower() in wordsDictionary:
                print(perm + " in Dictionary " + "And permutation " + perm)
                
        return
        
    def CrossReference_Jun28_3(self):
        words = self.LoadWords()
        #self.GeneratePermutation_Jun28_3()
        
        indexs = self.IndexPermutation()
        
        print("indexed dictionary")
        
        chars =["b","r","u","i","s","e","d","l","o","f","t"]        
        
        count = 0
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9],chars[10]):
            if perm[:3] not in indexs:
                continue           
            startat = indexs[perm[:3]]
            count+=1
            if count % 1000 == 0:
                print(count)
            #for word in itertools.islice(words,startat,None):
            #    if perm[:8] == word[:8].lower():
            #        print("dictionary word " + word + " perumutatin is " + perm)                
            #    elif word[:3].lower() > perm[:3]:
            #        break
        
        
        
        
        #chars =["b","r","u","i","s","e","d","l","o","f","t"]

        
        #for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9],chars[10]):
        #    startat = indexs[perm[0].lower()]
        #    for word in itertools.islice(words,startat,len(words)-1) :           
        #        if perm[:7] == word[:7].lower():
        #            print("dictionary word " + word + " perumutatin is " + perm)
                
        #        if word[0] > perm[0]:
        #            break
        
        
        #chars =["b","r","u","i","s","e","d","l","o","f","t"]
        #wordsDictionary = self.DictionaryOfWords()       
     
        #for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9],chars[10]):
        #    if perm.lower() in wordsDictionary:            
        #        print(perm + " in Dictionary " + "And permutation " + perm)
                
        return
    
    def CrossReference_Jun29_1(self):
        words = self.LoadWords()
                
        #indexs = self.IndexPermutation()
        
       
        chars =["g","l","e","n","p","l","a","i","n"]
        
        
        wordsDictionary = self.DictionaryOfWords()       
        
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8]):
            if perm.lower() in wordsDictionary:            
                print(perm + " in Dictionary " + "And permutation " + perm)
                
        
        ##for perm in self.permutations:
        
        ##    startat = indexs[perm[0].lower()]
        
        ##    for word in itertools.islice(words,startat,len(words)-1):
        ##        if word[:7].lower() == perm[:7].lower():
        ##            print("Dictionary word is: " + word + " Permutation is: " + perm)
                    
        ##        if word[0] > perm[0]:
        ##            break;
                    
        return
        
    def CrossReference_Jun29_2(self):
        words = self.LoadWords()                       
        chars =["h","o","u","r","l","y","p","e","s","t"]                
        wordsDictionary = self.DictionaryOfWords()       
        
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9]):
            if perm.lower() in wordsDictionary:            
                print(perm + " in Dictionary " + "And permutation " + perm)                                  
        return
    
    def CrossReference_Jun29_3(self):
        words = self.LoadWords()                       
        chars =["p","a","n","i","c","h","e","l","p","e","d"]                
        wordsDictionary = self.DictionaryOfWords()       
        
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9],chars[10]):
            if perm.lower() in wordsDictionary:            
                print(perm + " in Dictionary " + "And permutation " + perm)                                  
        return
        
    def CrossReference_Jun30_1(self):
        words = self.LoadWords()                       
        #chars =["c","o","r","n","m","e","a","l","s]
        chars =["c","o","r","m","a"]
        wordsDictionary = self.DictionaryOfWords() 
        
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4]):
            if perm.lower() in wordsDictionary:            
                print(perm + " in Dictionary " + "And permutation " + perm)                                  
        return
    
        

    def CrossReference_Jun30_2(self):
        words = self.LoadWords()                       
        chars =["d","r","i","v","e","n","w","i","f","e"]                
        wordsDictionary = self.DictionaryOfWords()       
        
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9]):
            if perm.lower() in wordsDictionary:            
                print(perm + " in Dictionary " + "And permutation " + perm)                                  
        return
        
    def CrossReference_Jun30_3(self):
        words = self.LoadWords()                       
        chars =["t","r","i","m","t","h","e","l","e","g"]                
        wordsDictionary = self.DictionaryOfWords()       
        
        self.CrossReference_Jun30_3_Rec(wordsDictionary,chars,5,list())
        
        
        
        #for i in range(9):
        #    taken = []
        #    newchars = chars[:]
        #    taken.append(newchars[i])
        #    del newchars[i]
        
        #    for j in range(8):
        #        taken2 = taken[:]
        #        newchars2 = newchars[:]
        #        taken2.append(newchars2[j])
        #        del newchars2[j]
            
         #       for k in range(7):
         #           taken3 = taken2[:]
         #           newchars3 = newchars2[:]                
         #           taken3.append(newchars3[k])
         #           del newchars3[k]
                    
         #           for perm in self.GeneratePermutation(newchars3[0],newchars3[1],newchars3[2],newchars3[3],newchars3[4],newchars3[5]):
         #               if perm.lower() in wordsDictionary:            
         #                   print(perm + " in Dictionary " + "And permutation " + perm) 
         #                   #and print ident word for 3 chars
         #                   for perm2 in self.GeneratePermutation(taken3[0],taken3[1],taken3[2]):
         #                       if perm2.lower() in wordsDictionary:
         #                           print("\t" + perm2)
        
        #for i in range(9):
        #    for j in range(9):
        #        if j==i:
        #            break                
        #        newchars = chars[:]
        #        del newchars[i]
        #        del newchars[j]
        #        for perm in self.GeneratePermutation(newchars[0],newchars[1],newchars[2],newchars[3],newchars[4],newchars[5],newchars[6]):
        #            if perm.lower() in wordsDictionary:            
        #                print(perm + " in Dictionary " + "And permutation " + perm)                                  
        
        
        #for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4]):
        #    if perm.lower() in wordsDictionary:            
        #        print(perm + " in Dictionary " + "And permutation " + perm)                                  
        return

    def CrossReference_Jun30_3_Rec(self,recWordsDictionary,recChars,recSplitNum, recSplitVals):
        wordsDictionary = recWordsDictionary
        chars = recChars
        splitNum = recSplitNum
        splitVals = recSplitVals
        
        if splitNum == 0:
            for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4]):
                if perm.lower() in wordsDictionary:            
                    #print(perm + " in Dictionary " + "And permutation " + perm) 
                    t = []
                    #and print ident word for 3 chars
                    for perm2 in self.GeneratePermutation(splitVals[0],splitVals[1],splitVals[2],splitVals[3],splitVals[4]):
                        if perm2.lower() in wordsDictionary:
                            #print("\t" + perm2)
                            t.append(perm2)
                    
                    if len(t) > 0:
                        print(perm + " in Dictionary " + "And permutation " + perm)
                        print("\t",end="")
                        for str in t:
                            print(str+",",end="")
                        print("")
            return
    
        for i in range(len(chars)):
            newSplitVals = splitVals[:]
            newChars = chars[:]
            newSplitVals.append(newChars[i])
            del newChars[i]
            
            self.CrossReference_Jun30_3_Rec(wordsDictionary,newChars,splitNum-1, newSplitVals)
        
    def CrossReference_Jun30_3_Rec_2(self,recWordsDictionary,recChars,recSplitNum, recSplitVals):
        wordsDictionary = recWordsDictionary
        chars = recChars
        splitNum = recSplitNum
        splitVals = recSplitVals
        
        for i in range(len(chars)):
            newchars = chars[:]
            newchars.remove(newchars[i])
            #newchars.
        
            #CrossReference_Jun30_3_Rec_2
            
    def CrossReference_July04_1(self): 
        words = self.LoadWords()                       
        chars =["m","i","n","i","c","o","s","m","o","s"]                
        wordsDictionary = self.DictionaryOfWords()       
        
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9]):
            if perm.lower() in wordsDictionary:            
                print(perm + " in Dictionary " + "And permutation " + perm)                                  
        return
        
    def CrossReference_July04_2(self): 
        words = self.LoadWords()                       
        chars =["b","a","l","t","i","c","c","u","p"]        
        wordsDictionary = self.DictionaryOfWords()       
        
        self.CrossReference_July04_2_Rec(wordsDictionary,chars,6)
        return

    def CrossReference_July04_2_Rec(self,recWordsDictionary,recChars,recSplit):
        wordsDictionary = recWordsDictionary
        chars = recChars
        Split = recSplit
        count = 0
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8]):
            count += 1
            if count == math.factorial(len(chars)-Split):
                count = 0
                if perm[:Split] in wordsDictionary:
                    out = []
                    chars2 = perm[Split:]
                    for perm2 in self.GeneratePermutation(chars2[0],chars2[1],chars2[2]):
                        if perm2 in wordsDictionary:
                            out.append(perm2)
                    if len(out) > 0:
                        print(perm[:Split] + " dictionary permuation " + perm[:Split])
                        print("\t", end="")                        
                        for item in out:
                            if out.index(item) == (len(out)-1):
                                print(item,end="")
                            else:
                                print(item + ", ",end="")
                        print("")
                        
    def CrossReference_July04_3(self): 
        words = self.LoadWords()                       
        chars =["r","i","p","w","e","t","h","e","a","p"]                
        wordsDictionary = self.DictionaryOfWords()       
        
        self.CrossReference_July04_3_Rec(wordsDictionary,chars,5)
        return

    def CrossReference_July04_3_Rec(self,recWordsDictionary,recChars,recSplit):
        wordsDictionary = recWordsDictionary
        chars = recChars
        Split = recSplit
        count = 0
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9]):
            count += 1
            if count == math.factorial(len(chars)-Split):
                count = 0
                if perm[:Split] in wordsDictionary:
                    out = []
                    chars2 = perm[Split:]
                    for perm2 in self.GeneratePermutation(chars2[0],chars2[1],chars2[2],chars2[3],chars2[4]):
                        if perm2 in wordsDictionary:
                            out.append(perm2)
                    if len(out) > 0:                            
                        print(perm[:Split] + " dictionary permuation " + perm[:Split])
                        #print(out)
                        print("\t", end="")                        
                        for item in out:
                                print("(" +str(out.index(item))+")"+item + ", ",end="")                               
                        print("")
        
                                                           
    def CrossReference_July05_1(self): 
        words = self.LoadWords()                       
        chars =["n","a","t","a","l","m","a","i","d"]                
        wordsDictionary = self.DictionaryOfWords()       
        
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8]):
            if perm.lower() in wordsDictionary:            
                print(perm + " in Dictionary " + "And permutation " + perm)                                  
        return
        
    def CrossReference_July05_2(self): 
        words = self.LoadWords()                       
        chars =["o","p","e","n","a","i","r","m","a","n"]                
        wordsDictionary = self.DictionaryOfWords()       
        
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9]):
            if perm.lower() in wordsDictionary:            
                print(perm + " in Dictionary " + "And permutation " + perm)                                  
        return
               
    def CrossReference_July05_3(self):
        words = self.LoadWords()                       
        chars =["t","i","t","h","e","r","i","s","e","r","s"]            
        wordsDictionary = self.DictionaryOfWords()       
        
        self.CrossReference_July05_3_Rec(wordsDictionary,chars,6)
        return

    def CrossReference_July05_3_Rec(self,recWordsDictionary,recChars,recSplit):
        wordsDictionary = recWordsDictionary
        chars = recChars
        Split = recSplit
        count = 0
        for perm in self.GeneratePermutation(chars[0],chars[1],chars[2],chars[3],chars[4],chars[5],chars[6],chars[7],chars[8],chars[9],chars[10]):
            count += 1
            if count == math.factorial(len(chars)-Split):
                count = 0
                if perm[:Split] in wordsDictionary:
                    print(perm[:Split] + " dictionary permuation " + perm[:Split])
                     
        
    def IndexPermutation_OLD(self):
        indexs = {}
        
        words = self.LoadWords()
        
        lowercases = list(string.ascii_lowercase)
        
        for letter in lowercases:
            for word in words:
                if letter == word[0].lower():
                    indexs[letter] = words.index(word)
                    break               
        
        return indexs
        
    def IndexPermutation(self):
        indexs = {}
        
        words = self.LoadWords()                
        
        print("words length"+str(len(words)))
        
        lowercases = list(string.ascii_lowercase)
        
        alphabetIndexes = []
        
        for char in lowercases:
            for char2 in lowercases:
                for char3 in lowercases:
                    alphabetIndexes.append(char+char2+char3)                
                                  
        print("ok")
        
        quickIndex = 0
        for perm in alphabetIndexes:
            if alphabetIndexes.index(perm) % 100 == 0:
                print(alphabetIndexes.index(perm))
            for word in itertools.islice(words, quickIndex, None):
                if len(word) < 3:
                    continue
                elif perm < word[:3].lower():
                    break
                elif perm == word[:3].lower():
                    indexs[perm] = words.index(word)
                    quickIndex = words.index(word)
                    break

        return indexs
        
    def AlphabetIndexs(self):
        return
        
    def IndexWords(self):
        words = self.LoadWords()
        WordsIndex = {}
        lowercases = list(string.ascii_lowecase)
        
        return
        
    def DictionaryOfWords(self):
        words = self.LoadWords()
        wordsDictionary = {}
        for word in words:
            wordsDictionary[word.lower()] = 1
    
        return wordsDictionary
        
    def LoadWords(self):
        with open('words.txt') as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 
        
        #make lowercase
        content = [x.lower() for x in content]
        
        content.sort(key = str.lower)
        
        return content
        
    
        
mycrossword = MyCrossword()
mycrossword.CrossReference_July04_3()
