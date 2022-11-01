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


class V1APIResourceList(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    APIResourceList is a list of APIResource, it is used to expose the name of the resources supported in a specific group and version, and if the resource is namespaced.
    """


    class MetaOapg:
        required = {
            "groupVersion",
            "resources",
        }
        
        class properties:
            groupVersion = schemas.StrSchema
            
            
            class resources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1APIResource']:
                        return V1APIResource
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1APIResource'], typing.List['V1APIResource']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'resources':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1APIResource':
                    return super().__getitem__(i)
            apiVersion = schemas.StrSchema
            kind = schemas.StrSchema
            __annotations__ = {
                "groupVersion": groupVersion,
                "resources": resources,
                "apiVersion": apiVersion,
                "kind": kind,
            }
    
    groupVersion: MetaOapg.properties.groupVersion
    resources: MetaOapg.properties.resources
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupVersion"]) -> MetaOapg.properties.groupVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> MetaOapg.properties.resources: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiVersion"]) -> MetaOapg.properties.apiVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["groupVersion", "resources", "apiVersion", "kind", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupVersion"]) -> MetaOapg.properties.groupVersion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> MetaOapg.properties.resources: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiVersion"]) -> typing.Union[MetaOapg.properties.apiVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union[MetaOapg.properties.kind, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["groupVersion", "resources", "apiVersion", "kind", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        groupVersion: typing.Union[MetaOapg.properties.groupVersion, str, ],
        resources: typing.Union[MetaOapg.properties.resources, list, tuple, ],
        apiVersion: typing.Union[MetaOapg.properties.apiVersion, str, schemas.Unset] = schemas.unset,
        kind: typing.Union[MetaOapg.properties.kind, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1APIResourceList':
        return super().__new__(
            cls,
            *args,
            groupVersion=groupVersion,
            resources=resources,
            apiVersion=apiVersion,
            kind=kind,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_api_resource import V1APIResource
