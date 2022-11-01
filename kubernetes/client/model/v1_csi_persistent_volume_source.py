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


class V1CSIPersistentVolumeSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents storage that is managed by an external CSI volume driver (Beta feature)
    """


    class MetaOapg:
        required = {
            "driver",
            "volumeHandle",
        }
        
        class properties:
            driver = schemas.StrSchema
            volumeHandle = schemas.StrSchema
        
            @staticmethod
            def controllerExpandSecretRef() -> typing.Type['V1SecretReference']:
                return V1SecretReference
        
            @staticmethod
            def controllerPublishSecretRef() -> typing.Type['V1SecretReference']:
                return V1SecretReference
            fsType = schemas.StrSchema
        
            @staticmethod
            def nodeExpandSecretRef() -> typing.Type['V1SecretReference']:
                return V1SecretReference
        
            @staticmethod
            def nodePublishSecretRef() -> typing.Type['V1SecretReference']:
                return V1SecretReference
        
            @staticmethod
            def nodeStageSecretRef() -> typing.Type['V1SecretReference']:
                return V1SecretReference
            readOnly = schemas.BoolSchema
            
            
            class volumeAttributes(
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
                ) -> 'volumeAttributes':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "driver": driver,
                "volumeHandle": volumeHandle,
                "controllerExpandSecretRef": controllerExpandSecretRef,
                "controllerPublishSecretRef": controllerPublishSecretRef,
                "fsType": fsType,
                "nodeExpandSecretRef": nodeExpandSecretRef,
                "nodePublishSecretRef": nodePublishSecretRef,
                "nodeStageSecretRef": nodeStageSecretRef,
                "readOnly": readOnly,
                "volumeAttributes": volumeAttributes,
            }
    
    driver: MetaOapg.properties.driver
    volumeHandle: MetaOapg.properties.volumeHandle
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["driver"]) -> MetaOapg.properties.driver: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volumeHandle"]) -> MetaOapg.properties.volumeHandle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["controllerExpandSecretRef"]) -> 'V1SecretReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["controllerPublishSecretRef"]) -> 'V1SecretReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fsType"]) -> MetaOapg.properties.fsType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeExpandSecretRef"]) -> 'V1SecretReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodePublishSecretRef"]) -> 'V1SecretReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeStageSecretRef"]) -> 'V1SecretReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readOnly"]) -> MetaOapg.properties.readOnly: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volumeAttributes"]) -> MetaOapg.properties.volumeAttributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["driver", "volumeHandle", "controllerExpandSecretRef", "controllerPublishSecretRef", "fsType", "nodeExpandSecretRef", "nodePublishSecretRef", "nodeStageSecretRef", "readOnly", "volumeAttributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["driver"]) -> MetaOapg.properties.driver: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volumeHandle"]) -> MetaOapg.properties.volumeHandle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["controllerExpandSecretRef"]) -> typing.Union['V1SecretReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["controllerPublishSecretRef"]) -> typing.Union['V1SecretReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fsType"]) -> typing.Union[MetaOapg.properties.fsType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeExpandSecretRef"]) -> typing.Union['V1SecretReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodePublishSecretRef"]) -> typing.Union['V1SecretReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeStageSecretRef"]) -> typing.Union['V1SecretReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readOnly"]) -> typing.Union[MetaOapg.properties.readOnly, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volumeAttributes"]) -> typing.Union[MetaOapg.properties.volumeAttributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["driver", "volumeHandle", "controllerExpandSecretRef", "controllerPublishSecretRef", "fsType", "nodeExpandSecretRef", "nodePublishSecretRef", "nodeStageSecretRef", "readOnly", "volumeAttributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        driver: typing.Union[MetaOapg.properties.driver, str, ],
        volumeHandle: typing.Union[MetaOapg.properties.volumeHandle, str, ],
        controllerExpandSecretRef: typing.Union['V1SecretReference', schemas.Unset] = schemas.unset,
        controllerPublishSecretRef: typing.Union['V1SecretReference', schemas.Unset] = schemas.unset,
        fsType: typing.Union[MetaOapg.properties.fsType, str, schemas.Unset] = schemas.unset,
        nodeExpandSecretRef: typing.Union['V1SecretReference', schemas.Unset] = schemas.unset,
        nodePublishSecretRef: typing.Union['V1SecretReference', schemas.Unset] = schemas.unset,
        nodeStageSecretRef: typing.Union['V1SecretReference', schemas.Unset] = schemas.unset,
        readOnly: typing.Union[MetaOapg.properties.readOnly, bool, schemas.Unset] = schemas.unset,
        volumeAttributes: typing.Union[MetaOapg.properties.volumeAttributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1CSIPersistentVolumeSource':
        return super().__new__(
            cls,
            *args,
            driver=driver,
            volumeHandle=volumeHandle,
            controllerExpandSecretRef=controllerExpandSecretRef,
            controllerPublishSecretRef=controllerPublishSecretRef,
            fsType=fsType,
            nodeExpandSecretRef=nodeExpandSecretRef,
            nodePublishSecretRef=nodePublishSecretRef,
            nodeStageSecretRef=nodeStageSecretRef,
            readOnly=readOnly,
            volumeAttributes=volumeAttributes,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_secret_reference import V1SecretReference
