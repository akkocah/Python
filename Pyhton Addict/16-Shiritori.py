class Shiritori:
    def __init__(self):
        self.game_over = False
        self.words = []
    def play(self, word):
        if len(self.words) == 0 or self.words[-1][-1] == word[0]  and word not in self.words :
            self.words.append(word)
            return print(self.words)
        self.game_over = True
        return print('game over')
    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'

my_shiritori = Shiritori()
my_shiritori.play("apple") 
my_shiritori.play("ear") 
my_shiritori.play("rhino") 
my_shiritori.play("corn") 
