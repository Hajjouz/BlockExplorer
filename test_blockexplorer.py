# test_blockexplorer.py
"""
Tests for BlockExplorer module.
"""

import unittest
from blockexplorer import BlockExplorer

class TestBlockExplorer(unittest.TestCase):
    """Test cases for BlockExplorer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockExplorer()
        self.assertIsInstance(instance, BlockExplorer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockExplorer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
