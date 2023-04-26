import unittest
import src.dec_2_hex as dh


class DecimalTestCase(unittest.TestCase):
    def test_dec2hexa1(self):
        answer = dh.dec_to_hex(1024)
        self.assertEqual(answer, '400')

    def test_dec2hexa2(self):
        answer = dh.dec_to_hex(123456789)
        self.assertEqual(answer, '75BCD15')


if __name__ == '__main__':
    unittest.main()
