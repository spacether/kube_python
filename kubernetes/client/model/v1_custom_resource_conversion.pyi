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


class V1CustomResourceConversion(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CustomResourceConversion describes how to convert different versions of a CR.
    """


    class MetaOapg:
        required = {
            "strategy",
        }
        
        class properties:
            strategy = schemas.StrSchema
        
            @staticmethod
            def webhook() -> typing.Type['V1WebhookConversion']:
                return V1WebhookConversion
            __annotations__ = {
                "strategy": strategy,
                "webhook": webhook,
            }
    
    strategy: MetaOapg.properties.strategy
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strategy"]) -> MetaOapg.properties.strategy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook"]) -> 'V1WebhookConversion': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["strategy", "webhook", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strategy"]) -> MetaOapg.properties.strategy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook"]) -> typing.Union['V1WebhookConversion', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["strategy", "webhook", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        strategy: typing.Union[MetaOapg.properties.strategy, str, ],
        webhook: typing.Union['V1WebhookConversion', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1CustomResourceConversion':
        return super().__new__(
            cls,
            *args,
            strategy=strategy,
            webhook=webhook,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_webhook_conversion import V1WebhookConversion
