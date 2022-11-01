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


class V2HorizontalPodAutoscalerStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.
    """


    class MetaOapg:
        required = {
            "desiredReplicas",
        }
        
        class properties:
            desiredReplicas = schemas.Int32Schema
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V2HorizontalPodAutoscalerCondition']:
                        return V2HorizontalPodAutoscalerCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V2HorizontalPodAutoscalerCondition'], typing.List['V2HorizontalPodAutoscalerCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V2HorizontalPodAutoscalerCondition':
                    return super().__getitem__(i)
            
            
            class currentMetrics(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V2MetricStatus']:
                        return V2MetricStatus
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V2MetricStatus'], typing.List['V2MetricStatus']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'currentMetrics':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V2MetricStatus':
                    return super().__getitem__(i)
            currentReplicas = schemas.Int32Schema
            lastScaleTime = schemas.DateTimeSchema
            observedGeneration = schemas.Int64Schema
            __annotations__ = {
                "desiredReplicas": desiredReplicas,
                "conditions": conditions,
                "currentMetrics": currentMetrics,
                "currentReplicas": currentReplicas,
                "lastScaleTime": lastScaleTime,
                "observedGeneration": observedGeneration,
            }
    
    desiredReplicas: MetaOapg.properties.desiredReplicas
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["desiredReplicas"]) -> MetaOapg.properties.desiredReplicas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentMetrics"]) -> MetaOapg.properties.currentMetrics: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentReplicas"]) -> MetaOapg.properties.currentReplicas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastScaleTime"]) -> MetaOapg.properties.lastScaleTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["observedGeneration"]) -> MetaOapg.properties.observedGeneration: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["desiredReplicas", "conditions", "currentMetrics", "currentReplicas", "lastScaleTime", "observedGeneration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["desiredReplicas"]) -> MetaOapg.properties.desiredReplicas: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentMetrics"]) -> typing.Union[MetaOapg.properties.currentMetrics, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentReplicas"]) -> typing.Union[MetaOapg.properties.currentReplicas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastScaleTime"]) -> typing.Union[MetaOapg.properties.lastScaleTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["observedGeneration"]) -> typing.Union[MetaOapg.properties.observedGeneration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["desiredReplicas", "conditions", "currentMetrics", "currentReplicas", "lastScaleTime", "observedGeneration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        desiredReplicas: typing.Union[MetaOapg.properties.desiredReplicas, decimal.Decimal, int, ],
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, schemas.Unset] = schemas.unset,
        currentMetrics: typing.Union[MetaOapg.properties.currentMetrics, list, tuple, schemas.Unset] = schemas.unset,
        currentReplicas: typing.Union[MetaOapg.properties.currentReplicas, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        lastScaleTime: typing.Union[MetaOapg.properties.lastScaleTime, str, datetime, schemas.Unset] = schemas.unset,
        observedGeneration: typing.Union[MetaOapg.properties.observedGeneration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V2HorizontalPodAutoscalerStatus':
        return super().__new__(
            cls,
            *args,
            desiredReplicas=desiredReplicas,
            conditions=conditions,
            currentMetrics=currentMetrics,
            currentReplicas=currentReplicas,
            lastScaleTime=lastScaleTime,
            observedGeneration=observedGeneration,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition
from client.model.v2_metric_status import V2MetricStatus
