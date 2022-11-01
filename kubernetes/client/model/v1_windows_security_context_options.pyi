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


class V1WindowsSecurityContextOptions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    WindowsSecurityContextOptions contain Windows-specific options and credentials.
    """


    class MetaOapg:
        
        class properties:
            gmsaCredentialSpec = schemas.StrSchema
            gmsaCredentialSpecName = schemas.StrSchema
            hostProcess = schemas.BoolSchema
            runAsUserName = schemas.StrSchema
            __annotations__ = {
                "gmsaCredentialSpec": gmsaCredentialSpec,
                "gmsaCredentialSpecName": gmsaCredentialSpecName,
                "hostProcess": hostProcess,
                "runAsUserName": runAsUserName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gmsaCredentialSpec"]) -> MetaOapg.properties.gmsaCredentialSpec: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gmsaCredentialSpecName"]) -> MetaOapg.properties.gmsaCredentialSpecName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostProcess"]) -> MetaOapg.properties.hostProcess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runAsUserName"]) -> MetaOapg.properties.runAsUserName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gmsaCredentialSpec", "gmsaCredentialSpecName", "hostProcess", "runAsUserName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gmsaCredentialSpec"]) -> typing.Union[MetaOapg.properties.gmsaCredentialSpec, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gmsaCredentialSpecName"]) -> typing.Union[MetaOapg.properties.gmsaCredentialSpecName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostProcess"]) -> typing.Union[MetaOapg.properties.hostProcess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runAsUserName"]) -> typing.Union[MetaOapg.properties.runAsUserName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gmsaCredentialSpec", "gmsaCredentialSpecName", "hostProcess", "runAsUserName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        gmsaCredentialSpec: typing.Union[MetaOapg.properties.gmsaCredentialSpec, str, schemas.Unset] = schemas.unset,
        gmsaCredentialSpecName: typing.Union[MetaOapg.properties.gmsaCredentialSpecName, str, schemas.Unset] = schemas.unset,
        hostProcess: typing.Union[MetaOapg.properties.hostProcess, bool, schemas.Unset] = schemas.unset,
        runAsUserName: typing.Union[MetaOapg.properties.runAsUserName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1WindowsSecurityContextOptions':
        return super().__new__(
            cls,
            *args,
            gmsaCredentialSpec=gmsaCredentialSpec,
            gmsaCredentialSpecName=gmsaCredentialSpecName,
            hostProcess=hostProcess,
            runAsUserName=runAsUserName,
            _configuration=_configuration,
            **kwargs,
        )
