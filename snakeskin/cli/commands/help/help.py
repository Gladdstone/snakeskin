from cli.commands.command import Command

class Help(Command):

  def __init__(self):
    super(self)
    self.help_content = self.read_file()

  def get_header(self):
    header = f"SNAKESKIN CLI v{__version__}\n\n"

  def execute(self):
    print(self.help)

  def read_file(self):
    content = self.get_header()

    help_file = open("help.txt", "r")
    for line in help_file:
      content = content + line

    return content
