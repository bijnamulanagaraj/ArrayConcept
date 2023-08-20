from abc import ABC, abstractmethod


class learning(ABC):
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
    @abstractmethod
    def python(self):
        pass
    @abstractmethod
    def API(self):
        pass

class firstLanguage(learning):
    def python(self):
        print(self.name1)
    def API(self):
        print(self.name2)


firstLanguageObj = firstLanguage("python","API")
firstLanguageObj.python()
firstLanguageObj.API()




