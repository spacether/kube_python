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


class V1beta1PriorityLevelConfigurationStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PriorityLevelConfigurationStatus represents the current state of a "request-priority".
    """


    class MetaOapg:
        
        class properties:
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1beta1PriorityLevelConfigurationCondition']:
                        return V1beta1PriorityLevelConfigurationCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1beta1PriorityLevelConfigurationCondition'], typing.List['V1beta1PriorityLevelConfigurationCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1beta1PriorityLevelConfigurationCondition':
                    return super().__getitem__(i)
            __annotations__ = {
                "conditions": conditions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conditions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conditions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1beta1PriorityLevelConfigurationStatus':
        return super().__new__(
            cls,
            *args,
            conditions=conditions,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1beta1_priority_level_configuration_condition import V1beta1PriorityLevelConfigurationCondition
