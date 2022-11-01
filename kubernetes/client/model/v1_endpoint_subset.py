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


class V1EndpointSubset(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:

	{
	  Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
	  Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
	}

The resulting set of endpoints can be viewed as:

	a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
	b: [ 10.10.1.1:309, 10.10.2.2:309 ]
    """


    class MetaOapg:
        
        class properties:
            
            
            class addresses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1EndpointAddress']:
                        return V1EndpointAddress
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1EndpointAddress'], typing.List['V1EndpointAddress']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addresses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1EndpointAddress':
                    return super().__getitem__(i)
            
            
            class notReadyAddresses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1EndpointAddress']:
                        return V1EndpointAddress
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1EndpointAddress'], typing.List['V1EndpointAddress']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'notReadyAddresses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1EndpointAddress':
                    return super().__getitem__(i)
            
            
            class ports(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CoreV1EndpointPort']:
                        return CoreV1EndpointPort
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CoreV1EndpointPort'], typing.List['CoreV1EndpointPort']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ports':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CoreV1EndpointPort':
                    return super().__getitem__(i)
            __annotations__ = {
                "addresses": addresses,
                "notReadyAddresses": notReadyAddresses,
                "ports": ports,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addresses"]) -> MetaOapg.properties.addresses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notReadyAddresses"]) -> MetaOapg.properties.notReadyAddresses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ports"]) -> MetaOapg.properties.ports: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["addresses", "notReadyAddresses", "ports", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addresses"]) -> typing.Union[MetaOapg.properties.addresses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notReadyAddresses"]) -> typing.Union[MetaOapg.properties.notReadyAddresses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ports"]) -> typing.Union[MetaOapg.properties.ports, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addresses", "notReadyAddresses", "ports", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        addresses: typing.Union[MetaOapg.properties.addresses, list, tuple, schemas.Unset] = schemas.unset,
        notReadyAddresses: typing.Union[MetaOapg.properties.notReadyAddresses, list, tuple, schemas.Unset] = schemas.unset,
        ports: typing.Union[MetaOapg.properties.ports, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1EndpointSubset':
        return super().__new__(
            cls,
            *args,
            addresses=addresses,
            notReadyAddresses=notReadyAddresses,
            ports=ports,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.core_v1_endpoint_port import CoreV1EndpointPort
from kubernetes.client.model.v1_endpoint_address import V1EndpointAddress
