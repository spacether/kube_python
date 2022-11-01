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


class V2beta2PodsMetricStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PodsMetricStatus indicates the current value of a metric describing each pod in the current scale target (for example, transactions-processed-per-second).
    """


    class MetaOapg:
        required = {
            "current",
            "metric",
        }
        
        class properties:
        
            @staticmethod
            def current() -> typing.Type['V2beta2MetricValueStatus']:
                return V2beta2MetricValueStatus
        
            @staticmethod
            def metric() -> typing.Type['V2beta2MetricIdentifier']:
                return V2beta2MetricIdentifier
            __annotations__ = {
                "current": current,
                "metric": metric,
            }
    
    current: 'V2beta2MetricValueStatus'
    metric: 'V2beta2MetricIdentifier'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current"]) -> 'V2beta2MetricValueStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metric"]) -> 'V2beta2MetricIdentifier': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["current", "metric", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> 'V2beta2MetricValueStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metric"]) -> 'V2beta2MetricIdentifier': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["current", "metric", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        current: 'V2beta2MetricValueStatus',
        metric: 'V2beta2MetricIdentifier',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V2beta2PodsMetricStatus':
        return super().__new__(
            cls,
            *args,
            current=current,
            metric=metric,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v2beta2_metric_identifier import V2beta2MetricIdentifier
from kubernetes.client.model.v2beta2_metric_value_status import V2beta2MetricValueStatus
