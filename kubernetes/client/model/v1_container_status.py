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


class V1ContainerStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ContainerStatus contains details for the current status of this container.
    """


    class MetaOapg:
        required = {
            "image",
            "imageID",
            "restartCount",
            "ready",
            "name",
        }
        
        class properties:
            image = schemas.StrSchema
            imageID = schemas.StrSchema
            name = schemas.StrSchema
            ready = schemas.BoolSchema
            restartCount = schemas.Int32Schema
            containerID = schemas.StrSchema
        
            @staticmethod
            def lastState() -> typing.Type['V1ContainerState']:
                return V1ContainerState
            started = schemas.BoolSchema
        
            @staticmethod
            def state() -> typing.Type['V1ContainerState']:
                return V1ContainerState
            __annotations__ = {
                "image": image,
                "imageID": imageID,
                "name": name,
                "ready": ready,
                "restartCount": restartCount,
                "containerID": containerID,
                "lastState": lastState,
                "started": started,
                "state": state,
            }
    
    image: MetaOapg.properties.image
    imageID: MetaOapg.properties.imageID
    restartCount: MetaOapg.properties.restartCount
    ready: MetaOapg.properties.ready
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageID"]) -> MetaOapg.properties.imageID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ready"]) -> MetaOapg.properties.ready: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restartCount"]) -> MetaOapg.properties.restartCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["containerID"]) -> MetaOapg.properties.containerID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastState"]) -> 'V1ContainerState': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["started"]) -> MetaOapg.properties.started: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> 'V1ContainerState': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["image", "imageID", "name", "ready", "restartCount", "containerID", "lastState", "started", "state", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageID"]) -> MetaOapg.properties.imageID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ready"]) -> MetaOapg.properties.ready: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restartCount"]) -> MetaOapg.properties.restartCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["containerID"]) -> typing.Union[MetaOapg.properties.containerID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastState"]) -> typing.Union['V1ContainerState', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["started"]) -> typing.Union[MetaOapg.properties.started, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union['V1ContainerState', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["image", "imageID", "name", "ready", "restartCount", "containerID", "lastState", "started", "state", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        image: typing.Union[MetaOapg.properties.image, str, ],
        imageID: typing.Union[MetaOapg.properties.imageID, str, ],
        restartCount: typing.Union[MetaOapg.properties.restartCount, decimal.Decimal, int, ],
        ready: typing.Union[MetaOapg.properties.ready, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        containerID: typing.Union[MetaOapg.properties.containerID, str, schemas.Unset] = schemas.unset,
        lastState: typing.Union['V1ContainerState', schemas.Unset] = schemas.unset,
        started: typing.Union[MetaOapg.properties.started, bool, schemas.Unset] = schemas.unset,
        state: typing.Union['V1ContainerState', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1ContainerStatus':
        return super().__new__(
            cls,
            *args,
            image=image,
            imageID=imageID,
            restartCount=restartCount,
            ready=ready,
            name=name,
            containerID=containerID,
            lastState=lastState,
            started=started,
            state=state,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_container_state import V1ContainerState
