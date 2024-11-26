from unittest import TestCase
from main import compute_lcs


class Test(TestCase):
    def test_compute_lcs(self):
        word1 = "horse"
        word2 = "ros"
        res = compute_lcs(word1, word2)
        assert (res == [
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,1,1],
                    [0,1,1,1],
                    [0,1,1,2],
                    [0,1,1,2]
                ])
