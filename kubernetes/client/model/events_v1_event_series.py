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


class EventsV1EventSeries(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations.
    """


    class MetaOapg:
        required = {
            "count",
            "lastObservedTime",
        }
        
        class properties:
            count = schemas.Int32Schema
            lastObservedTime = schemas.DateTimeSchema
            __annotations__ = {
                "count": count,
                "lastObservedTime": lastObservedTime,
            }
    
    count: MetaOapg.properties.count
    lastObservedTime: MetaOapg.properties.lastObservedTime
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastObservedTime"]) -> MetaOapg.properties.lastObservedTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["count", "lastObservedTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastObservedTime"]) -> MetaOapg.properties.lastObservedTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["count", "lastObservedTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, ],
        lastObservedTime: typing.Union[MetaOapg.properties.lastObservedTime, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventsV1EventSeries':
        return super().__new__(
            cls,
            *args,
            count=count,
            lastObservedTime=lastObservedTime,
            _configuration=_configuration,
            **kwargs,
        )
