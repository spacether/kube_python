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


class V1alpha1StorageVersion(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Storage version of a specific resource.
    """


    class MetaOapg:
        required = {
            "spec",
            "status",
        }
        
        class properties:
            spec = schemas.DictSchema
        
            @staticmethod
            def status() -> typing.Type['V1alpha1StorageVersionStatus']:
                return V1alpha1StorageVersionStatus
            apiVersion = schemas.StrSchema
            kind = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['V1ObjectMeta']:
                return V1ObjectMeta
            __annotations__ = {
                "spec": spec,
                "status": status,
                "apiVersion": apiVersion,
                "kind": kind,
                "metadata": metadata,
            }
    
    spec: MetaOapg.properties.spec
    status: 'V1alpha1StorageVersionStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spec"]) -> MetaOapg.properties.spec: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'V1alpha1StorageVersionStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiVersion"]) -> MetaOapg.properties.apiVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'V1ObjectMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["spec", "status", "apiVersion", "kind", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spec"]) -> MetaOapg.properties.spec: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'V1alpha1StorageVersionStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiVersion"]) -> typing.Union[MetaOapg.properties.apiVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union[MetaOapg.properties.kind, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['V1ObjectMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["spec", "status", "apiVersion", "kind", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        spec: typing.Union[MetaOapg.properties.spec, dict, frozendict.frozendict, ],
        status: 'V1alpha1StorageVersionStatus',
        apiVersion: typing.Union[MetaOapg.properties.apiVersion, str, schemas.Unset] = schemas.unset,
        kind: typing.Union[MetaOapg.properties.kind, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['V1ObjectMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1alpha1StorageVersion':
        return super().__new__(
            cls,
            *args,
            spec=spec,
            status=status,
            apiVersion=apiVersion,
            kind=kind,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_object_meta import V1ObjectMeta
from client.model.v1alpha1_storage_version_status import V1alpha1StorageVersionStatus
