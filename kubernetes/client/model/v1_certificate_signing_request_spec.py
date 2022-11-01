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


class V1CertificateSigningRequestSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CertificateSigningRequestSpec contains the certificate request.
    """


    class MetaOapg:
        required = {
            "request",
            "signerName",
        }
        
        class properties:
            
            
            class request(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'byte'
                    regex=[{
                        'pattern': r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$',  # noqa: E501
                    }]
            signerName = schemas.StrSchema
            expirationSeconds = schemas.Int32Schema
            
            
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
            uid = schemas.StrSchema
            
            
            class usages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'usages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            username = schemas.StrSchema
            __annotations__ = {
                "request": request,
                "signerName": signerName,
                "expirationSeconds": expirationSeconds,
                "extra": extra,
                "groups": groups,
                "uid": uid,
                "usages": usages,
                "username": username,
            }
    
    request: MetaOapg.properties.request
    signerName: MetaOapg.properties.signerName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request"]) -> MetaOapg.properties.request: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signerName"]) -> MetaOapg.properties.signerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationSeconds"]) -> MetaOapg.properties.expirationSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra"]) -> MetaOapg.properties.extra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groups"]) -> MetaOapg.properties.groups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usages"]) -> MetaOapg.properties.usages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["request", "signerName", "expirationSeconds", "extra", "groups", "uid", "usages", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request"]) -> MetaOapg.properties.request: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signerName"]) -> MetaOapg.properties.signerName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationSeconds"]) -> typing.Union[MetaOapg.properties.expirationSeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra"]) -> typing.Union[MetaOapg.properties.extra, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groups"]) -> typing.Union[MetaOapg.properties.groups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uid"]) -> typing.Union[MetaOapg.properties.uid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usages"]) -> typing.Union[MetaOapg.properties.usages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["request", "signerName", "expirationSeconds", "extra", "groups", "uid", "usages", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        request: typing.Union[MetaOapg.properties.request, str, ],
        signerName: typing.Union[MetaOapg.properties.signerName, str, ],
        expirationSeconds: typing.Union[MetaOapg.properties.expirationSeconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        extra: typing.Union[MetaOapg.properties.extra, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        groups: typing.Union[MetaOapg.properties.groups, list, tuple, schemas.Unset] = schemas.unset,
        uid: typing.Union[MetaOapg.properties.uid, str, schemas.Unset] = schemas.unset,
        usages: typing.Union[MetaOapg.properties.usages, list, tuple, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1CertificateSigningRequestSpec':
        return super().__new__(
            cls,
            *args,
            request=request,
            signerName=signerName,
            expirationSeconds=expirationSeconds,
            extra=extra,
            groups=groups,
            uid=uid,
            usages=usages,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )
