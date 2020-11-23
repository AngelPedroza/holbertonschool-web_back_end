#!/usr/bin/env python3
"""Test client module
"""
import unittest
from unittest.mock import patch, PropertyMock
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
    def test_org(self, organization: str, mock: unittest.mock.patch):
        """
        Test the org request
        :return: Nothing
        """
        test_class = GithubOrgClient(organization)
        test_class.org()
        mock.assert_called_once_with(
            f'https://api.github.com/orgs/{organization}'
        )

    def test_public_repos_url(self):
        """
        Test public organization repos
        :return: Nothing
        """
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "test"}
            test_class = GithubOrgClient('test')
            res = test_class._public_repos_url
            self.assertEqual(res, mock.return_value['repos_url'])
