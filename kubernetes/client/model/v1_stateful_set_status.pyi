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


class V1StatefulSetStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    StatefulSetStatus represents the current state of a StatefulSet.
    """


    class MetaOapg:
        required = {
            "replicas",
        }
        
        class properties:
            replicas = schemas.Int32Schema
            availableReplicas = schemas.Int32Schema
            collisionCount = schemas.Int32Schema
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1StatefulSetCondition']:
                        return V1StatefulSetCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1StatefulSetCondition'], typing.List['V1StatefulSetCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1StatefulSetCondition':
                    return super().__getitem__(i)
            currentReplicas = schemas.Int32Schema
            currentRevision = schemas.StrSchema
            observedGeneration = schemas.Int64Schema
            readyReplicas = schemas.Int32Schema
            updateRevision = schemas.StrSchema
            updatedReplicas = schemas.Int32Schema
            __annotations__ = {
                "replicas": replicas,
                "availableReplicas": availableReplicas,
                "collisionCount": collisionCount,
                "conditions": conditions,
                "currentReplicas": currentReplicas,
                "currentRevision": currentRevision,
                "observedGeneration": observedGeneration,
                "readyReplicas": readyReplicas,
                "updateRevision": updateRevision,
                "updatedReplicas": updatedReplicas,
            }
    
    replicas: MetaOapg.properties.replicas
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replicas"]) -> MetaOapg.properties.replicas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableReplicas"]) -> MetaOapg.properties.availableReplicas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collisionCount"]) -> MetaOapg.properties.collisionCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentReplicas"]) -> MetaOapg.properties.currentReplicas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentRevision"]) -> MetaOapg.properties.currentRevision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["observedGeneration"]) -> MetaOapg.properties.observedGeneration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readyReplicas"]) -> MetaOapg.properties.readyReplicas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateRevision"]) -> MetaOapg.properties.updateRevision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedReplicas"]) -> MetaOapg.properties.updatedReplicas: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["replicas", "availableReplicas", "collisionCount", "conditions", "currentReplicas", "currentRevision", "observedGeneration", "readyReplicas", "updateRevision", "updatedReplicas", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replicas"]) -> MetaOapg.properties.replicas: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableReplicas"]) -> typing.Union[MetaOapg.properties.availableReplicas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collisionCount"]) -> typing.Union[MetaOapg.properties.collisionCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentReplicas"]) -> typing.Union[MetaOapg.properties.currentReplicas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentRevision"]) -> typing.Union[MetaOapg.properties.currentRevision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["observedGeneration"]) -> typing.Union[MetaOapg.properties.observedGeneration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readyReplicas"]) -> typing.Union[MetaOapg.properties.readyReplicas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateRevision"]) -> typing.Union[MetaOapg.properties.updateRevision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedReplicas"]) -> typing.Union[MetaOapg.properties.updatedReplicas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["replicas", "availableReplicas", "collisionCount", "conditions", "currentReplicas", "currentRevision", "observedGeneration", "readyReplicas", "updateRevision", "updatedReplicas", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        replicas: typing.Union[MetaOapg.properties.replicas, decimal.Decimal, int, ],
        availableReplicas: typing.Union[MetaOapg.properties.availableReplicas, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        collisionCount: typing.Union[MetaOapg.properties.collisionCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, schemas.Unset] = schemas.unset,
        currentReplicas: typing.Union[MetaOapg.properties.currentReplicas, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currentRevision: typing.Union[MetaOapg.properties.currentRevision, str, schemas.Unset] = schemas.unset,
        observedGeneration: typing.Union[MetaOapg.properties.observedGeneration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        readyReplicas: typing.Union[MetaOapg.properties.readyReplicas, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updateRevision: typing.Union[MetaOapg.properties.updateRevision, str, schemas.Unset] = schemas.unset,
        updatedReplicas: typing.Union[MetaOapg.properties.updatedReplicas, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1StatefulSetStatus':
        return super().__new__(
            cls,
            *args,
            replicas=replicas,
            availableReplicas=availableReplicas,
            collisionCount=collisionCount,
            conditions=conditions,
            currentReplicas=currentReplicas,
            currentRevision=currentRevision,
            observedGeneration=observedGeneration,
            readyReplicas=readyReplicas,
            updateRevision=updateRevision,
            updatedReplicas=updatedReplicas,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_stateful_set_condition import V1StatefulSetCondition
