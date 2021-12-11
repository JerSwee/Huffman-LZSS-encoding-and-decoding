import sys
import heapq



class HuffmanCode:
	def __init__(self):
		self.heap = []
		self.hmanCodes = {}

	class Node: #leaf node for tree 
		def __init__(self, val, total):
			self.char = val
			self.total = total #total frequency
			self.left = None
			self.right = None

		#set comparisons to compare frequencies properly when comparing nodes
		def __eq__(self, aNode):
			if(aNode == None):
				return False
			if(not isinstance(aNode, Node)):
				return False
			return self.total == aNode.total

		def __lt__(self, aNode):
			return self.total < aNode.total

		


	def get_frequency(self, text): #create list of frequencies
		freqList = {}
		for char in text:
			if not char in freqList:
				freqList[char] = 0
			freqList[char] += 1
            
		return freqList



	def set_heap(self, freqList): #create heap from frequency list
            for char in freqList:
                node = self.Node(char, freqList[char])
                heapq.heappush(self.heap, node)


	def traverse_tree(self, aNode, code): #do root to leaf traversal
		if(aNode == None):
			return

		if(aNode.char != None):
			self.hmanCodes[aNode.char] = code #build up codes through traversal
			return

		#assign bit symbols to branches
		self.traverse_tree(aNode.left, code + "0")
		self.traverse_tree(aNode.right, code + "1")


	def join_nodes(self):
		
		while(len(self.heap)>1): #Join 2 nodes with the smallest frequencies 

			lNode = heapq.heappop(self.heap)
			rNode = heapq.heappop(self.heap)

			newNode = self.Node(None, rNode.total+ lNode.total )
			newNode.left = lNode
			newNode.right = rNode

			heapq.heappush(self.heap, newNode)




	def get_code(self):
		rootNode = heapq.heappop(self.heap) #start with smallest node
		current_code = ""
		self.traverse_tree(rootNode, current_code) 



	def compute_codes(self,text):
		frequency = self.get_frequency(text)
		self.set_heap(frequency)
		self.join_nodes()
		self.get_code()




        
#Elias Omega
def recursive_elias(n): #get elias integer code recursively
    s = ""
    if n>1:
        b = bin(n)[2:]
        stringb = str(b)
        b = stringb.replace("1","0",1)
        s += recursive_elias(len(b)-1) + b
    
    if n == 1:
        s+= "0"
    return s

def EliasEncode(n):

    b = bin(n)[2:]
    n = len(b)-1
    
    return recursive_elias(n)+b





def asciiCode(ch): #get ascii code of a character

    asci = ord(ch)
    return bin(asci)[2:]





if __name__ == "__main__":

	
		

		f = open (sys.argv[1],"r") 
		inputString = f.read()
		f.close()
		headerString = ''
		
		hmanEncode = HuffmanCode() #initialize and get unique chars
		hmanEncode.compute_codes(inputString)
		uniqueChars = EliasEncode(len(hmanEncode.hmanCodes))

		headerString += uniqueChars
		print(hmanEncode.hmanCodes)
		for char in hmanEncode.hmanCodes: #encode accordingly for every unique character
			headerString += asciiCode(char)
			headerString += EliasEncode(len(hmanEncode.hmanCodes[char]))
			headerString += hmanEncode.hmanCodes[char]
		f = open("output_header.txt", "w")
		f.write(headerString)
		#write to file
			





    
