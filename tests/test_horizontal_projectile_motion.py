import unittest
from unittest.mock import patch

import app_functions


class HorizontalProjectileMotionTestCase(unittest.TestCase):
    @patch('builtins.input', lambda _: '15.7')
    def test_read_data_start_height(self):
        result = app_functions.read_data('Podaj wysokość początkową (w m): ', 10)

        self.assertEqual(result, 15.7)

    @patch('builtins.input', lambda _: '17.9')
    def test_read_data_start_velocity(self):
        result = app_functions.read_data('Podaj prędkość początkową (w m/s): ', 2)

        self.assertEqual(result, 17.9)


if __name__ == '__main__':
    unittest.main()
