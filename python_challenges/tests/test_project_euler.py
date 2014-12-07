__author__ = 'tilmannbruckhaus'

import unittest
from project_euler.problem_1 import SumOfMultiples
from project_euler.problem_2 import Fibonacci
from project_euler.problem_3 import LargestPrimeFactor
from project_euler.problem_4 import LargestPalindrome
from project_euler.problem_5 import SmallestMultiple
from project_euler.problem_6 import SumSquareDifference
from project_euler.problem_7 import TenThousandFirstPrime
from project_euler.problem_8 import LargestProductInSeries
from project_euler.problem_9 import SpecialPythagoreanTriplet
from project_euler.problem_10 import SummationOfPrimes
from project_euler.problem_11 import LargestProductInAGrid
from project_euler.problem_12 import HighlyDivisible
from project_euler.problem_13 import LargeSum
from project_euler.problem_14 import LongestCollatzSequence
from project_euler.problem_15 import LatticePaths
from project_euler.problem_16 import PowerDigitSum
from project_euler.problem_17 import NumberLetterCounts


class TestProjectEuler(unittest.TestCase):
    def test_problem1(self):
        fixtures = [[10, 23], [100, 2318], [1000, 233168]]
        for fixture in fixtures:
            self.assertEquals(fixture[1], SumOfMultiples.sum_of_multiples_of_3_or_5(fixture[0]))

    def test_problem2(self):
        self.assertEquals(4613732, Fibonacci().even_sum(4000000))

    def test_problem_3(self):
        fixtures = [[2, 1],
                    [3, 1],
                    [4, 2],
                    [7, 1],
                    [15, 5],
                    [44, 11],
                    [99, 11],
                    [111, 37],
                    [1577, 83],
                    [19 * 37 * 83, 83],
                    [600851475143, 6857]]

        for fixture in fixtures:
            self.assertEquals(fixture[1], LargestPrimeFactor.find(fixture[0]))

    def test_problem_4(self):
        fixtures = [[1, 9], [2, 9009], [3, 906609]]
        for fixture in fixtures:
            self.assertEquals(fixture[1], LargestPalindrome.find(fixture[0]))

    def test_problem_5(self):
        self.assertEquals(232792560, SmallestMultiple.find())

    def test_problem_6(self):
        self.assertEquals(25164150, SumSquareDifference.find())

    def test_problem_7(self):
        self.assertEquals(104743, TenThousandFirstPrime.find())

    def test_problem_8(self):
        self.assertEquals(23514624000, LargestProductInSeries.find())

    def test_problem_9(self):
        self.assertEquals((200, 375, 425), SpecialPythagoreanTriplet.find())

    def test_problem_10(self):
        self.assertEquals(142913828922, SummationOfPrimes().find())

    def test_problem_11(self):
        self.assertEquals(70600674, LargestProductInAGrid().find())

    def test_problem_12(self):
        h = HighlyDivisible
        self.assertEquals([[2, 2], [7, 1]], h.factor(28))
        self.assertEquals(6, h.num_divisors([[2, 2], [7, 1]]))
        self.assertEquals(28, h.find(5))
        self.assertEquals([[17, 1]], h.factor(17))
        self.assertEquals(2, h.num_divisors([[17, 1]]))
        self.assertEquals([[5, 2]], h.factor(25))
        self.assertEquals(3, h.num_divisors([[5, 2]]))
        self.assertEquals([[2, 2], [3, 1], [5, 1]], h.factor(60))
        self.assertEquals(12, h.num_divisors([[2, 2], [3, 1], [5, 1]]))
        self.assertEquals([[2, 2], [5, 2]], h.factor(100))
        self.assertEquals(9, h.num_divisors([[2, 2], [5, 2]]))
        self.assertEquals([[2, 4], [3, 4], [5, 1], [7, 1]], h.factor(45360))
        self.assertEquals(100, h.num_divisors([[2, 4], [3, 4], [5, 1], [7, 1]]))
        self.assertEquals([[2, 2], [3, 2], [5, 3], [7, 1], [11, 1], [13, 1], [17, 1]], h.factor(76576500))
        self.assertEquals(576, h.num_divisors([[2, 2], [3, 2], [5, 3], [7, 1], [11, 1], [13, 1], [17, 1]]))

    def test_problem_13(self):
        self.assertEquals('5537376229', LargeSum().digit_sum(10))
        self.assertEquals('5537376230', LargeSum().digit_sum(11))
        self.assertEquals('5537376230', LargeSum().digit_sum(20))
        self.assertEquals('5537376230', LargeSum().digit_sum(50))
        self.assertEquals('5537376230', LargeSum().find())

    def test_problem14(self):
        self.assertEquals(0, LongestCollatzSequence.collatz(1))
        self.assertEquals(1, LongestCollatzSequence.collatz(2))
        self.assertEquals(7, LongestCollatzSequence.collatz(3))
        self.assertEquals(20, LongestCollatzSequence.collatz(18))
        self.assertEquals(121, LongestCollatzSequence.collatz(129))
        self.assertEquals(181, LongestCollatzSequence.collatz(1161))
        self.assertEquals(508, LongestCollatzSequence.collatz(626331))
        self.assertEquals(524, LongestCollatzSequence.collatz(837799))
        self.assertEquals(474, LongestCollatzSequence.collatz(1234567890987654321))

    def test_problem15(self):
        self.assertAlmostEquals(6, LatticePaths.find(2), 1)
        self.assertAlmostEquals(20, LatticePaths.find(3), 1)
        self.assertAlmostEquals(70, LatticePaths.find(4), 1)
        self.assertAlmostEquals(252, LatticePaths.find(5), 1)
        self.assertAlmostEquals(924, LatticePaths.find(6), 1)
        self.assertAlmostEquals(184756, LatticePaths.find(10), 1)
        self.assertAlmostEquals(35345263800, LatticePaths.find(19), 1)
        self.assertAlmostEquals(137846528820, LatticePaths.find(20), 1)
        self.assertAlmostEquals(538257874440, LatticePaths.find(21), 1)

    def test_problem_16(self):
        self.assertEquals(1, PowerDigitSum.find(0))
        self.assertEquals(2, PowerDigitSum.find(1))
        self.assertEquals(4, PowerDigitSum.find(2))
        self.assertEquals(7, PowerDigitSum.find(10))
        self.assertEquals(31, PowerDigitSum.find(20))
        self.assertEquals(115, PowerDigitSum.find(100))
        self.assertEquals(679, PowerDigitSum.find(500))
        self.assertEquals(1366, PowerDigitSum.find(1000))

    def test_problem_17(self):
        self.assertEquals('one', NumberLetterCounts.in_words(1))
        self.assertEquals('two', NumberLetterCounts.in_words(2))
        self.assertEquals('seventeen', NumberLetterCounts.in_words(17))
        self.assertEquals('one hundred and fifteen', NumberLetterCounts.in_words(115))
        self.assertEquals('three hundred and forty-two', NumberLetterCounts.in_words(342))
        self.assertEquals('one thousand', NumberLetterCounts.in_words(1000))
        self.assertEquals(3, NumberLetterCounts.letter_count('one'))
        self.assertEquals(3, NumberLetterCounts.letter_count('two'))
        self.assertEquals(9, NumberLetterCounts.letter_count('seventeen'))
        self.assertEquals(20, NumberLetterCounts.letter_count('one hundred and fifteen'))
        self.assertEquals(23, NumberLetterCounts.letter_count('three hundred and forty-two'))
        self.assertEquals(11, NumberLetterCounts.letter_count('one thousand'))
        self.assertEquals(3, NumberLetterCounts.find(1))
        self.assertEquals(6, NumberLetterCounts.find(2))
        self.assertEquals(90, NumberLetterCounts.find(17))
        self.assertEquals(1133, NumberLetterCounts.find(115))
        self.assertEquals(6117, NumberLetterCounts.find(342))
        self.assertEquals(21124, NumberLetterCounts.find(1000))

if __name__ == '__main__':
    unittest.main()
