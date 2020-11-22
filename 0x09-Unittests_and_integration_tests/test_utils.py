#!/usr/bin/env python3
"""First unit test
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
import requests

from utils import access_nested_map, get_json


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
