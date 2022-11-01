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


class V1FCVolumeSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.
    """


    class MetaOapg:
        
        class properties:
            fsType = schemas.StrSchema
            lun = schemas.Int32Schema
            readOnly = schemas.BoolSchema
            
            
            class targetWWNs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targetWWNs':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class wwids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'wwids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "fsType": fsType,
                "lun": lun,
                "readOnly": readOnly,
                "targetWWNs": targetWWNs,
                "wwids": wwids,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fsType"]) -> MetaOapg.properties.fsType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lun"]) -> MetaOapg.properties.lun: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readOnly"]) -> MetaOapg.properties.readOnly: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetWWNs"]) -> MetaOapg.properties.targetWWNs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wwids"]) -> MetaOapg.properties.wwids: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fsType", "lun", "readOnly", "targetWWNs", "wwids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fsType"]) -> typing.Union[MetaOapg.properties.fsType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lun"]) -> typing.Union[MetaOapg.properties.lun, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readOnly"]) -> typing.Union[MetaOapg.properties.readOnly, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetWWNs"]) -> typing.Union[MetaOapg.properties.targetWWNs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wwids"]) -> typing.Union[MetaOapg.properties.wwids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fsType", "lun", "readOnly", "targetWWNs", "wwids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        fsType: typing.Union[MetaOapg.properties.fsType, str, schemas.Unset] = schemas.unset,
        lun: typing.Union[MetaOapg.properties.lun, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        readOnly: typing.Union[MetaOapg.properties.readOnly, bool, schemas.Unset] = schemas.unset,
        targetWWNs: typing.Union[MetaOapg.properties.targetWWNs, list, tuple, schemas.Unset] = schemas.unset,
        wwids: typing.Union[MetaOapg.properties.wwids, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1FCVolumeSource':
        return super().__new__(
            cls,
            *args,
            fsType=fsType,
            lun=lun,
            readOnly=readOnly,
            targetWWNs=targetWWNs,
            wwids=wwids,
            _configuration=_configuration,
            **kwargs,
        )
