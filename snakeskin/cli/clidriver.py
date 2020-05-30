import sys

class SnakeskinCli():

  def __init__(self, command_parser, command_loader):
    self.command_parser = command_parser
    self.command_loader = command_loader

  def get_cli_version(self):
    return self.__version__

  def process_input(self, args):
    self.command_parser.raw_args = args
    self.command_parser.load_commands()

    self.command_loader.command_table = self.command_parser.command_table
    self.command_loader.execute_command_table()
  

def main(args=None):
  snakeskin_cli = get_default_cli()
  print("cli objects created")

  if args is None:
    args = sys.argv[1:]
  snakeskin_cli.process_input(args)

def get_default_cli():
  from cli.parser import CommandParser
  from cli.loader import CommandLoader

  return SnakeskinCli(command_parser=CommandParser(),
      command_loader=CommandLoader())