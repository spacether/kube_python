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


class V1DeleteOptions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    DeleteOptions may be provided when deleting an API object.
    """


    class MetaOapg:
        
        class properties:
            apiVersion = schemas.StrSchema
            
            
            class dryRun(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dryRun':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            gracePeriodSeconds = schemas.Int64Schema
            kind = schemas.StrSchema
            orphanDependents = schemas.BoolSchema
        
            @staticmethod
            def preconditions() -> typing.Type['V1Preconditions']:
                return V1Preconditions
            propagationPolicy = schemas.StrSchema
            __annotations__ = {
                "apiVersion": apiVersion,
                "dryRun": dryRun,
                "gracePeriodSeconds": gracePeriodSeconds,
                "kind": kind,
                "orphanDependents": orphanDependents,
                "preconditions": preconditions,
                "propagationPolicy": propagationPolicy,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiVersion"]) -> MetaOapg.properties.apiVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dryRun"]) -> MetaOapg.properties.dryRun: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gracePeriodSeconds"]) -> MetaOapg.properties.gracePeriodSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orphanDependents"]) -> MetaOapg.properties.orphanDependents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preconditions"]) -> 'V1Preconditions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["propagationPolicy"]) -> MetaOapg.properties.propagationPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["apiVersion", "dryRun", "gracePeriodSeconds", "kind", "orphanDependents", "preconditions", "propagationPolicy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiVersion"]) -> typing.Union[MetaOapg.properties.apiVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dryRun"]) -> typing.Union[MetaOapg.properties.dryRun, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gracePeriodSeconds"]) -> typing.Union[MetaOapg.properties.gracePeriodSeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union[MetaOapg.properties.kind, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orphanDependents"]) -> typing.Union[MetaOapg.properties.orphanDependents, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preconditions"]) -> typing.Union['V1Preconditions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["propagationPolicy"]) -> typing.Union[MetaOapg.properties.propagationPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["apiVersion", "dryRun", "gracePeriodSeconds", "kind", "orphanDependents", "preconditions", "propagationPolicy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        apiVersion: typing.Union[MetaOapg.properties.apiVersion, str, schemas.Unset] = schemas.unset,
        dryRun: typing.Union[MetaOapg.properties.dryRun, list, tuple, schemas.Unset] = schemas.unset,
        gracePeriodSeconds: typing.Union[MetaOapg.properties.gracePeriodSeconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        kind: typing.Union[MetaOapg.properties.kind, str, schemas.Unset] = schemas.unset,
        orphanDependents: typing.Union[MetaOapg.properties.orphanDependents, bool, schemas.Unset] = schemas.unset,
        preconditions: typing.Union['V1Preconditions', schemas.Unset] = schemas.unset,
        propagationPolicy: typing.Union[MetaOapg.properties.propagationPolicy, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1DeleteOptions':
        return super().__new__(
            cls,
            *args,
            apiVersion=apiVersion,
            dryRun=dryRun,
            gracePeriodSeconds=gracePeriodSeconds,
            kind=kind,
            orphanDependents=orphanDependents,
            preconditions=preconditions,
            propagationPolicy=propagationPolicy,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_preconditions import V1Preconditions
