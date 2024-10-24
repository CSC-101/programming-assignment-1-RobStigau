import data
import hw1
import unittest
import math

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        vowel = 'apple'
        result = hw1.vowel_count(vowel)
        expected = 2
        self.assertEqual(result, expected)

    def test_vowel_count2(self):
        vowel = 'Banana'
        result = hw1.vowel_count(vowel)
        expected = 3
        self.assertEqual(result, expected)

    # Part 2
    def test_shorts_lists1(self):
        lists = [[4, 3], [4, 2], [9,2,3,1], [10,2], [6, 4, 3, 5]]
        result = hw1.shorts_lists(lists)
        expected = [4, 3, 4, 2, 10, 2]
        self.assertEqual(result, expected)

    def test_shorts_lists2(self):
        lists = [[1, 5], [6, 8], [2, 3, 1], [4], [2, 1]]
        result = hw1.shorts_lists(lists)
        expected = [1, 5, 6, 8, 2, 1]
        self.assertEqual(result, expected)

    # Part 3
    def test_ascending_pairs1(self):
        lists = [[4, 3], [4, 2], [9,2,3,1], [10,2], [6, 4, 3, 5]]
        result = hw1.ascending_pairs(lists)
        expected = [3, 4, 2, 4, 9, 2, 3, 1, 2, 10, 6, 4, 3, 5]
        self.assertEqual(result, expected)

    def test_ascending_pairs2(self):
        lists = [[1, 5], [6, 8], [2, 3, 1], [4], [2, 1]]
        result = hw1.ascending_pairs(lists)
        expected = [1, 5, 6, 8, 2, 3, 1, 4, 1, 2]
        self.assertEqual(result, expected)

    # Part 4
    def test_add_prices1(self):
        price1 = data.Price(24, 36)
        price2 = data.Price(36, 21)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(60, 57)
        self.assertEqual(result, expected)

    def test_add_prices2(self):
        price1 = data.Price(15, 16)
        price2 = data.Price(20, 45)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(35, 61)
        self.assertEqual(result, expected)

    # Part 5
    def test_rectangle_area1(self):
        inputs = data.Rectangle(data.Point(-4,2), data.Point(3, -5))
        result = hw1.rectangle_area(inputs)
        expected = 49
        self.assertEqual(result, expected)

    def test_rectangle_area2(self):
        inputs = data.Rectangle(data.Point(-8,3), data.Point(6, -3))
        result = hw1.rectangle_area(inputs)
        expected = 84
        self.assertEqual(result, expected)

    # Part 6
    def test_books_by_author1(self):
        authname = 'Edgar Allen Poe'
        books = [data.Book(['Edgar Allen Poe'], 'The Tell-Tale Heart'), data.Book(['Edgar Allen Poe'], 'The Raven')]
        result = hw1.books_by_author(authname, books)
        expected = [data.Book(['Edgar Allen Poe'], 'The Tell-Tale Heart'), data.Book(['Edgar Allen Poe'], 'The Raven')]
        self.assertEqual(result, expected)

    def test_books_by_author2(self):
        authname = 'Edgar Allen Poe'
        books = [data.Book(['Edgar Allen Poe'], 'The Fall of the House of Usher'), data.Book(['Edgar Allen Poe'], 'The Black Cat'), data.Book(['William Shakespeare'], 'Romeo and Juliet')]
        result = hw1.books_by_author(authname, books)
        expected = [data.Book(['Edgar Allen Poe'], 'The Fall of the House of Usher'), data.Book(['Edgar Allen Poe'], 'The Black Cat')]
        self.assertEqual(result, expected)

    # Part 7
    def test_circle_bound1(self):
        inputs = data.Rectangle(data.Point(-4, 4), data.Point(2, -5))
        result = hw1.circle_bound(inputs)
        expected = data.Circle(data.Point(3.0, 4.5), math.sqrt(29.25))
        self.assertEqual(result, expected)

    def test_circle_bound2(self):
        inputs = data.Rectangle(data.Point(-8, 3), data.Point(6, -3))
        result = hw1.circle_bound(inputs)
        expected = data.Circle(data.Point(7.0, 3.0), math.sqrt(58))
        self.assertEqual(result, expected)

    # Part 8
    def test_below_average_pay1(self):
        lists = [data.Employee('Frank', 16), data.Employee('Tallis', 18), data.Employee('Jayden', 10)]
        result = hw1.below_pay_average(lists)
        expected = ['Jayden']
        self.assertEqual(result, expected)

    def test_below_average_pay2(self):
        lists = [data.Employee('Bob', 24), data.Employee('Koen', 40), data.Employee('Cole', 14)]
        result = hw1.below_pay_average(lists)
        expected = ['Bob', 'Cole']
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()
