import sys

class bin:
  def __init__(self, word, readable):
    self.words = []
    self.words.append([word, readable])
  
  def printAsBin(self):
    for word in self.words:
      sys.stdout.write(word[0]+" ")
    print("")

  def printAsReadable(self):
    for word in self.words:
      sys.stdout.write(word[1]+" ")
    print("")

  def addWord(self, word, readable):
    self.words.append([word, readable])