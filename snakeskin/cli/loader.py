class CommandLoader():

  def __init__(self):
    self._command_table = {}

  @property
  def command_table(self):
    return self._comand_table

  @command_table.setter
  def command_table(self, arg):
      self._command_table = arg

  def execute_command_table(self):
    if self._command_table["options"]:
      self._command_table["options"].execute()
  