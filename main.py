import sys

def getBin(num, length):
  return format(num, '0{}b'.format(int(length)))

def getInt(bin):
  return int(bin, 2)

class bin:
  def __init__(self, words=None, readables=None):
    self.words = []

    if words != None:
      for i in range(len(words)):
        self.words.append([getInt(words[i]), readables[i], len(words[i])])

  def __getitem__(self, i):
    return self.words[i]
    
  def printAsBin(self):
    for word in self.words:
      sys.stdout.write(getBin(word[0], word[2])+" ")
    print("")

  def printAsReadable(self):
    for word in self.words:
      sys.stdout.write(word[1]+" ")
    print("")

  def addWord(self, word, readable):
    self.words.append([getInt(word), readable, len(word)])

class stack:
  def __init__(self):
    self.queue = []
  
  def push(self, val):
    self.queue.append(val)
  def pull(self):
    n = self.queue[len(self.queue)-1]
    self.queue.remove(len(self.queue)-1)
    return n

code = input("code: ")

# get binary of code, like ingame
bfCode = bin()
for char in code:
  if char == ".":
    bfCode.addWord("001", "OUT")
  elif char == ">":
    bfCode.addWord("010", "RIGHT")
  elif char == "<":
    bfCode.addWord("011", "LEFT")
  elif char == "+":
    bfCode.addWord("100", "ADD")
  elif char == "-":
    bfCode.addWord("101", "SUB")
  elif char == "[":
    bfCode.addWord("110", "OPEN")
  elif char == "]":
    bfCode.addWord("111", "CLOSE")

# COMPILATION

# for cell argument of instruction
cell = 0

# for brackets
brackets = stack()

# for add/sub calls
n = 0
add = True

cells = []

for word in bfCode:
  if word[1] == "OUT":
    code.append(bin())