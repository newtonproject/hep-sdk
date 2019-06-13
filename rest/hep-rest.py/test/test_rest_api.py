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

import hep_rest
from api.rest_api import RestApi  # noqa: E501
from hep_rest.rest import ApiException


class TestRestApi(unittest.TestCase):
    """RestApi unit test stubs"""

    def setUp(self):
        self.api = api.rest_api.RestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rest_dapps_read(self):
        """Test case for rest_dapps_read

        """
        pass

    def test_rest_newids_read(self):
        """Test case for rest_newids_read

        """
        pass

    def test_rest_newnet_caches_auth_create(self):
        """Test case for rest_newnet_caches_auth_create

        """
        pass

    def test_rest_newnet_caches_auth_read(self):
        """Test case for rest_newnet_caches_auth_read

        """
        pass

    def test_rest_newnet_caches_pay_create(self):
        """Test case for rest_newnet_caches_pay_create

        """
        pass

    def test_rest_newnet_caches_pay_read(self):
        """Test case for rest_newnet_caches_pay_read

        """
        pass

    def test_rest_proofs_create(self):
        """Test case for rest_proofs_create

        """
        pass

    def test_rest_proofs_delete(self):
        """Test case for rest_proofs_delete

        """
        pass


if __name__ == '__main__':
    unittest.main()
