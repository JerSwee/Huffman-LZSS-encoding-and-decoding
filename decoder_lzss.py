import sys

DICT_SIZE = 6
BUFFER_SIZE = 4





def recursive_decode(s, n):


    if s[0]=="1":
        decimalVal = '0b' + s[0:n] 
        decimalVal = int(decimalVal,2)
        return (decimalVal,s[n:])


    if n == 1:

        b = s[0]
        b = b.replace("0","1",1)
        n = 1+int(b)

        return recursive_decode(s[1:],n)


    if s[0]=="0":
        b = str(s[0:n])
        b = b.replace("0","1",1)
        decimalVal = '0b' + b 
        decimalVal = int(decimalVal,2)
        m = decimalVal + 1
        return recursive_decode(s[n:],m)




def elias_decode(s):
    return recursive_decode(s, 1) #set readlen to 1



def ascii_decode(aString):
    # Get the calue of character from the ascii encoding
    numberstr = '0b'+ aString
    numberstr = int(numberstr,2)
    charValue = chr(numberstr)
    return(charValue)

class LZSS_decoder:
    
    def __init__(self,initialString,codeList):
        self.tuplesList = []
        self.string = initialString
        self.codes = codeList
        
    def start_decode(self,aString): #get triplets
        
        i=0
        lengthString = len(aString)
        currentDict = ''
        currentBuffer = ''
        windowSize = DICT_SIZE + BUFFER_SIZE
        while i<len(aString):

            currentChar = aString[i]

            if i == 0:
                bit = '1'
                for code in self.codes:
                    hmanIndex = aString.index(code[1])
                    if hmanIndex == i + 1:
                        char = code[1]
                        self.tuplesList.append((bit,char))
                        i +=len(char)+1
                        break
            
            
            if i < DICT_SIZE:
                currentDict = aString[0:i]
            else:
                currentDict = aString[i-DICT_SIZE:i]

            if i + BUFFER_SIZE < lengthString:
                currentBuffer = aString[i:i+BUFFER_SIZE]
            else:
                currentBuffer = aString[i:lengthString]

            currentLCS = self.getLCS(currentDict,currentBuffer,len(currentDict),len(currentBuffer))
            '''
            if len(currentLCS) < 3:
                a = 1
                #self.tuplesList.append((bit,char))
            else:
                bit = "0"
            '''


           
            return
	
    def getLCS(self, X, Y, lenX, lenY):
 

        return
 

if __name__ == "__main__":
    charsList = []
    
    f = open (sys.argv[1],"r") 
    inputStr = f.read()
    f.close()
 

    totalUnique = elias_decode(inputStr)[0]

    inputStr = inputStr[totalUnique:]

    for i in range (0,totalUnique): #loop for the number of unique chars to decode the header
        currentAscii = inputStr[0:7]
        currentChar = ascii_decode(currentAscii)
        inputStr = inputStr[7:]
        lenHmancode = elias_decode(inputStr)
        inputStr = lenHmancode[1]
        currentCode = inputStr[0:int(lenHmancode[0])]
        charsList.append((currentChar,currentCode))
        inputStr = inputStr[len(currentCode):]
    

    totalFields = elias_decode(inputStr) #begin decoding data portion
    inputStr = totalFields[1]
    lzss = LZSS_decoder(inputStr,charsList)
    lzss.start_decode(lzss.string)



