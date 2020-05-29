from cli.arguments import Arguments
from cli.commands.help.help import Help

class CommandParser:

  def __init__(self):
    self.raw_args = []
    self.command_table = {}

  def set_arg(self, raw_args):
    self.raw_args = raw_args

  def load_commands(self):    
    if len(self.raw_args) < 1:
      return  # TODO - error handler (invalid arg count error)

    for cmd in self.raw_args:
      if cmd[0] != "-":
        return
      option = self.get_command(cmd)
      if option == None:
        return  # TODO - invalid option input error
      self.command_table["options"] = option

    # previous_cmd_marker = ""
    # for cmd in self.raw_args:
    #   if cmd[0] == "-" and self.command_table.get(cmd) == None:
    #     arg = self.get_command(cmd)
    #     self.command_table[arg] = ""
    #     previous_cmd_marker = arg
    #   else:
    #     self.command_table[previous_cmd_marker] = cmd

    self.print_command_table()
  
  def get_command(self, command):
    command_switch = {
      "--help": Help(),
      "--name": "ami_name",
      "--type": "type",
      "--version": "version"
    }

    return command_switch.get(command)

  def print_command_table(self):
    for key in self.command_table:
      print(key, "->", self.command_table[key])
