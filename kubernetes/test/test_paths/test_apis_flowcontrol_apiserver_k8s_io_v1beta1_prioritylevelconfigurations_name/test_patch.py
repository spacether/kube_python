# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import kubernetes.client
from kubernetes.client.paths.apis_flowcontrol_apiserver_k8s_io_v1beta1_prioritylevelconfigurations_name import patch  # noqa: E501
from kubernetes.client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApisFlowcontrolApiserverK8sIoV1beta1PrioritylevelconfigurationsName(ApiTestMixin, unittest.TestCase):
    """
    ApisFlowcontrolApiserverK8sIoV1beta1PrioritylevelconfigurationsName unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = patch.ApiForpatch(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
















if __name__ == '__main__':
    unittest.main()
