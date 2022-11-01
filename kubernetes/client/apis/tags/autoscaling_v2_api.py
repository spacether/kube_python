# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.25
    Generated by: https://openapi-generator.tech
"""

from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers.post import CreateNamespacedHorizontalPodAutoscaler
from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers.delete import DeleteCollectionNamespacedHorizontalPodAutoscaler
from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers_name.delete import DeleteNamespacedHorizontalPodAutoscaler
from kubernetes.client.paths.apis_autoscaling_v2_.get import GetApiResources
from kubernetes.client.paths.apis_autoscaling_v2_horizontalpodautoscalers.get import ListHorizontalPodAutoscalerForAllNamespaces
from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers.get import ListNamespacedHorizontalPodAutoscaler
from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers_name.patch import PatchNamespacedHorizontalPodAutoscaler
from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers_name_status.patch import PatchNamespacedHorizontalPodAutoscalerStatus
from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers_name.get import ReadNamespacedHorizontalPodAutoscaler
from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers_name_status.get import ReadNamespacedHorizontalPodAutoscalerStatus
from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers_name.put import ReplaceNamespacedHorizontalPodAutoscaler
from kubernetes.client.paths.apis_autoscaling_v2_namespaces_namespace_horizontalpodautoscalers_name_status.put import ReplaceNamespacedHorizontalPodAutoscalerStatus


class AutoscalingV2Api(
    CreateNamespacedHorizontalPodAutoscaler,
    DeleteCollectionNamespacedHorizontalPodAutoscaler,
    DeleteNamespacedHorizontalPodAutoscaler,
    GetApiResources,
    ListHorizontalPodAutoscalerForAllNamespaces,
    ListNamespacedHorizontalPodAutoscaler,
    PatchNamespacedHorizontalPodAutoscaler,
    PatchNamespacedHorizontalPodAutoscalerStatus,
    ReadNamespacedHorizontalPodAutoscaler,
    ReadNamespacedHorizontalPodAutoscalerStatus,
    ReplaceNamespacedHorizontalPodAutoscaler,
    ReplaceNamespacedHorizontalPodAutoscalerStatus,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
