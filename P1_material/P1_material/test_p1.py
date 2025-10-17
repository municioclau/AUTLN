#!/usr/bin/env python

import re
import unittest

from regular_expressions import RE0, RE1, RE2, RE3, RE4, RE5, RE6


class TestP0(unittest.TestCase):
    """Tests of assignment 0."""

    def check_expression(self, expr: str, string: str, expected: bool) -> None:
        with self.subTest(string=string):
            match = re.fullmatch(expr, string)
            self.assertEqual(bool(match), expected)

    def test_exercise_0(self) -> None:
        self.check_expression(RE0, "a", True)
        self.check_expression(RE0, "bbbbaba", True)
        self.check_expression(RE0, "abbab", False)
        self.check_expression(RE0, "b", False)

    def test_exercise_1(self) -> None:
        self.check_expression(RE1, "", True)
        self.check_expression(RE1, "00", True)
        self.check_expression(RE1, "110101", True)
        self.check_expression(RE1, "1", False)
        self.check_expression(RE1, "1ba", False)
        

    def test_exercise_2(self) -> None:
        pass

    def test_exercise_3(self) -> None:
        pass

    def test_exercise_4(self) -> None:
        pass

    def test_exercise_5(self) -> None:
        pass

    def test_exercise_6(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
