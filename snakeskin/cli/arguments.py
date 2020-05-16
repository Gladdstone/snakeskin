class Arguments():
  
  def __init__(self, name):
    self.name = name

  @property
  def required(self):
    return self.__required

  @property
  def multi_input(self):
    return self.multi_input

  @multi_input.setter
  def multi_input(self, args):
    self.multi_input = args
