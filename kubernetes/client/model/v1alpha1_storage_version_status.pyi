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


class V1alpha1StorageVersionStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    API server instances report the versions they can decode and the version they encode objects to when persisting objects in the backend.
    """


    class MetaOapg:
        
        class properties:
            commonEncodingVersion = schemas.StrSchema
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1alpha1StorageVersionCondition']:
                        return V1alpha1StorageVersionCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1alpha1StorageVersionCondition'], typing.List['V1alpha1StorageVersionCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1alpha1StorageVersionCondition':
                    return super().__getitem__(i)
            
            
            class storageVersions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1alpha1ServerStorageVersion']:
                        return V1alpha1ServerStorageVersion
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1alpha1ServerStorageVersion'], typing.List['V1alpha1ServerStorageVersion']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'storageVersions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1alpha1ServerStorageVersion':
                    return super().__getitem__(i)
            __annotations__ = {
                "commonEncodingVersion": commonEncodingVersion,
                "conditions": conditions,
                "storageVersions": storageVersions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commonEncodingVersion"]) -> MetaOapg.properties.commonEncodingVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storageVersions"]) -> MetaOapg.properties.storageVersions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["commonEncodingVersion", "conditions", "storageVersions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commonEncodingVersion"]) -> typing.Union[MetaOapg.properties.commonEncodingVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storageVersions"]) -> typing.Union[MetaOapg.properties.storageVersions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["commonEncodingVersion", "conditions", "storageVersions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        commonEncodingVersion: typing.Union[MetaOapg.properties.commonEncodingVersion, str, schemas.Unset] = schemas.unset,
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, schemas.Unset] = schemas.unset,
        storageVersions: typing.Union[MetaOapg.properties.storageVersions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1alpha1StorageVersionStatus':
        return super().__new__(
            cls,
            *args,
            commonEncodingVersion=commonEncodingVersion,
            conditions=conditions,
            storageVersions=storageVersions,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1alpha1_server_storage_version import V1alpha1ServerStorageVersion
from client.model.v1alpha1_storage_version_condition import V1alpha1StorageVersionCondition