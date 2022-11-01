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


class V1AggregationRule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole
    """


    class MetaOapg:
        
        class properties:
            
            
            class clusterRoleSelectors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1LabelSelector']:
                        return V1LabelSelector
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1LabelSelector'], typing.List['V1LabelSelector']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'clusterRoleSelectors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1LabelSelector':
                    return super().__getitem__(i)
            __annotations__ = {
                "clusterRoleSelectors": clusterRoleSelectors,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clusterRoleSelectors"]) -> MetaOapg.properties.clusterRoleSelectors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["clusterRoleSelectors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clusterRoleSelectors"]) -> typing.Union[MetaOapg.properties.clusterRoleSelectors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["clusterRoleSelectors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        clusterRoleSelectors: typing.Union[MetaOapg.properties.clusterRoleSelectors, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1AggregationRule':
        return super().__new__(
            cls,
            *args,
            clusterRoleSelectors=clusterRoleSelectors,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_label_selector import V1LabelSelector
