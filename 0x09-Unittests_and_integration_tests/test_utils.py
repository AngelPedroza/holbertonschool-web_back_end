#!/usr/bin/env python3
"""First unit test
"""
import unittest
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test the map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Take the parametrizer and test the access to a dict
        :param nested_map: Dict to test
        :param path: Keys in the order to access
        :param expected: Value expected
        :return: Nothing
        """
        self.assertEqual(access_nested_map(nested_map=nested_map, path=path), expected)
