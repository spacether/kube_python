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


class V1EphemeralVolumeSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents an ephemeral volume that is handled by a normal storage driver.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def volumeClaimTemplate() -> typing.Type['V1PersistentVolumeClaimTemplate']:
                return V1PersistentVolumeClaimTemplate
            __annotations__ = {
                "volumeClaimTemplate": volumeClaimTemplate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volumeClaimTemplate"]) -> 'V1PersistentVolumeClaimTemplate': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["volumeClaimTemplate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volumeClaimTemplate"]) -> typing.Union['V1PersistentVolumeClaimTemplate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["volumeClaimTemplate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        volumeClaimTemplate: typing.Union['V1PersistentVolumeClaimTemplate', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1EphemeralVolumeSource':
        return super().__new__(
            cls,
            *args,
            volumeClaimTemplate=volumeClaimTemplate,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_persistent_volume_claim_template import V1PersistentVolumeClaimTemplate
