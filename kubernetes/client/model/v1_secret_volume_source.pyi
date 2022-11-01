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


class V1SecretVolumeSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Adapts a Secret into a volume.

The contents of the target Secret's Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.
    """


    class MetaOapg:
        
        class properties:
            defaultMode = schemas.Int32Schema
            
            
            class items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1KeyToPath']:
                        return V1KeyToPath
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1KeyToPath'], typing.List['V1KeyToPath']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1KeyToPath':
                    return super().__getitem__(i)
            optional = schemas.BoolSchema
            secretName = schemas.StrSchema
            __annotations__ = {
                "defaultMode": defaultMode,
                "items": items,
                "optional": optional,
                "secretName": secretName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultMode"]) -> MetaOapg.properties.defaultMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optional"]) -> MetaOapg.properties.optional: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secretName"]) -> MetaOapg.properties.secretName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["defaultMode", "items", "optional", "secretName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultMode"]) -> typing.Union[MetaOapg.properties.defaultMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union[MetaOapg.properties.items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["optional"]) -> typing.Union[MetaOapg.properties.optional, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secretName"]) -> typing.Union[MetaOapg.properties.secretName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["defaultMode", "items", "optional", "secretName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        defaultMode: typing.Union[MetaOapg.properties.defaultMode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        items: typing.Union[MetaOapg.properties.items, list, tuple, schemas.Unset] = schemas.unset,
        optional: typing.Union[MetaOapg.properties.optional, bool, schemas.Unset] = schemas.unset,
        secretName: typing.Union[MetaOapg.properties.secretName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1SecretVolumeSource':
        return super().__new__(
            cls,
            *args,
            defaultMode=defaultMode,
            items=items,
            optional=optional,
            secretName=secretName,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_key_to_path import V1KeyToPath
