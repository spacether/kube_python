# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.25
    Generated by: https://openapi-generator.tech
"""

from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets.post import CreateNamespacedPodDisruptionBudget
from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets.delete import DeleteCollectionNamespacedPodDisruptionBudget
from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets_name.delete import DeleteNamespacedPodDisruptionBudget
from kubernetes.client.paths.apis_policy_v1_.get import GetApiResources
from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets.get import ListNamespacedPodDisruptionBudget
from kubernetes.client.paths.apis_policy_v1_poddisruptionbudgets.get import ListPodDisruptionBudgetForAllNamespaces
from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets_name.patch import PatchNamespacedPodDisruptionBudget
from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets_name_status.patch import PatchNamespacedPodDisruptionBudgetStatus
from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets_name.get import ReadNamespacedPodDisruptionBudget
from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets_name_status.get import ReadNamespacedPodDisruptionBudgetStatus
from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets_name.put import ReplaceNamespacedPodDisruptionBudget
from kubernetes.client.paths.apis_policy_v1_namespaces_namespace_poddisruptionbudgets_name_status.put import ReplaceNamespacedPodDisruptionBudgetStatus


class PolicyV1Api(
    CreateNamespacedPodDisruptionBudget,
    DeleteCollectionNamespacedPodDisruptionBudget,
    DeleteNamespacedPodDisruptionBudget,
    GetApiResources,
    ListNamespacedPodDisruptionBudget,
    ListPodDisruptionBudgetForAllNamespaces,
    PatchNamespacedPodDisruptionBudget,
    PatchNamespacedPodDisruptionBudgetStatus,
    ReadNamespacedPodDisruptionBudget,
    ReadNamespacedPodDisruptionBudgetStatus,
    ReplaceNamespacedPodDisruptionBudget,
    ReplaceNamespacedPodDisruptionBudgetStatus,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
