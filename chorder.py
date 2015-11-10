#!/usr/bin/python

testdata = """
|--4-3-------------3-6--4--3-4------8-11---9--8--9-------6-9-8-6-8--4-|
|--6----6-5-6--2---2-5--6--5-6--6~--7-10--11-10-11--11~--4-8-9---9--4-|
|--5----6-5-6--3---3-6--5-------5~--8-11--10--------10~--6-8-8---8--5-|
|--3----8-7-8--3---2-5--3-------6~--7-10---8--------11~--5-8-6------4-|
|---------------------------------------------------------------------|
|---------------------------------------------------------------------|

|-4-8-6-4-6-----7----7----8---7-8/15~~-15-13--11-9---8-6-6--4---------|
|-6-6-6---6--8--8-10---8--8------------13-13--13-11--9-5-5--6---------|
|-5-6-6---6-----7---------9------------13-13--10-10--9-6-6--5---------|
|-6-6-5---5-----7---------10-----------15-15--11-11--8-5-5--3---------|
|-4-------------------------------------------------------------------|
|---------------------------------------------------------------------|

|-------------------1|------------------------------------------------|
|-8-6--4-2--1-1--1--1|---9-8-6-----------------------------------6---6|
|-5-5--5-3--1-3--3--1|---------5-----5-6-8-5-------------5---5-7---8--|
|-6-6--3-3--2-2--2--3|-----------6-8---------6-------5-7---8----------|
|------4----3-3--3--3|-------------------------7---8------------------|
|-------------------1v---------------------------8--------------------|"""

class TabReader:
    def __init__(self):
        self.data = None
        self.phrases = []
        self.pIndex = {}
    
    def read(self, tabData):
        self.data = tabData.split("\n")
        
        newPhrase = True
        
        for i in range(0, len(self.data) - 1):
            line = self.data[i].strip()
            if(line != ""):
                if(newPhrase):
                    self.phrases.append([line])
                    newPhrase = False
                else:
                    self.phrases[len(self.phrases) - 1].append(line)
            else:
                newPhrase = True

    def nextInPhrase(self, pId):
        offset = 0
        if(pId in self.pIndex):
            offset = self.pIndex[pId]
        
        #for i in range(offset, len(self.phrases[pId])):

    def readPos(self, pId, pos):
        l = []
        for i in range(0, len(self.phrases[pId]) - 1):
            try:
                s = int(self.phrases[pId][i][pos])
                
                sIdx = Fretboard.Strings[len(Fretboard.Strings) - 1 - i]
                #ch = Chord.calc
                l.append([sIdx, s])
            except:
                None
        return l        
class Scale:
    Notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    
class Fretboard:
    Strings = ["E2", "A2", "D3", "G3", "B3", "E4"]
    
class Chord:
    def __init__(self):
        self.id = 0
    
    def calc(self, root, adj):
        r = []
        r[:0] = root
        
        idx = Scale.Notes.index(r[0]) + adj
        
        #print(str(idx) + " : " + str(r))
        
        if(idx >= len(Scale.Notes)):
            r[1] = int(r[1]) + int(idx / len(Scale.Notes))
            r[0] = Scale.Notes[idx % len(Scale.Notes)]
        elif(idx < 0):
            r[1] = int(r[1]) - 1
            r[0] = Scale.Notes[idx % len(Scale.Notes)]
        else:
            r[0] = Scale.Notes[idx]
        
        return r
 
    def calcMusical(self, noteList):
        readReverse = True
        noteList = noteList[::-1]
        
        root = noteList[0]
        
        for n in noteList[1:]:
            interv = self.calcInterval(root, n)
            print(str(root) + ": " + str(n) + ": " + str(interv))
        
    def calcInterval(self, root, noteB):
        rPos = Scale.Notes.index(root[0])
        nPos = Scale.Notes.index(noteB[0])
        if(nPos < rPos):
            nPos += len(Scale.Notes)
        
        return nPos - rPos
        
tr = TabReader()

tr.read(testdata)

x = tr.readPos(0, 8)
c = Chord()

ch = []
for e in x:
    r = c.calc(e[0], e[1])
    ch.append(r)

c.calcMusical(ch)
    
print(tr.__dict__)

r = c.calc("C2", 4)
print(r)