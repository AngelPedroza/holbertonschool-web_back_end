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
        Test public repos function
        :param mock_json: Mock get_json
        :return:
        """
        test_payload = [{"name": "Google"}, {"name": "Facebook"}]
        mock_json.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            res = test_class.public_repos()

            check = [i["name"] for i in test_payload]
            self.assertEqual(res, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
