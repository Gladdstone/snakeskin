import os

from cli.commands.command import Command

class Help(Command):

  def __init__(self):
    Command.__init__(self, "help")
    self.help_content = self.read_file()

  def get_header(self):
    header = f"SNAKESKIN CLI v0.0\n\n"    # TODO - dynamic versioning
    return header

  def execute(self):
    print(self.help_content)

  def read_file(self):
    content = self.get_header()

    cur_path = os.path.dirname(__file__)
    help_path = os.path.join(cur_path, "../../../", "doc/assets", "help.txt")   # TODO - create env variable

    with open(help_path, "r") as help_file:
      for line in help_file:
        content = content + line

    return content
