#!/usr/bin/env python
# coding: utf-8

# In[4]:


# problem 1 

from abc import ABC, abstractmethod, abstractproperty


class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

    def draw(self):
        return 'I can draw a circle'


class Square(Shape):

    def draw(self):
        return 'I can draw a square'


class Triangle(Shape):

    def draw(self):
        return 'I can draw a triangle'


class ShapeFactory:
    SHAPES = {
        'circle': Circle,
        'square': Square,
        'triangle': Triangle,
    }


    @staticmethod
    def build(shape):
        return ShapeFactory.SHAPES[shape]()


class Client:

    @staticmethod
    def draw(shape):
        factory = ShapeFactory().build(shape)

        return factory.draw()


client = Client()
print(client.draw('square'))


# In[3]:


# problem 2
class Button(ABC):

    @abstractmethod
    def on_down(self):
        pass

    @abstractmethod
    def on_up(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def on_change(self):
        pass


class WinButton(Button):

    def on_down(self):
        return 'Win button is pressed'

    def on_up(self):
        return 'Win button is pressed'

    def draw(self):
        return 'Win button drawing...'


class MacButton(Button):

    def on_down(self):
        return 'Mac button is pressed'

    def on_up(self):
        return 'Mac button is pressed'

    def draw(self):
        return 'Mac button drawing...'


class WinCheckbox(Checkbox):

    def on_change(self):
        return 'Win checkbox changed'


class MacCheckbox(Checkbox):

    def on_change(self):
        return 'Mac checkbox changed'


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(GUIFactory):

    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Application:

    def __init__(self, f):
        self.factory = f

    def createUI(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        draw1 = self.button.draw()
        change = self.checkbox.on_change()
        draw2 = self.button.draw()

        return [draw1, change, draw2]


winApp = Application(WinFactory())
winApp.createUI()

macApp = Application(MacFactory())
macApp.createUI()

print(winApp.paint())
print(macApp.paint())


# In[7]:


class AbstractBuilder(ABC):

    @abstractmethod
    def create_id(self, id):
        pass

    @abstractmethod
    def create_balance(self, balance):
        pass

    @abstractmethod
    def create_rate(self, rate):
        pass


class BankAccount():

    def __init__(self):
        self.attributes = {}

    def add(self, key, value):
        self.attributes[key] = value

    def describe(self):
        print(self.attributes)


class BankAccountBuilder(AbstractBuilder):

    def __init__(self):
        self.bank_account = BankAccount()

    def create_id(self, id):
        self.bank_account.add('id', id)

    def create_balance(self, balance):
        self.bank_account.add('balance', balance)

    def create_rate(self, rate):
        self.bank_account.add('rate', rate)


builder = BankAccountBuilder()
builder.create_id(10988768)
builder.create_balance(45000.0)
builder.create_rate(4.2)
builder.bank_account.describe()

builder = BankAccountBuilder()
builder.create_id('138499')
builder.create_balance(3500000.0)
builder.bank_account.describe()

