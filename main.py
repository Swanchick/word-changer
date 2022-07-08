from pynput.keyboard import Listener, Key
from appscript import app
from json import load

class WordChanger:
    text: str = ""
    words: dict = {}

    def change_word(self, word: str, change: str):
        for i in range(len(word)):
            app("System Events").key_code(51)

        app("System Events").keystroke(change)

    def check_word(self):
        for word in list(self.words.keys()):
            if not word in self.text: continue

            self.change_word(word, self.words[word])

    def on_press(self, key):
        latter = str(key).replace("'", "")
        
        if len(latter) > 1: 
            if key == Key.space:
                self.text += " "
            elif key == Key.backspace:
                self.text = self.text[:-1]
            elif key == Key.enter:
                self.text = ""

            return

        self.text += latter

        self.check_word()

    def load(self):
        f = open("words.json", "r")
        self.words = load(f)
        f.close()

    def start(self):
        self.load()

        with Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    word_changer = WordChanger()

    word_changer.start()
