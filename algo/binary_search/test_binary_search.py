import unittest

from binary_search import search


class TestSearch(unittest.TestCase):
    def test_search(self):
        assert search([], 1) == -1
        assert search([1], 1) == 0
        assert search([1, 2, 3, 4, 5], 3) == 2
        assert search([1, 2, 3, 4, 5], 6) == -1
        assert search([1, 2, 3, 4, 5], 0) == -1
        assert search([1, 2, 3, 4, 5], 1) == 0
        assert search([1, 2, 3, 4, 5], 5) == 4
        assert search([1, 2, 3, 4, 5], 2) == 1
        assert search([1, 2, 3, 4, 5], 4) == 3
        assert search([1, 2, 3, 4, 5], 3) == 2
        assert search([1, 2, 3, 4, 5], 1) == 0
        assert search([1, 2, 3, 4, 5], 5) == 4
        assert search([1, 2, 3, 4, 5], 0) == -1
        assert search([1, 2, 3, 4, 5], 6) == -1
        assert search([1, 2, 3, 4, 5], 2) == 1
        assert search([1, 2, 3, 4, 5], 4) == 3
        assert search([1, 2, 3, 4, 5], 3) == 2
        assert search([1, 2, 3, 4, 5], 1) == 0
        assert search([1, 2, 3, 4, 5], 5) == 4
        assert search([1, 2, 3, 4, 5], 0) == -1
        assert search([1, 2, 3, 4, 5], 6) == -1

    def test_search_letters(self):
        assert search(["a", "b", "c", "d", "e"], "c") == 2
        assert search(["a", "b", "c", "d", "e"], "f") == -1
        assert search(["a", "b", "c", "d", "e"], "a") == 0
        assert search(["a", "b", "c", "d", "e"], "e") == 4
        assert search(["a", "b", "c", "d", "e"], "b") == 1
        assert search(["a", "b", "c", "d", "e"], "d") == 3
