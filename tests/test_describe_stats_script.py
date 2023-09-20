import unittest
from unittest.mock import patch

# Add the parent directory to the sys.path to access describe_stats_script
sys.path.append("..")

from describe_stats_script import full_describe

class TestDescribeStatsScript(unittest.TestCase):

    @patch('lib.readfile')
    @patch('lib.stats')
    @patch('lib.save_stats')
    @patch('lib.visualize_cars')
    def test_full_describe_returns_0(self, *_):
        # Call the full_describe function and check if it returns 0
        result = full_describe("tables/cars.csv")  # Replace with a test file path
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()