#!/usr/bin/env python3
"""First unit test
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
import requests

from utils import access_nested_map, get_json, memoize


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
        self.assertEqual(
            access_nested_map(nested_map=nested_map, path=path), expected
        )

    @parameterized.expand([
        ({}, ("a",), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Tets the exceptions of the function
        :param nested_map: Dict to test
        :param path: Keys in the order to access
        :param expected: Value expected
        :return: Nothing
        """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map=nested_map, path=path)

        self.assertEqual(repr(err.exception), repr(expected))


class TestGetJson(unittest.TestCase):
    """Test the get json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test if a request execute correctly
        :param test_url: Url to tets
        :param test_payload: The value expected
        :return: Nothing
        """
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Test the memoize decorator
    """
    def test_memoize(self):
        """
        Test the memoize decorator that save the return of the function
        that use it. If the attribute already exist the memo
        not execute the function, return the value directly.
        :return: Nothing
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_memo:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_memo.assert_called_once()
