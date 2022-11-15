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


class V1PersistentVolumeClaimStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PersistentVolumeClaimStatus is the current status of a persistent volume claim.
    """


    class MetaOapg:
        
        class properties:
            
            
            class accessModes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accessModes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class allocatedResources(
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
                ) -> 'allocatedResources':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class capacity(
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
                ) -> 'capacity':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1PersistentVolumeClaimCondition']:
                        return V1PersistentVolumeClaimCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1PersistentVolumeClaimCondition'], typing.List['V1PersistentVolumeClaimCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1PersistentVolumeClaimCondition':
                    return super().__getitem__(i)
            phase = schemas.StrSchema
            resizeStatus = schemas.StrSchema
            __annotations__ = {
                "accessModes": accessModes,
                "allocatedResources": allocatedResources,
                "capacity": capacity,
                "conditions": conditions,
                "phase": phase,
                "resizeStatus": resizeStatus,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessModes"]) -> MetaOapg.properties.accessModes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allocatedResources"]) -> MetaOapg.properties.allocatedResources: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phase"]) -> MetaOapg.properties.phase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resizeStatus"]) -> MetaOapg.properties.resizeStatus: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accessModes", "allocatedResources", "capacity", "conditions", "phase", "resizeStatus", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessModes"]) -> typing.Union[MetaOapg.properties.accessModes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allocatedResources"]) -> typing.Union[MetaOapg.properties.allocatedResources, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> typing.Union[MetaOapg.properties.capacity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phase"]) -> typing.Union[MetaOapg.properties.phase, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resizeStatus"]) -> typing.Union[MetaOapg.properties.resizeStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accessModes", "allocatedResources", "capacity", "conditions", "phase", "resizeStatus", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accessModes: typing.Union[MetaOapg.properties.accessModes, list, tuple, schemas.Unset] = schemas.unset,
        allocatedResources: typing.Union[MetaOapg.properties.allocatedResources, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        capacity: typing.Union[MetaOapg.properties.capacity, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, schemas.Unset] = schemas.unset,
        phase: typing.Union[MetaOapg.properties.phase, str, schemas.Unset] = schemas.unset,
        resizeStatus: typing.Union[MetaOapg.properties.resizeStatus, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1PersistentVolumeClaimStatus':
        return super().__new__(
            cls,
            *args,
            accessModes=accessModes,
            allocatedResources=allocatedResources,
            capacity=capacity,
            conditions=conditions,
            phase=phase,
            resizeStatus=resizeStatus,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_persistent_volume_claim_condition import V1PersistentVolumeClaimCondition