# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.25
    Generated by: https://openapi-generator.tech
"""

from kubernetes.client.paths.apis_authorization_k8s_io_v1_namespaces_namespace_localsubjectaccessreviews.post import CreateNamespacedLocalSubjectAccessReview
from kubernetes.client.paths.apis_authorization_k8s_io_v1_selfsubjectaccessreviews.post import CreateSelfSubjectAccessReview
from kubernetes.client.paths.apis_authorization_k8s_io_v1_selfsubjectrulesreviews.post import CreateSelfSubjectRulesReview
from kubernetes.client.paths.apis_authorization_k8s_io_v1_subjectaccessreviews.post import CreateSubjectAccessReview
from kubernetes.client.paths.apis_authorization_k8s_io_v1_.get import GetApiResources


class AuthorizationV1Api(
    CreateNamespacedLocalSubjectAccessReview,
    CreateSelfSubjectAccessReview,
    CreateSelfSubjectRulesReview,
    CreateSubjectAccessReview,
    GetApiResources,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass