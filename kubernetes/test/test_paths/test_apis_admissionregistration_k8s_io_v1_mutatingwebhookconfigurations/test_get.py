# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import kubernetes.client
from kubernetes.client.paths.apis_admissionregistration_k8s_io_v1_mutatingwebhookconfigurations import get  # noqa: E501
from kubernetes.client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApisAdmissionregistrationK8sIoV1Mutatingwebhookconfigurations(ApiTestMixin, unittest.TestCase):
    """
    ApisAdmissionregistrationK8sIoV1Mutatingwebhookconfigurations unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200












if __name__ == '__main__':
    unittest.main()