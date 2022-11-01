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


class V1ReplicationControllerSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ReplicationControllerSpec is the specification of a replication controller.
    """


    class MetaOapg:
        
        class properties:
            minReadySeconds = schemas.Int32Schema
            replicas = schemas.Int32Schema
            
            
            class selector(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'selector':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def template() -> typing.Type['V1PodTemplateSpec']:
                return V1PodTemplateSpec
            __annotations__ = {
                "minReadySeconds": minReadySeconds,
                "replicas": replicas,
                "selector": selector,
                "template": template,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minReadySeconds"]) -> MetaOapg.properties.minReadySeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replicas"]) -> MetaOapg.properties.replicas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selector"]) -> MetaOapg.properties.selector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template"]) -> 'V1PodTemplateSpec': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["minReadySeconds", "replicas", "selector", "template", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minReadySeconds"]) -> typing.Union[MetaOapg.properties.minReadySeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replicas"]) -> typing.Union[MetaOapg.properties.replicas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selector"]) -> typing.Union[MetaOapg.properties.selector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> typing.Union['V1PodTemplateSpec', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["minReadySeconds", "replicas", "selector", "template", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        minReadySeconds: typing.Union[MetaOapg.properties.minReadySeconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        replicas: typing.Union[MetaOapg.properties.replicas, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        selector: typing.Union[MetaOapg.properties.selector, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        template: typing.Union['V1PodTemplateSpec', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1ReplicationControllerSpec':
        return super().__new__(
            cls,
            *args,
            minReadySeconds=minReadySeconds,
            replicas=replicas,
            selector=selector,
            template=template,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_pod_template_spec import V1PodTemplateSpec
