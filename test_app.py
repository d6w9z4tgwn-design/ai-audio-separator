import unittest
from app import command
class Test(unittest.TestCase):
 def test_command(self): self.assertEqual(command('a.wav','out')[-2:],['out','a.wav'])
