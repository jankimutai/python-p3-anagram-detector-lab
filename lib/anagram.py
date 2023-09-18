# your code goes here!
class Anagram:
    
    def __init__(self,my_list):
        self.my_list = my_list
        
    def match(self,my_lists):
        my_data = []
        for letter in my_lists:
            if sorted(letter) == sorted(self.my_list) and letter != self.my_list:
                my_data.append(letter)
        return (my_data)
    
       

listen = Anagram('listen')
listen.match(['enlists', 'google', 'inlets', 'banana'])
