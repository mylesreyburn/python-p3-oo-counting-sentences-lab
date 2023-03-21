#!/usr/bin/env python3

class MyString:

  def __init__(self, value = None) -> None:
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if value == None:
      self._value = ""
    elif type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
      self._value = False

  value = property(get_value, set_value,)

  def is_sentence(self):
    split_value = [letter for letter in self.value]
    if split_value[-1] == ".":
      return True
    else:
      return False
    
  def is_question(self):
    split_value = [letter for letter in self.value]
    if split_value[-1] == "?":
      return True
    else:
      return False
    
  def is_exclamation(self):
    split_value = [letter for letter in self.value]
    if split_value[-1] == "!":
      return True
    else:
      return False
    
  def count_sentences(self):
    listed_words = self.value.split()
    sentences = 0
    for word in listed_words:
      word_letters = [letter for letter in word]
      if word_letters[-1] == "." or word_letters[-1] == "?" or word_letters[-1] == "!":
        sentences += 1
    return sentences

cungadero = MyString("stringy bingy bing bang bong! boom!! bababooie? ratatouille...")
cungadero.count_sentences()
