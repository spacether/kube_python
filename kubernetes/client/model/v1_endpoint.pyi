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


class V1Endpoint(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Endpoint represents a single logical "backend" implementing a service.
    """


    class MetaOapg:
        required = {
            "addresses",
        }
        
        class properties:
            
            
            class addresses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addresses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def conditions() -> typing.Type['V1EndpointConditions']:
                return V1EndpointConditions
            
            
            class deprecatedTopology(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'deprecatedTopology':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def hints() -> typing.Type['V1EndpointHints']:
                return V1EndpointHints
            hostname = schemas.StrSchema
            nodeName = schemas.StrSchema
        
            @staticmethod
            def targetRef() -> typing.Type['V1ObjectReference']:
                return V1ObjectReference
            zone = schemas.StrSchema
            __annotations__ = {
                "addresses": addresses,
                "conditions": conditions,
                "deprecatedTopology": deprecatedTopology,
                "hints": hints,
                "hostname": hostname,
                "nodeName": nodeName,
                "targetRef": targetRef,
                "zone": zone,
            }
    
    addresses: MetaOapg.properties.addresses
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addresses"]) -> MetaOapg.properties.addresses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> 'V1EndpointConditions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deprecatedTopology"]) -> MetaOapg.properties.deprecatedTopology: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hints"]) -> 'V1EndpointHints': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeName"]) -> MetaOapg.properties.nodeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetRef"]) -> 'V1ObjectReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zone"]) -> MetaOapg.properties.zone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["addresses", "conditions", "deprecatedTopology", "hints", "hostname", "nodeName", "targetRef", "zone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addresses"]) -> MetaOapg.properties.addresses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union['V1EndpointConditions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deprecatedTopology"]) -> typing.Union[MetaOapg.properties.deprecatedTopology, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hints"]) -> typing.Union['V1EndpointHints', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeName"]) -> typing.Union[MetaOapg.properties.nodeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetRef"]) -> typing.Union['V1ObjectReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zone"]) -> typing.Union[MetaOapg.properties.zone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addresses", "conditions", "deprecatedTopology", "hints", "hostname", "nodeName", "targetRef", "zone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        addresses: typing.Union[MetaOapg.properties.addresses, list, tuple, ],
        conditions: typing.Union['V1EndpointConditions', schemas.Unset] = schemas.unset,
        deprecatedTopology: typing.Union[MetaOapg.properties.deprecatedTopology, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        hints: typing.Union['V1EndpointHints', schemas.Unset] = schemas.unset,
        hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
        nodeName: typing.Union[MetaOapg.properties.nodeName, str, schemas.Unset] = schemas.unset,
        targetRef: typing.Union['V1ObjectReference', schemas.Unset] = schemas.unset,
        zone: typing.Union[MetaOapg.properties.zone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1Endpoint':
        return super().__new__(
            cls,
            *args,
            addresses=addresses,
            conditions=conditions,
            deprecatedTopology=deprecatedTopology,
            hints=hints,
            hostname=hostname,
            nodeName=nodeName,
            targetRef=targetRef,
            zone=zone,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_endpoint_conditions import V1EndpointConditions
from client.model.v1_endpoint_hints import V1EndpointHints
from client.model.v1_object_reference import V1ObjectReference
