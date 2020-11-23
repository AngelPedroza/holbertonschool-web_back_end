#!/usr/bin/env python3
"""Test client module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test Org function
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """
        Test the org request
        :return: Nothing
        """
        test_class = GithubOrgClient(org)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
