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


class V1SubjectAccessReviewSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    SubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set
    """


    class MetaOapg:
        
        class properties:
            
            
            class extra(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            additional_properties = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.additional_properties, str, ]], typing.List[typing.Union[MetaOapg.additional_properties, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'extra':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class groups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'groups':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def nonResourceAttributes() -> typing.Type['V1NonResourceAttributes']:
                return V1NonResourceAttributes
        
            @staticmethod
            def resourceAttributes() -> typing.Type['V1ResourceAttributes']:
                return V1ResourceAttributes
            uid = schemas.StrSchema
            user = schemas.StrSchema
            __annotations__ = {
                "extra": extra,
                "groups": groups,
                "nonResourceAttributes": nonResourceAttributes,
                "resourceAttributes": resourceAttributes,
                "uid": uid,
                "user": user,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra"]) -> MetaOapg.properties.extra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groups"]) -> MetaOapg.properties.groups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonResourceAttributes"]) -> 'V1NonResourceAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceAttributes"]) -> 'V1ResourceAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["extra", "groups", "nonResourceAttributes", "resourceAttributes", "uid", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra"]) -> typing.Union[MetaOapg.properties.extra, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groups"]) -> typing.Union[MetaOapg.properties.groups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonResourceAttributes"]) -> typing.Union['V1NonResourceAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceAttributes"]) -> typing.Union['V1ResourceAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uid"]) -> typing.Union[MetaOapg.properties.uid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["extra", "groups", "nonResourceAttributes", "resourceAttributes", "uid", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        extra: typing.Union[MetaOapg.properties.extra, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        groups: typing.Union[MetaOapg.properties.groups, list, tuple, schemas.Unset] = schemas.unset,
        nonResourceAttributes: typing.Union['V1NonResourceAttributes', schemas.Unset] = schemas.unset,
        resourceAttributes: typing.Union['V1ResourceAttributes', schemas.Unset] = schemas.unset,
        uid: typing.Union[MetaOapg.properties.uid, str, schemas.Unset] = schemas.unset,
        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1SubjectAccessReviewSpec':
        return super().__new__(
            cls,
            *args,
            extra=extra,
            groups=groups,
            nonResourceAttributes=nonResourceAttributes,
            resourceAttributes=resourceAttributes,
            uid=uid,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_non_resource_attributes import V1NonResourceAttributes
from kubernetes.client.model.v1_resource_attributes import V1ResourceAttributes
