# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.25
    Generated by: https://openapi-generator.tech
"""

from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events.post import CreateNamespacedEvent
from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events.delete import DeleteCollectionNamespacedEvent
from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events_name.delete import DeleteNamespacedEvent
from kubernetes.client.paths.apis_events_k8s_io_v1_.get import GetApiResources
from kubernetes.client.paths.apis_events_k8s_io_v1_events.get import ListEventForAllNamespaces
from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events.get import ListNamespacedEvent
from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events_name.patch import PatchNamespacedEvent
from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events_name.get import ReadNamespacedEvent
from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events_name.put import ReplaceNamespacedEvent


class EventsV1Api(
    CreateNamespacedEvent,
    DeleteCollectionNamespacedEvent,
    DeleteNamespacedEvent,
    GetApiResources,
    ListEventForAllNamespaces,
    ListNamespacedEvent,
    PatchNamespacedEvent,
    ReadNamespacedEvent,
    ReplaceNamespacedEvent,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass