# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.25
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from kubernetes.client import schemas  # noqa: F401


class V2beta2MetricSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once).
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            type = schemas.StrSchema
        
            @staticmethod
            def containerResource() -> typing.Type['V2beta2ContainerResourceMetricSource']:
                return V2beta2ContainerResourceMetricSource
        
            @staticmethod
            def external() -> typing.Type['V2beta2ExternalMetricSource']:
                return V2beta2ExternalMetricSource
        
            @staticmethod
            def object() -> typing.Type['V2beta2ObjectMetricSource']:
                return V2beta2ObjectMetricSource
        
            @staticmethod
            def pods() -> typing.Type['V2beta2PodsMetricSource']:
                return V2beta2PodsMetricSource
        
            @staticmethod
            def resource() -> typing.Type['V2beta2ResourceMetricSource']:
                return V2beta2ResourceMetricSource
            __annotations__ = {
                "type": type,
                "containerResource": containerResource,
                "external": external,
                "object": object,
                "pods": pods,
                "resource": resource,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["containerResource"]) -> 'V2beta2ContainerResourceMetricSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external"]) -> 'V2beta2ExternalMetricSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> 'V2beta2ObjectMetricSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pods"]) -> 'V2beta2PodsMetricSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource"]) -> 'V2beta2ResourceMetricSource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "containerResource", "external", "object", "pods", "resource", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["containerResource"]) -> typing.Union['V2beta2ContainerResourceMetricSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external"]) -> typing.Union['V2beta2ExternalMetricSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union['V2beta2ObjectMetricSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pods"]) -> typing.Union['V2beta2PodsMetricSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource"]) -> typing.Union['V2beta2ResourceMetricSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "containerResource", "external", "object", "pods", "resource", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        containerResource: typing.Union['V2beta2ContainerResourceMetricSource', schemas.Unset] = schemas.unset,
        external: typing.Union['V2beta2ExternalMetricSource', schemas.Unset] = schemas.unset,
        object: typing.Union['V2beta2ObjectMetricSource', schemas.Unset] = schemas.unset,
        pods: typing.Union['V2beta2PodsMetricSource', schemas.Unset] = schemas.unset,
        resource: typing.Union['V2beta2ResourceMetricSource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V2beta2MetricSpec':
        return super().__new__(
            cls,
            *args,
            type=type,
            containerResource=containerResource,
            external=external,
            object=object,
            pods=pods,
            resource=resource,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v2beta2_container_resource_metric_source import V2beta2ContainerResourceMetricSource
from kubernetes.client.model.v2beta2_external_metric_source import V2beta2ExternalMetricSource
from kubernetes.client.model.v2beta2_object_metric_source import V2beta2ObjectMetricSource
from kubernetes.client.model.v2beta2_pods_metric_source import V2beta2PodsMetricSource
from kubernetes.client.model.v2beta2_resource_metric_source import V2beta2ResourceMetricSource
