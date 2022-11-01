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


class V2MetricValueStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    MetricValueStatus holds the current value for a metric
    """


    class MetaOapg:
        
        class properties:
            averageUtilization = schemas.Int32Schema
            averageValue = schemas.StrSchema
            value = schemas.StrSchema
            __annotations__ = {
                "averageUtilization": averageUtilization,
                "averageValue": averageValue,
                "value": value,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageUtilization"]) -> MetaOapg.properties.averageUtilization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageValue"]) -> MetaOapg.properties.averageValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["averageUtilization", "averageValue", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageUtilization"]) -> typing.Union[MetaOapg.properties.averageUtilization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageValue"]) -> typing.Union[MetaOapg.properties.averageValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["averageUtilization", "averageValue", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        averageUtilization: typing.Union[MetaOapg.properties.averageUtilization, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        averageValue: typing.Union[MetaOapg.properties.averageValue, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V2MetricValueStatus':
        return super().__new__(
            cls,
            *args,
            averageUtilization=averageUtilization,
            averageValue=averageValue,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )
