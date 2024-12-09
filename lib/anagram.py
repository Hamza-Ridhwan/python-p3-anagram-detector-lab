# your code goes here!
class Anagram:
    def __init__ (self, word):
        self.word = word
    
    def match(self, words):
        return [sim_word for sim_word in words if sorted(sim_word) == sorted(self.word)]

        # for sim_word in words:
        #     if sorted(sim_word) == sorted(self.word):
        #         return sim_word



anagram = Anagram('liten')
print(anagram.match(['enlists', 'google', 'inlets', 'banana']))

