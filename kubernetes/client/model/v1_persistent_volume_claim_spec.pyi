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


class V1PersistentVolumeClaimSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes
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
        
            @staticmethod
            def dataSource() -> typing.Type['V1TypedLocalObjectReference']:
                return V1TypedLocalObjectReference
        
            @staticmethod
            def dataSourceRef() -> typing.Type['V1TypedLocalObjectReference']:
                return V1TypedLocalObjectReference
        
            @staticmethod
            def resources() -> typing.Type['V1ResourceRequirements']:
                return V1ResourceRequirements
        
            @staticmethod
            def selector() -> typing.Type['V1LabelSelector']:
                return V1LabelSelector
            storageClassName = schemas.StrSchema
            volumeMode = schemas.StrSchema
            volumeName = schemas.StrSchema
            __annotations__ = {
                "accessModes": accessModes,
                "dataSource": dataSource,
                "dataSourceRef": dataSourceRef,
                "resources": resources,
                "selector": selector,
                "storageClassName": storageClassName,
                "volumeMode": volumeMode,
                "volumeName": volumeName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessModes"]) -> MetaOapg.properties.accessModes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataSource"]) -> 'V1TypedLocalObjectReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataSourceRef"]) -> 'V1TypedLocalObjectReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> 'V1ResourceRequirements': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selector"]) -> 'V1LabelSelector': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storageClassName"]) -> MetaOapg.properties.storageClassName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volumeMode"]) -> MetaOapg.properties.volumeMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volumeName"]) -> MetaOapg.properties.volumeName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accessModes", "dataSource", "dataSourceRef", "resources", "selector", "storageClassName", "volumeMode", "volumeName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessModes"]) -> typing.Union[MetaOapg.properties.accessModes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataSource"]) -> typing.Union['V1TypedLocalObjectReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataSourceRef"]) -> typing.Union['V1TypedLocalObjectReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> typing.Union['V1ResourceRequirements', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selector"]) -> typing.Union['V1LabelSelector', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storageClassName"]) -> typing.Union[MetaOapg.properties.storageClassName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volumeMode"]) -> typing.Union[MetaOapg.properties.volumeMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volumeName"]) -> typing.Union[MetaOapg.properties.volumeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accessModes", "dataSource", "dataSourceRef", "resources", "selector", "storageClassName", "volumeMode", "volumeName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accessModes: typing.Union[MetaOapg.properties.accessModes, list, tuple, schemas.Unset] = schemas.unset,
        dataSource: typing.Union['V1TypedLocalObjectReference', schemas.Unset] = schemas.unset,
        dataSourceRef: typing.Union['V1TypedLocalObjectReference', schemas.Unset] = schemas.unset,
        resources: typing.Union['V1ResourceRequirements', schemas.Unset] = schemas.unset,
        selector: typing.Union['V1LabelSelector', schemas.Unset] = schemas.unset,
        storageClassName: typing.Union[MetaOapg.properties.storageClassName, str, schemas.Unset] = schemas.unset,
        volumeMode: typing.Union[MetaOapg.properties.volumeMode, str, schemas.Unset] = schemas.unset,
        volumeName: typing.Union[MetaOapg.properties.volumeName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1PersistentVolumeClaimSpec':
        return super().__new__(
            cls,
            *args,
            accessModes=accessModes,
            dataSource=dataSource,
            dataSourceRef=dataSourceRef,
            resources=resources,
            selector=selector,
            storageClassName=storageClassName,
            volumeMode=volumeMode,
            volumeName=volumeName,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_label_selector import V1LabelSelector
from client.model.v1_resource_requirements import V1ResourceRequirements
from client.model.v1_typed_local_object_reference import V1TypedLocalObjectReference