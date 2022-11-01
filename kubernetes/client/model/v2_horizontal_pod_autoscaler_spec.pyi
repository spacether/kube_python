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


class V2HorizontalPodAutoscalerSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    HorizontalPodAutoscalerSpec describes the desired functionality of the HorizontalPodAutoscaler.
    """


    class MetaOapg:
        required = {
            "maxReplicas",
            "scaleTargetRef",
        }
        
        class properties:
            maxReplicas = schemas.Int32Schema
        
            @staticmethod
            def scaleTargetRef() -> typing.Type['V2CrossVersionObjectReference']:
                return V2CrossVersionObjectReference
        
            @staticmethod
            def behavior() -> typing.Type['V2HorizontalPodAutoscalerBehavior']:
                return V2HorizontalPodAutoscalerBehavior
            
            
            class metrics(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V2MetricSpec']:
                        return V2MetricSpec
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V2MetricSpec'], typing.List['V2MetricSpec']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'metrics':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V2MetricSpec':
                    return super().__getitem__(i)
            minReplicas = schemas.Int32Schema
            __annotations__ = {
                "maxReplicas": maxReplicas,
                "scaleTargetRef": scaleTargetRef,
                "behavior": behavior,
                "metrics": metrics,
                "minReplicas": minReplicas,
            }
    
    maxReplicas: MetaOapg.properties.maxReplicas
    scaleTargetRef: 'V2CrossVersionObjectReference'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxReplicas"]) -> MetaOapg.properties.maxReplicas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scaleTargetRef"]) -> 'V2CrossVersionObjectReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["behavior"]) -> 'V2HorizontalPodAutoscalerBehavior': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metrics"]) -> MetaOapg.properties.metrics: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minReplicas"]) -> MetaOapg.properties.minReplicas: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxReplicas", "scaleTargetRef", "behavior", "metrics", "minReplicas", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxReplicas"]) -> MetaOapg.properties.maxReplicas: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scaleTargetRef"]) -> 'V2CrossVersionObjectReference': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["behavior"]) -> typing.Union['V2HorizontalPodAutoscalerBehavior', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metrics"]) -> typing.Union[MetaOapg.properties.metrics, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minReplicas"]) -> typing.Union[MetaOapg.properties.minReplicas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxReplicas", "scaleTargetRef", "behavior", "metrics", "minReplicas", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        maxReplicas: typing.Union[MetaOapg.properties.maxReplicas, decimal.Decimal, int, ],
        scaleTargetRef: 'V2CrossVersionObjectReference',
        behavior: typing.Union['V2HorizontalPodAutoscalerBehavior', schemas.Unset] = schemas.unset,
        metrics: typing.Union[MetaOapg.properties.metrics, list, tuple, schemas.Unset] = schemas.unset,
        minReplicas: typing.Union[MetaOapg.properties.minReplicas, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V2HorizontalPodAutoscalerSpec':
        return super().__new__(
            cls,
            *args,
            maxReplicas=maxReplicas,
            scaleTargetRef=scaleTargetRef,
            behavior=behavior,
            metrics=metrics,
            minReplicas=minReplicas,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v2_cross_version_object_reference import V2CrossVersionObjectReference
from client.model.v2_horizontal_pod_autoscaler_behavior import V2HorizontalPodAutoscalerBehavior
from client.model.v2_metric_spec import V2MetricSpec
