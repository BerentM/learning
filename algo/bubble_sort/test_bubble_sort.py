import unittest

from .bubble_sort import sort


# create unittests for bubble_sort function
class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        assert sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert sort([3, 5, 2, 4, 1]) == [1, 2, 3, 4, 5]
        assert sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
        assert sort([1]) == [1]
        assert sort([]) == []
