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


class V1AWSElasticBlockStoreVolumeSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents a Persistent Disk resource in AWS.

An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.
    """


    class MetaOapg:
        required = {
            "volumeID",
        }
        
        class properties:
            volumeID = schemas.StrSchema
            fsType = schemas.StrSchema
            partition = schemas.Int32Schema
            readOnly = schemas.BoolSchema
            __annotations__ = {
                "volumeID": volumeID,
                "fsType": fsType,
                "partition": partition,
                "readOnly": readOnly,
            }
    
    volumeID: MetaOapg.properties.volumeID
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volumeID"]) -> MetaOapg.properties.volumeID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fsType"]) -> MetaOapg.properties.fsType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partition"]) -> MetaOapg.properties.partition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readOnly"]) -> MetaOapg.properties.readOnly: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["volumeID", "fsType", "partition", "readOnly", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volumeID"]) -> MetaOapg.properties.volumeID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fsType"]) -> typing.Union[MetaOapg.properties.fsType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partition"]) -> typing.Union[MetaOapg.properties.partition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readOnly"]) -> typing.Union[MetaOapg.properties.readOnly, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["volumeID", "fsType", "partition", "readOnly", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        volumeID: typing.Union[MetaOapg.properties.volumeID, str, ],
        fsType: typing.Union[MetaOapg.properties.fsType, str, schemas.Unset] = schemas.unset,
        partition: typing.Union[MetaOapg.properties.partition, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        readOnly: typing.Union[MetaOapg.properties.readOnly, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1AWSElasticBlockStoreVolumeSource':
        return super().__new__(
            cls,
            *args,
            volumeID=volumeID,
            fsType=fsType,
            partition=partition,
            readOnly=readOnly,
            _configuration=_configuration,
            **kwargs,
        )