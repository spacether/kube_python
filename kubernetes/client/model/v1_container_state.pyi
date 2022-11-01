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


class V1ContainerState(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def running() -> typing.Type['V1ContainerStateRunning']:
                return V1ContainerStateRunning
        
            @staticmethod
            def terminated() -> typing.Type['V1ContainerStateTerminated']:
                return V1ContainerStateTerminated
        
            @staticmethod
            def waiting() -> typing.Type['V1ContainerStateWaiting']:
                return V1ContainerStateWaiting
            __annotations__ = {
                "running": running,
                "terminated": terminated,
                "waiting": waiting,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["running"]) -> 'V1ContainerStateRunning': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminated"]) -> 'V1ContainerStateTerminated': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["waiting"]) -> 'V1ContainerStateWaiting': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["running", "terminated", "waiting", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["running"]) -> typing.Union['V1ContainerStateRunning', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminated"]) -> typing.Union['V1ContainerStateTerminated', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["waiting"]) -> typing.Union['V1ContainerStateWaiting', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["running", "terminated", "waiting", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        running: typing.Union['V1ContainerStateRunning', schemas.Unset] = schemas.unset,
        terminated: typing.Union['V1ContainerStateTerminated', schemas.Unset] = schemas.unset,
        waiting: typing.Union['V1ContainerStateWaiting', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1ContainerState':
        return super().__new__(
            cls,
            *args,
            running=running,
            terminated=terminated,
            waiting=waiting,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_container_state_running import V1ContainerStateRunning
from client.model.v1_container_state_terminated import V1ContainerStateTerminated
from client.model.v1_container_state_waiting import V1ContainerStateWaiting
