class Arguments():
  
  def __init__(self, name):
    self.name = name

  @property
  def parameter(self, arg):
    return self.__parameter

  @parameter.setter
  def parameter(self, arg):
    self.__parameter = arg

  @property
  def required(self):
    return self.__required

  @required.setter
  def required(self):
    self.required = False

  @property
  def multi_input(self):
    raise NotImplementedError

  @multi_input.setter
  def multi_input(self, args):
    raise NotImplementedError

class RequiredArgument(Arguments):

  def __init__(self):
    super(self)

  @property
  def required(self):
    return self.__required

  @required.setter
  def required(self):
    self.required = True
