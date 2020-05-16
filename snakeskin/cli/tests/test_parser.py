import unittest
from cli.parser import CommandParser
from cli import get_default_cli

class TestParser(unittest.TestCase):

  def test_load_empty(self):
    cli = get_default_cli()

    command_string = ""
    parser = CommandParser(command_string)
    

if __name__ == "main":
  unittest.main()
