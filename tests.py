
import unittest
from io import StringIO
from unittest.mock import patch

from tasks.task_1 import get_first_unique_char
from tasks.task_2 import Book
from tasks.task_3 import find_first_occurrence


class TestGetFirstUniqueChar(unittest.TestCase):
    def test_get_first_unique_char(self):
        string1 = "hello"
        self.assertEqual(get_first_unique_char(string1), 'h')

        string2 = "leetcode"
        self.assertEqual(get_first_unique_char(string2), 'l')

        string3 = "abracadabra"
        self.assertEqual(get_first_unique_char(string3), 'c')

    def test_get_first_unique_char_no_unique_char(self):
        string = "aabbcc"
        self.assertIsNone(get_first_unique_char(string))

    def test_get_first_unique_char_empty_string(self):
        string = ""
        self.assertIsNone(get_first_unique_char(string))


class TestBookMethods(unittest.TestCase):
    def setUp(self):
        self.book = Book('Test_book_1', 'Test_author_1', 100)

    def test_turn_page_default(self):
        self.book.turn_page()
        self.assertEqual(self.book.current_page, 0)

    def test_turn_page_positive(self):
        self.book.turn_page(20)
        self.assertEqual(self.book.current_page, 19)

    def test_turn_page_under_limit(self):
        self.book.turn_page(21)
        self.book.turn_page(-5)
        self.assertEqual(self.book.current_page, 15)

    def test_turn_page_negative(self):
        self.book.turn_page(-200)
        self.assertEqual(self.book.current_page, -1)

    def test_turn_page_over_limit(self):
        self.book.turn_page(200)
        self.assertEqual(self.book.current_page, 100)

    def test_turn_page_invalid_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.book.turn_page('wrong input')
            self.assertEqual(self.book.current_page, -1)
            self.assertEqual(fake_out.getvalue().strip(), 'Only an integer must be entered')


class TestFindFirstOccurrence(unittest.TestCase):
    def test_existing_element(self):
        array = [1, 1, 2, 2, 4, 4, 6, 6, 6, 8, 8, 10, 10, 10, 11, 13, 13, 15, 15, 15, 18, 18, 20, 20, 22, 22, 24, 24,
                 26, 26, 26, 29, 30, 31, 31, 33, 35, 35, 37, 37, 39, 39, 41, 41, 43, 45, 45, 47, 49, 50]
        target = 15
        self.assertEqual(find_first_occurrence(array, target), 17)

    def test_non_existing_element(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 11
        self.assertEqual(find_first_occurrence(array, target), -1)


if __name__ == '__main__':
    unittest.main()
