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


class V2ContainerResourceMetricSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ContainerResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  The values will be averaged together before being compared to the target.  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.  Only one "target" type should be set.
    """


    class MetaOapg:
        required = {
            "container",
            "name",
            "target",
        }
        
        class properties:
            container = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def target() -> typing.Type['V2MetricTarget']:
                return V2MetricTarget
            __annotations__ = {
                "container": container,
                "name": name,
                "target": target,
            }
    
    container: MetaOapg.properties.container
    name: MetaOapg.properties.name
    target: 'V2MetricTarget'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["container"]) -> MetaOapg.properties.container: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> 'V2MetricTarget': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["container", "name", "target", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["container"]) -> MetaOapg.properties.container: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> 'V2MetricTarget': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["container", "name", "target", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        container: typing.Union[MetaOapg.properties.container, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        target: 'V2MetricTarget',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V2ContainerResourceMetricSource':
        return super().__new__(
            cls,
            *args,
            container=container,
            name=name,
            target=target,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v2_metric_target import V2MetricTarget
