import unittest
from kalkulacka import Kalkulacka

class KalkulackaTestCase(unittest.TestCase):

    def setUp(self):
        self.kalkulacka = Kalkulacka()

    def test_scitani(self):
        self.assertEqual(5, kalkulacka.scitani(2, 3))


if __name__ == '__main__':
    unittest.main()
