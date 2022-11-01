# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import kubernetes.client
from kubernetes.client.paths.api_v1_namespaces_namespace_services_name_proxy_path import delete  # noqa: E501
from kubernetes.client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1NamespacesNamespaceServicesNameProxyPath(ApiTestMixin, unittest.TestCase):
    """
    ApiV1NamespacesNamespaceServicesNameProxyPath unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
