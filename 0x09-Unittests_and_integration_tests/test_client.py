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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test public repos
        :return: Nothing
        """
        test_payload = [{"name": "test_1"},  {"name": "test_2"}]
        mock_json.return_value = test_payload

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock:
            mock.return_value = "test/value"
            test_class = GithubOrgClient('test')
            list_test = test_class.public_repos()

            verify_dict = [
                {"name": i} for i in list_test
            ]
            self.assertEqual(verify_dict, test_payload)
            mock.assert_called_once()
            mock_json.assert_called_once()
