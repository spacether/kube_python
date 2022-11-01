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


class V1PodAntiAffinity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Pod anti affinity is a group of inter pod anti affinity scheduling rules.
    """


    class MetaOapg:
        
        class properties:
            
            
            class preferredDuringSchedulingIgnoredDuringExecution(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1WeightedPodAffinityTerm']:
                        return V1WeightedPodAffinityTerm
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1WeightedPodAffinityTerm'], typing.List['V1WeightedPodAffinityTerm']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'preferredDuringSchedulingIgnoredDuringExecution':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1WeightedPodAffinityTerm':
                    return super().__getitem__(i)
            
            
            class requiredDuringSchedulingIgnoredDuringExecution(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1PodAffinityTerm']:
                        return V1PodAffinityTerm
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1PodAffinityTerm'], typing.List['V1PodAffinityTerm']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'requiredDuringSchedulingIgnoredDuringExecution':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1PodAffinityTerm':
                    return super().__getitem__(i)
            __annotations__ = {
                "preferredDuringSchedulingIgnoredDuringExecution": preferredDuringSchedulingIgnoredDuringExecution,
                "requiredDuringSchedulingIgnoredDuringExecution": requiredDuringSchedulingIgnoredDuringExecution,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferredDuringSchedulingIgnoredDuringExecution"]) -> MetaOapg.properties.preferredDuringSchedulingIgnoredDuringExecution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requiredDuringSchedulingIgnoredDuringExecution"]) -> MetaOapg.properties.requiredDuringSchedulingIgnoredDuringExecution: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["preferredDuringSchedulingIgnoredDuringExecution", "requiredDuringSchedulingIgnoredDuringExecution", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferredDuringSchedulingIgnoredDuringExecution"]) -> typing.Union[MetaOapg.properties.preferredDuringSchedulingIgnoredDuringExecution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requiredDuringSchedulingIgnoredDuringExecution"]) -> typing.Union[MetaOapg.properties.requiredDuringSchedulingIgnoredDuringExecution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["preferredDuringSchedulingIgnoredDuringExecution", "requiredDuringSchedulingIgnoredDuringExecution", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        preferredDuringSchedulingIgnoredDuringExecution: typing.Union[MetaOapg.properties.preferredDuringSchedulingIgnoredDuringExecution, list, tuple, schemas.Unset] = schemas.unset,
        requiredDuringSchedulingIgnoredDuringExecution: typing.Union[MetaOapg.properties.requiredDuringSchedulingIgnoredDuringExecution, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1PodAntiAffinity':
        return super().__new__(
            cls,
            *args,
            preferredDuringSchedulingIgnoredDuringExecution=preferredDuringSchedulingIgnoredDuringExecution,
            requiredDuringSchedulingIgnoredDuringExecution=requiredDuringSchedulingIgnoredDuringExecution,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_pod_affinity_term import V1PodAffinityTerm
from client.model.v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm
