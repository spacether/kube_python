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


class V1CustomResourceDefinitionSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CustomResourceDefinitionSpec describes how a user wants their resource to appear
    """


    class MetaOapg:
        required = {
            "names",
            "versions",
            "scope",
            "group",
        }
        
        class properties:
            group = schemas.StrSchema
        
            @staticmethod
            def names() -> typing.Type['V1CustomResourceDefinitionNames']:
                return V1CustomResourceDefinitionNames
            scope = schemas.StrSchema
            
            
            class versions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1CustomResourceDefinitionVersion']:
                        return V1CustomResourceDefinitionVersion
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1CustomResourceDefinitionVersion'], typing.List['V1CustomResourceDefinitionVersion']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'versions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1CustomResourceDefinitionVersion':
                    return super().__getitem__(i)
        
            @staticmethod
            def conversion() -> typing.Type['V1CustomResourceConversion']:
                return V1CustomResourceConversion
            preserveUnknownFields = schemas.BoolSchema
            __annotations__ = {
                "group": group,
                "names": names,
                "scope": scope,
                "versions": versions,
                "conversion": conversion,
                "preserveUnknownFields": preserveUnknownFields,
            }
    
    names: 'V1CustomResourceDefinitionNames'
    versions: MetaOapg.properties.versions
    scope: MetaOapg.properties.scope
    group: MetaOapg.properties.group
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group"]) -> MetaOapg.properties.group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["names"]) -> 'V1CustomResourceDefinitionNames': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versions"]) -> MetaOapg.properties.versions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversion"]) -> 'V1CustomResourceConversion': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preserveUnknownFields"]) -> MetaOapg.properties.preserveUnknownFields: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["group", "names", "scope", "versions", "conversion", "preserveUnknownFields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group"]) -> MetaOapg.properties.group: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["names"]) -> 'V1CustomResourceDefinitionNames': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versions"]) -> MetaOapg.properties.versions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversion"]) -> typing.Union['V1CustomResourceConversion', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preserveUnknownFields"]) -> typing.Union[MetaOapg.properties.preserveUnknownFields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["group", "names", "scope", "versions", "conversion", "preserveUnknownFields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        names: 'V1CustomResourceDefinitionNames',
        versions: typing.Union[MetaOapg.properties.versions, list, tuple, ],
        scope: typing.Union[MetaOapg.properties.scope, str, ],
        group: typing.Union[MetaOapg.properties.group, str, ],
        conversion: typing.Union['V1CustomResourceConversion', schemas.Unset] = schemas.unset,
        preserveUnknownFields: typing.Union[MetaOapg.properties.preserveUnknownFields, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1CustomResourceDefinitionSpec':
        return super().__new__(
            cls,
            *args,
            names=names,
            versions=versions,
            scope=scope,
            group=group,
            conversion=conversion,
            preserveUnknownFields=preserveUnknownFields,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_custom_resource_conversion import V1CustomResourceConversion
from client.model.v1_custom_resource_definition_names import V1CustomResourceDefinitionNames
from client.model.v1_custom_resource_definition_version import V1CustomResourceDefinitionVersion
