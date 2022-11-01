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


class V1EndpointConditions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    EndpointConditions represents the current condition of an endpoint.
    """


    class MetaOapg:
        
        class properties:
            ready = schemas.BoolSchema
            serving = schemas.BoolSchema
            terminating = schemas.BoolSchema
            __annotations__ = {
                "ready": ready,
                "serving": serving,
                "terminating": terminating,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ready"]) -> MetaOapg.properties.ready: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serving"]) -> MetaOapg.properties.serving: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminating"]) -> MetaOapg.properties.terminating: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ready", "serving", "terminating", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ready"]) -> typing.Union[MetaOapg.properties.ready, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serving"]) -> typing.Union[MetaOapg.properties.serving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminating"]) -> typing.Union[MetaOapg.properties.terminating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ready", "serving", "terminating", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ready: typing.Union[MetaOapg.properties.ready, bool, schemas.Unset] = schemas.unset,
        serving: typing.Union[MetaOapg.properties.serving, bool, schemas.Unset] = schemas.unset,
        terminating: typing.Union[MetaOapg.properties.terminating, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1EndpointConditions':
        return super().__new__(
            cls,
            *args,
            ready=ready,
            serving=serving,
            terminating=terminating,
            _configuration=_configuration,
            **kwargs,
        )
