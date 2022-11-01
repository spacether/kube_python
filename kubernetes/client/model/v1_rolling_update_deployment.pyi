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


class V1RollingUpdateDeployment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Spec to control the desired behavior of rolling update.
    """


    class MetaOapg:
        
        class properties:
            maxSurge = schemas.DictSchema
            maxUnavailable = schemas.DictSchema
            __annotations__ = {
                "maxSurge": maxSurge,
                "maxUnavailable": maxUnavailable,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxSurge"]) -> MetaOapg.properties.maxSurge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxUnavailable"]) -> MetaOapg.properties.maxUnavailable: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxSurge", "maxUnavailable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxSurge"]) -> typing.Union[MetaOapg.properties.maxSurge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxUnavailable"]) -> typing.Union[MetaOapg.properties.maxUnavailable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxSurge", "maxUnavailable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        maxSurge: typing.Union[MetaOapg.properties.maxSurge, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        maxUnavailable: typing.Union[MetaOapg.properties.maxUnavailable, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1RollingUpdateDeployment':
        return super().__new__(
            cls,
            *args,
            maxSurge=maxSurge,
            maxUnavailable=maxUnavailable,
            _configuration=_configuration,
            **kwargs,
        )
