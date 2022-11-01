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


class V1OwnerReference(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.
    """


    class MetaOapg:
        required = {
            "uid",
            "apiVersion",
            "kind",
            "name",
        }
        
        class properties:
            apiVersion = schemas.StrSchema
            kind = schemas.StrSchema
            name = schemas.StrSchema
            uid = schemas.StrSchema
            blockOwnerDeletion = schemas.BoolSchema
            controller = schemas.BoolSchema
            __annotations__ = {
                "apiVersion": apiVersion,
                "kind": kind,
                "name": name,
                "uid": uid,
                "blockOwnerDeletion": blockOwnerDeletion,
                "controller": controller,
            }
    
    uid: MetaOapg.properties.uid
    apiVersion: MetaOapg.properties.apiVersion
    kind: MetaOapg.properties.kind
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiVersion"]) -> MetaOapg.properties.apiVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockOwnerDeletion"]) -> MetaOapg.properties.blockOwnerDeletion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["controller"]) -> MetaOapg.properties.controller: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["apiVersion", "kind", "name", "uid", "blockOwnerDeletion", "controller", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiVersion"]) -> MetaOapg.properties.apiVersion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockOwnerDeletion"]) -> typing.Union[MetaOapg.properties.blockOwnerDeletion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["controller"]) -> typing.Union[MetaOapg.properties.controller, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["apiVersion", "kind", "name", "uid", "blockOwnerDeletion", "controller", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        uid: typing.Union[MetaOapg.properties.uid, str, ],
        apiVersion: typing.Union[MetaOapg.properties.apiVersion, str, ],
        kind: typing.Union[MetaOapg.properties.kind, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        blockOwnerDeletion: typing.Union[MetaOapg.properties.blockOwnerDeletion, bool, schemas.Unset] = schemas.unset,
        controller: typing.Union[MetaOapg.properties.controller, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1OwnerReference':
        return super().__new__(
            cls,
            *args,
            uid=uid,
            apiVersion=apiVersion,
            kind=kind,
            name=name,
            blockOwnerDeletion=blockOwnerDeletion,
            controller=controller,
            _configuration=_configuration,
            **kwargs,
        )
