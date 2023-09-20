import unittest
import sys
import os

# Append the parent directory to the sys.path to access lib.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the module you want to test
import lib

class TestLibFunctions(unittest.TestCase):
    filepath = 'tables/cars.csv'  # Provide a test data file for testing
        
    def test_readfile(self):
        df = lib.readfile(self.filepath)
        self.assertIsNotNone(df)  # Check if df is not None

    def test_stats(self):
        df = lib.readfile(self.filepath)
        self.assertIsNotNone(df)

    def test_save_stats(self):
        df = lib.readfile(self.filepath)
        # Test saving summary stats and check if it returns a table string
        summary_table = lib.save_stats(df)

        # Check if the summary table string is not empty
        self.assertNotEqual(summary_table, "")
    
    def test_visualize_cars(self):
        df = lib.readfile(self.filepath)
        fig = lib.visualize_cars(df)
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()
