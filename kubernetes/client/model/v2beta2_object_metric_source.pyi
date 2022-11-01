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

from client import schemas  # noqa: F401


class V2beta2ObjectMetricSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).
    """


    class MetaOapg:
        required = {
            "describedObject",
            "metric",
            "target",
        }
        
        class properties:
        
            @staticmethod
            def describedObject() -> typing.Type['V2beta2CrossVersionObjectReference']:
                return V2beta2CrossVersionObjectReference
        
            @staticmethod
            def metric() -> typing.Type['V2beta2MetricIdentifier']:
                return V2beta2MetricIdentifier
        
            @staticmethod
            def target() -> typing.Type['V2beta2MetricTarget']:
                return V2beta2MetricTarget
            __annotations__ = {
                "describedObject": describedObject,
                "metric": metric,
                "target": target,
            }
    
    describedObject: 'V2beta2CrossVersionObjectReference'
    metric: 'V2beta2MetricIdentifier'
    target: 'V2beta2MetricTarget'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["describedObject"]) -> 'V2beta2CrossVersionObjectReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metric"]) -> 'V2beta2MetricIdentifier': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> 'V2beta2MetricTarget': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["describedObject", "metric", "target", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["describedObject"]) -> 'V2beta2CrossVersionObjectReference': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metric"]) -> 'V2beta2MetricIdentifier': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> 'V2beta2MetricTarget': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["describedObject", "metric", "target", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        describedObject: 'V2beta2CrossVersionObjectReference',
        metric: 'V2beta2MetricIdentifier',
        target: 'V2beta2MetricTarget',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V2beta2ObjectMetricSource':
        return super().__new__(
            cls,
            *args,
            describedObject=describedObject,
            metric=metric,
            target=target,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v2beta2_cross_version_object_reference import V2beta2CrossVersionObjectReference
from client.model.v2beta2_metric_identifier import V2beta2MetricIdentifier
from client.model.v2beta2_metric_target import V2beta2MetricTarget
