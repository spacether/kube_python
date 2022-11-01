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


class V1EndpointSlice(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints.
    """


    class MetaOapg:
        required = {
            "endpoints",
            "addressType",
        }
        
        class properties:
            addressType = schemas.StrSchema
            
            
            class endpoints(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1Endpoint']:
                        return V1Endpoint
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1Endpoint'], typing.List['V1Endpoint']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'endpoints':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1Endpoint':
                    return super().__getitem__(i)
            apiVersion = schemas.StrSchema
            kind = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['V1ObjectMeta']:
                return V1ObjectMeta
            
            
            class ports(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DiscoveryV1EndpointPort']:
                        return DiscoveryV1EndpointPort
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DiscoveryV1EndpointPort'], typing.List['DiscoveryV1EndpointPort']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ports':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DiscoveryV1EndpointPort':
                    return super().__getitem__(i)
            __annotations__ = {
                "addressType": addressType,
                "endpoints": endpoints,
                "apiVersion": apiVersion,
                "kind": kind,
                "metadata": metadata,
                "ports": ports,
            }
    
    endpoints: MetaOapg.properties.endpoints
    addressType: MetaOapg.properties.addressType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressType"]) -> MetaOapg.properties.addressType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoints"]) -> MetaOapg.properties.endpoints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiVersion"]) -> MetaOapg.properties.apiVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'V1ObjectMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ports"]) -> MetaOapg.properties.ports: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["addressType", "endpoints", "apiVersion", "kind", "metadata", "ports", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressType"]) -> MetaOapg.properties.addressType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoints"]) -> MetaOapg.properties.endpoints: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiVersion"]) -> typing.Union[MetaOapg.properties.apiVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union[MetaOapg.properties.kind, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['V1ObjectMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ports"]) -> typing.Union[MetaOapg.properties.ports, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addressType", "endpoints", "apiVersion", "kind", "metadata", "ports", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        endpoints: typing.Union[MetaOapg.properties.endpoints, list, tuple, ],
        addressType: typing.Union[MetaOapg.properties.addressType, str, ],
        apiVersion: typing.Union[MetaOapg.properties.apiVersion, str, schemas.Unset] = schemas.unset,
        kind: typing.Union[MetaOapg.properties.kind, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['V1ObjectMeta', schemas.Unset] = schemas.unset,
        ports: typing.Union[MetaOapg.properties.ports, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1EndpointSlice':
        return super().__new__(
            cls,
            *args,
            endpoints=endpoints,
            addressType=addressType,
            apiVersion=apiVersion,
            kind=kind,
            metadata=metadata,
            ports=ports,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.discovery_v1_endpoint_port import DiscoveryV1EndpointPort
from client.model.v1_endpoint import V1Endpoint
from client.model.v1_object_meta import V1ObjectMeta
