class CommandParser:

  def __init__(self, command_string):
    self.command_string = command_string

  def load_commands(self):
    command_table = {}
    
    command_arr = self.command_string.split(" ")
    previous_cmd_marker = ""
    for cmd in command_arr:
      if cmd[0] == "-" and command_table.get(cmd) == None:
        command_table[cmd] = ""   # TODO - updateable parameter class?
        previous_cmd_marker = cmd
      else:
        command_table[previous_cmd_marker] = cmd
