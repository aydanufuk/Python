from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class Hp(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling on Hp laptop")


class Dell(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling on Dell laptop")


class HpNotebook(Hp):

    def click(self):
        print("Clicking on Hp Notebook")



class DellNotebook(Dell):

    def click(self):
        print("Clicking on Dell Notebook")

hpNotebook = HpNotebook()
hpNotebook.scroll()
hpNotebook.click()

dellNotebook = DellNotebook()
dellNotebook.scroll()
dellNotebook.click()