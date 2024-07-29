#!/usr/bin/env python3
""" Task 0."""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """ A class to test to te function access_nested_map."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[int, Dict]):
        """ Testing the function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
