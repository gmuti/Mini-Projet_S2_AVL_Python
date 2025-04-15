import unittest
from avl import AVL, to_str, lr, rr, lrr, rlr

class TestNewAVL(unittest.TestCase):
    """Tests for the new AVL implementation."""
    
    def test_creation(self):
        """Test AVL node creation."""
        # Create a simple AVL tree
        #      5(0)
        #     /   \
        #  2(-1)   8(0)
        #  /
        # 1(0)
        leaf1 = AVL(1, None, None, 0)
        leaf8 = AVL(8, None, None, 0)
        node2 = AVL(2, leaf1, None, -1)
        root = AVL(5, node2, leaf8, 0)
        
        # Check node values
        self.assertEqual(root.key, 5)
        self.assertEqual(root.bal, 0)
        self.assertEqual(root.left.key, 2)
        self.assertEqual(root.right.key, 8)
        
    def test_to_str(self):
        """Test string representation."""
        # Create a simple AVL tree
        leaf1 = AVL(1, None, None, 0)
        leaf8 = AVL(8, None, None, 0)
        node2 = AVL(2, leaf1, None, -1)
        root = AVL(5, node2, leaf8, 0)
        
        # Get string representation
        tree_str = to_str(root)
        
        # Check that all nodes are in the string
        self.assertIn("5 (0)", tree_str)
        self.assertIn("2 (-1)", tree_str)
        self.assertIn("1 (0)", tree_str)
        self.assertIn("8 (0)", tree_str)
        
    def test_left_rotation(self):
        """Test left rotation (lr)."""
        # Create a tree that needs left rotation
        #    1(0)                 2(0)
        #     \                  / \
        #     2(0)      ->     1(0) 3(0)
        #      \
        #      3(0)
        leaf3 = AVL(3, None, None, 0)
        node2 = AVL(2, None, leaf3, 0)
        root = AVL(1, None, node2, 0)
        
        # Apply left rotation
        new_root = lr(root)
        
        # Check the new structure
        self.assertEqual(new_root.key, 2)
        self.assertEqual(new_root.left.key, 1)
        self.assertEqual(new_root.right.key, 3)
        
    def test_right_rotation(self):
        """Test right rotation (rr)."""
        # Create a tree that needs right rotation
        #      3(0)              2(0)
        #     /                 / \
        #    2(0)      ->     1(0) 3(0)
        #   /
        #  1(0)
        leaf1 = AVL(1, None, None, 0)
        node2 = AVL(2, leaf1, None, 0)
        root = AVL(3, node2, None, 0)
        
        # Apply right rotation
        new_root = rr(root)
        
        # Check the new structure
        self.assertEqual(new_root.key, 2)
        self.assertEqual(new_root.left.key, 1)
        self.assertEqual(new_root.right.key, 3)
        
    def test_left_right_rotation(self):
        """Test left-right rotation (lrr)."""
        # Create a tree that needs left-right rotation
        #    3(0)                 2(0)
        #   /                    / \
        #  1(0)       ->       1(0) 3(0)
        #   \
        #    2(0)
        leaf2 = AVL(2, None, None, 0)
        node1 = AVL(1, None, leaf2, 0)
        root = AVL(3, node1, None, 0)
        
        # Apply left-right rotation
        new_root = lrr(root)
        
        # Check the new structure
        self.assertEqual(new_root.key, 2)
        self.assertEqual(new_root.left.key, 1)
        self.assertEqual(new_root.right.key, 3)
        
    def test_right_left_rotation(self):
        """Test right-left rotation (rlr)."""
        # Create a tree that needs right-left rotation
        #  1(0)                 2(0)
        #   \                  / \
        #    3(0)     ->     1(0) 3(0)
        #   /
        #  2(0)
        leaf2 = AVL(2, None, None, 0)
        node3 = AVL(3, leaf2, None, 0)
        root = AVL(1, None, node3, 0)
        
        # Apply right-left rotation
        new_root = rlr(root)
        
        # Check the new structure
        self.assertEqual(new_root.key, 2)
        self.assertEqual(new_root.left.key, 1)
        self.assertEqual(new_root.right.key, 3)

if __name__ == "__main__":
    unittest.main()