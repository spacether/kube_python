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


class V1beta2FlowSchemaCondition(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    FlowSchemaCondition describes conditions for a FlowSchema.
    """


    class MetaOapg:
        
        class properties:
            lastTransitionTime = schemas.DateTimeSchema
            message = schemas.StrSchema
            reason = schemas.StrSchema
            status = schemas.StrSchema
            type = schemas.StrSchema
            __annotations__ = {
                "lastTransitionTime": lastTransitionTime,
                "message": message,
                "reason": reason,
                "status": status,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastTransitionTime"]) -> MetaOapg.properties.lastTransitionTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lastTransitionTime", "message", "reason", "status", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastTransitionTime"]) -> typing.Union[MetaOapg.properties.lastTransitionTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lastTransitionTime", "message", "reason", "status", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lastTransitionTime: typing.Union[MetaOapg.properties.lastTransitionTime, str, datetime, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1beta2FlowSchemaCondition':
        return super().__new__(
            cls,
            *args,
            lastTransitionTime=lastTransitionTime,
            message=message,
            reason=reason,
            status=status,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
