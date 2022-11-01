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


class AdmissionregistrationV1WebhookClientConfig(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    WebhookClientConfig contains the information to make a TLS connection with the webhook
    """


    class MetaOapg:
        
        class properties:
            
            
            class caBundle(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'byte'
                    regex=[{
                        'pattern': r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$',  # noqa: E501
                    }]
        
            @staticmethod
            def service() -> typing.Type['AdmissionregistrationV1ServiceReference']:
                return AdmissionregistrationV1ServiceReference
            url = schemas.StrSchema
            __annotations__ = {
                "caBundle": caBundle,
                "service": service,
                "url": url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caBundle"]) -> MetaOapg.properties.caBundle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service"]) -> 'AdmissionregistrationV1ServiceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["caBundle", "service", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caBundle"]) -> typing.Union[MetaOapg.properties.caBundle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service"]) -> typing.Union['AdmissionregistrationV1ServiceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["caBundle", "service", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        caBundle: typing.Union[MetaOapg.properties.caBundle, str, schemas.Unset] = schemas.unset,
        service: typing.Union['AdmissionregistrationV1ServiceReference', schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdmissionregistrationV1WebhookClientConfig':
        return super().__new__(
            cls,
            *args,
            caBundle=caBundle,
            service=service,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.admissionregistration_v1_service_reference import AdmissionregistrationV1ServiceReference
