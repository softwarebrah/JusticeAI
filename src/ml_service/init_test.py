import os
import unittest
from util.constant import Path


class TestInitScript(unittest.TestCase):
    def test_init(self):
        import init
        self.assertTrue(os.path.isfile(Path.binary_directory + 'non-lem.bin'))