class SnakeskinCli():

  def __init__(self, command_parser, command_loader):
    command_parser = command_parser
    command_loader = command_loader

  def get_cli_version(self):
    return __version__
  

def main():
  snakeskin_cli = get_default_cli()
  print("cli objects created")

def get_default_cli():
  from cli.parser import CommandParser
  from cli.loader import CommandLoader

  return SnakeskinCli(command_parser=CommandParser,
      command_loader=CommandLoader)