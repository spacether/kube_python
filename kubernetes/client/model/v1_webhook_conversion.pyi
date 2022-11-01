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


class V1WebhookConversion(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    WebhookConversion describes how to call a conversion webhook
    """


    class MetaOapg:
        required = {
            "conversionReviewVersions",
        }
        
        class properties:
            
            
            class conversionReviewVersions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conversionReviewVersions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def clientConfig() -> typing.Type['ApiextensionsV1WebhookClientConfig']:
                return ApiextensionsV1WebhookClientConfig
            __annotations__ = {
                "conversionReviewVersions": conversionReviewVersions,
                "clientConfig": clientConfig,
            }
    
    conversionReviewVersions: MetaOapg.properties.conversionReviewVersions
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversionReviewVersions"]) -> MetaOapg.properties.conversionReviewVersions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientConfig"]) -> 'ApiextensionsV1WebhookClientConfig': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conversionReviewVersions", "clientConfig", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversionReviewVersions"]) -> MetaOapg.properties.conversionReviewVersions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientConfig"]) -> typing.Union['ApiextensionsV1WebhookClientConfig', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conversionReviewVersions", "clientConfig", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        conversionReviewVersions: typing.Union[MetaOapg.properties.conversionReviewVersions, list, tuple, ],
        clientConfig: typing.Union['ApiextensionsV1WebhookClientConfig', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1WebhookConversion':
        return super().__new__(
            cls,
            *args,
            conversionReviewVersions=conversionReviewVersions,
            clientConfig=clientConfig,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.apiextensions_v1_webhook_client_config import ApiextensionsV1WebhookClientConfig
