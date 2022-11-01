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


class V1EnvFromSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    EnvFromSource represents the source of a set of ConfigMaps
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def configMapRef() -> typing.Type['V1ConfigMapEnvSource']:
                return V1ConfigMapEnvSource
            prefix = schemas.StrSchema
        
            @staticmethod
            def secretRef() -> typing.Type['V1SecretEnvSource']:
                return V1SecretEnvSource
            __annotations__ = {
                "configMapRef": configMapRef,
                "prefix": prefix,
                "secretRef": secretRef,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configMapRef"]) -> 'V1ConfigMapEnvSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefix"]) -> MetaOapg.properties.prefix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secretRef"]) -> 'V1SecretEnvSource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["configMapRef", "prefix", "secretRef", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configMapRef"]) -> typing.Union['V1ConfigMapEnvSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefix"]) -> typing.Union[MetaOapg.properties.prefix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secretRef"]) -> typing.Union['V1SecretEnvSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["configMapRef", "prefix", "secretRef", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        configMapRef: typing.Union['V1ConfigMapEnvSource', schemas.Unset] = schemas.unset,
        prefix: typing.Union[MetaOapg.properties.prefix, str, schemas.Unset] = schemas.unset,
        secretRef: typing.Union['V1SecretEnvSource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1EnvFromSource':
        return super().__new__(
            cls,
            *args,
            configMapRef=configMapRef,
            prefix=prefix,
            secretRef=secretRef,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_config_map_env_source import V1ConfigMapEnvSource
from kubernetes.client.model.v1_secret_env_source import V1SecretEnvSource
