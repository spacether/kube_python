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


class V1NodeSelectorTerm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
    """


    class MetaOapg:
        
        class properties:
            
            
            class matchExpressions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1NodeSelectorRequirement']:
                        return V1NodeSelectorRequirement
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1NodeSelectorRequirement'], typing.List['V1NodeSelectorRequirement']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matchExpressions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1NodeSelectorRequirement':
                    return super().__getitem__(i)
            
            
            class matchFields(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1NodeSelectorRequirement']:
                        return V1NodeSelectorRequirement
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1NodeSelectorRequirement'], typing.List['V1NodeSelectorRequirement']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matchFields':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1NodeSelectorRequirement':
                    return super().__getitem__(i)
            __annotations__ = {
                "matchExpressions": matchExpressions,
                "matchFields": matchFields,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchExpressions"]) -> MetaOapg.properties.matchExpressions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchFields"]) -> MetaOapg.properties.matchFields: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["matchExpressions", "matchFields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchExpressions"]) -> typing.Union[MetaOapg.properties.matchExpressions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchFields"]) -> typing.Union[MetaOapg.properties.matchFields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["matchExpressions", "matchFields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        matchExpressions: typing.Union[MetaOapg.properties.matchExpressions, list, tuple, schemas.Unset] = schemas.unset,
        matchFields: typing.Union[MetaOapg.properties.matchFields, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1NodeSelectorTerm':
        return super().__new__(
            cls,
            *args,
            matchExpressions=matchExpressions,
            matchFields=matchFields,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_node_selector_requirement import V1NodeSelectorRequirement
