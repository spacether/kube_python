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


class V1NetworkPolicyIngressRule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    NetworkPolicyIngressRule describes a particular set of traffic that is allowed to the pods matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and from.
    """


    class MetaOapg:
        
        class properties:
            
            
            class _from(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1NetworkPolicyPeer']:
                        return V1NetworkPolicyPeer
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1NetworkPolicyPeer'], typing.List['V1NetworkPolicyPeer']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> '_from':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1NetworkPolicyPeer':
                    return super().__getitem__(i)
            
            
            class ports(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1NetworkPolicyPort']:
                        return V1NetworkPolicyPort
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1NetworkPolicyPort'], typing.List['V1NetworkPolicyPort']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ports':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1NetworkPolicyPort':
                    return super().__getitem__(i)
            __annotations__ = {
                "from": _from,
                "ports": ports,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ports"]) -> MetaOapg.properties.ports: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["from", "ports", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ports"]) -> typing.Union[MetaOapg.properties.ports, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["from", "ports", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ports: typing.Union[MetaOapg.properties.ports, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1NetworkPolicyIngressRule':
        return super().__new__(
            cls,
            *args,
            ports=ports,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_network_policy_peer import V1NetworkPolicyPeer
from kubernetes.client.model.v1_network_policy_port import V1NetworkPolicyPort
