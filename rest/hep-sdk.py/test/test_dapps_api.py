# coding: utf-8

"""
    HEP REST API

    The REST API for HEP protocol  # noqa: E501

    OpenAPI spec version: v1
    Contact: xiawu@zeuux.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.dapps_api import DappsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDappsApi(unittest.TestCase):
    """DappsApi unit test stubs"""

    def setUp(self):
        self.api = api.dapps_api.DappsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dapps_read(self):
        """Test case for dapps_read

        """
        pass


if __name__ == '__main__':
    unittest.main()
