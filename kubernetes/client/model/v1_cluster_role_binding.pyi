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


class V1ClusterRoleBinding(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ClusterRoleBinding references a ClusterRole, but not contain it.  It can reference a ClusterRole in the global namespace, and adds who information via Subject.
    """


    class MetaOapg:
        required = {
            "roleRef",
        }
        
        class properties:
        
            @staticmethod
            def roleRef() -> typing.Type['V1RoleRef']:
                return V1RoleRef
            apiVersion = schemas.StrSchema
            kind = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['V1ObjectMeta']:
                return V1ObjectMeta
            
            
            class subjects(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1Subject']:
                        return V1Subject
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1Subject'], typing.List['V1Subject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'subjects':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1Subject':
                    return super().__getitem__(i)
            __annotations__ = {
                "roleRef": roleRef,
                "apiVersion": apiVersion,
                "kind": kind,
                "metadata": metadata,
                "subjects": subjects,
            }
    
    roleRef: 'V1RoleRef'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleRef"]) -> 'V1RoleRef': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiVersion"]) -> MetaOapg.properties.apiVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'V1ObjectMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subjects"]) -> MetaOapg.properties.subjects: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["roleRef", "apiVersion", "kind", "metadata", "subjects", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleRef"]) -> 'V1RoleRef': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiVersion"]) -> typing.Union[MetaOapg.properties.apiVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union[MetaOapg.properties.kind, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['V1ObjectMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subjects"]) -> typing.Union[MetaOapg.properties.subjects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["roleRef", "apiVersion", "kind", "metadata", "subjects", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        roleRef: 'V1RoleRef',
        apiVersion: typing.Union[MetaOapg.properties.apiVersion, str, schemas.Unset] = schemas.unset,
        kind: typing.Union[MetaOapg.properties.kind, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['V1ObjectMeta', schemas.Unset] = schemas.unset,
        subjects: typing.Union[MetaOapg.properties.subjects, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1ClusterRoleBinding':
        return super().__new__(
            cls,
            *args,
            roleRef=roleRef,
            apiVersion=apiVersion,
            kind=kind,
            metadata=metadata,
            subjects=subjects,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_object_meta import V1ObjectMeta
from client.model.v1_role_ref import V1RoleRef
from client.model.v1_subject import V1Subject