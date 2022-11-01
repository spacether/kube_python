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


class V1IngressClassSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    IngressClassSpec provides information about the class of an Ingress.
    """


    class MetaOapg:
        
        class properties:
            controller = schemas.StrSchema
        
            @staticmethod
            def parameters() -> typing.Type['V1IngressClassParametersReference']:
                return V1IngressClassParametersReference
            __annotations__ = {
                "controller": controller,
                "parameters": parameters,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["controller"]) -> MetaOapg.properties.controller: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameters"]) -> 'V1IngressClassParametersReference': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["controller", "parameters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["controller"]) -> typing.Union[MetaOapg.properties.controller, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameters"]) -> typing.Union['V1IngressClassParametersReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["controller", "parameters", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        controller: typing.Union[MetaOapg.properties.controller, str, schemas.Unset] = schemas.unset,
        parameters: typing.Union['V1IngressClassParametersReference', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1IngressClassSpec':
        return super().__new__(
            cls,
            *args,
            controller=controller,
            parameters=parameters,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_ingress_class_parameters_reference import V1IngressClassParametersReference
