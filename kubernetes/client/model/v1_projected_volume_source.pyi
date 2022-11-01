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


class V1ProjectedVolumeSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents a projected volume source
    """


    class MetaOapg:
        
        class properties:
            defaultMode = schemas.Int32Schema
            
            
            class sources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1VolumeProjection']:
                        return V1VolumeProjection
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1VolumeProjection'], typing.List['V1VolumeProjection']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sources':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1VolumeProjection':
                    return super().__getitem__(i)
            __annotations__ = {
                "defaultMode": defaultMode,
                "sources": sources,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultMode"]) -> MetaOapg.properties.defaultMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sources"]) -> MetaOapg.properties.sources: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["defaultMode", "sources", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultMode"]) -> typing.Union[MetaOapg.properties.defaultMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sources"]) -> typing.Union[MetaOapg.properties.sources, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["defaultMode", "sources", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        defaultMode: typing.Union[MetaOapg.properties.defaultMode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sources: typing.Union[MetaOapg.properties.sources, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1ProjectedVolumeSource':
        return super().__new__(
            cls,
            *args,
            defaultMode=defaultMode,
            sources=sources,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_volume_projection import V1VolumeProjection
