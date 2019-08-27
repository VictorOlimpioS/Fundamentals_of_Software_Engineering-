import json
import subprocess as s
import sys

class Chatbot():
    def __init__(self,name):
        try:
            memory = open(name + '.json','r')
        except FileNotFoundError:
            memory = open(name + '.json','w')
            memory.write('["Vcitor","Jones"]')
            memory = open(name + '.json','r')
        self.name = name
        self.known = json.load(memory)
        memory.close()
        self.history = [None]
        self.phrases = {'hi': 'Hi, what is your name?', 'bye':'bye'}
 
    
    def listenTo (self,phrase=None):
        if phrase == None:
            phrase = input('You: ' )
        phrase = str(phrase)
        if 'run ' in phrase:
            return phrase
        phrase = phrase.lower()
        #phrase = phrase.replace('é', 'eh')
        return phrase
    
    def think(self, phrase):
        if phrase in self.phrases:
            return self.phrases[phrase]
        if phrase == 'catch it':
            return 'write the sentence: '
            
        lastSentence = self.history[-1]
        if lastSentence == "Hi, what is your name?":
            name = self.getName(phrase)
            phrase = self.asnwerName(name)
            return phrase
        if lastSentence == 'write the sentence: ':
            self.key = phrase
            return 'write the answer: '
        if lastSentence == 'write the answer: ':
            asw= phrase
            self.phrases[self.key] = asw
            self.recordMemory()
            return 'Got it '

        try:
            resp = str(eval(phrase))
            return resp
        except:
            pass
        return "Sorry, i didn't understand"

    def getName(self,name):
        if 'my name is ' in name:
            name = name[11:]
        name = name.title()
        return name
    
    def asnwerName(self,name):
        if name in self.known:
            phrase = 'Hey '
        else:
            phrase = 'Nice to meet you '
            self.known.append(name)
            self.recordMemory()
        return phrase + name

    def recordMemory(self):
        memory = open(self.name + '.json', 'w')
        json.dump(self.known,memory)
        memory.close()

    
    def speak(self,phrase):
        if 'run' in phrase:
            platform = sys.platform
            command = phrase.replace('run ', '')
            if 'win' in platform:
                os.startfile(command)
            if 'linux' in platform:
                try:
                    s.Popen(command)
                except FileNotFoundError:
                    s.Popen([ 'xdg-open',command])
        else: 
            print(phrase)
        self.history.append(phrase)




