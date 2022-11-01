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


class V1CustomResourceDefinitionVersion(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CustomResourceDefinitionVersion describes a version for CRD.
    """


    class MetaOapg:
        required = {
            "served",
            "name",
            "storage",
        }
        
        class properties:
            name = schemas.StrSchema
            served = schemas.BoolSchema
            storage = schemas.BoolSchema
            
            
            class additionalPrinterColumns(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1CustomResourceColumnDefinition']:
                        return V1CustomResourceColumnDefinition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1CustomResourceColumnDefinition'], typing.List['V1CustomResourceColumnDefinition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'additionalPrinterColumns':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1CustomResourceColumnDefinition':
                    return super().__getitem__(i)
            deprecated = schemas.BoolSchema
            deprecationWarning = schemas.StrSchema
        
            @staticmethod
            def schema() -> typing.Type['V1CustomResourceValidation']:
                return V1CustomResourceValidation
        
            @staticmethod
            def subresources() -> typing.Type['V1CustomResourceSubresources']:
                return V1CustomResourceSubresources
            __annotations__ = {
                "name": name,
                "served": served,
                "storage": storage,
                "additionalPrinterColumns": additionalPrinterColumns,
                "deprecated": deprecated,
                "deprecationWarning": deprecationWarning,
                "schema": schema,
                "subresources": subresources,
            }
    
    served: MetaOapg.properties.served
    name: MetaOapg.properties.name
    storage: MetaOapg.properties.storage
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["served"]) -> MetaOapg.properties.served: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storage"]) -> MetaOapg.properties.storage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalPrinterColumns"]) -> MetaOapg.properties.additionalPrinterColumns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deprecated"]) -> MetaOapg.properties.deprecated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deprecationWarning"]) -> MetaOapg.properties.deprecationWarning: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema"]) -> 'V1CustomResourceValidation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subresources"]) -> 'V1CustomResourceSubresources': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "served", "storage", "additionalPrinterColumns", "deprecated", "deprecationWarning", "schema", "subresources", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["served"]) -> MetaOapg.properties.served: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storage"]) -> MetaOapg.properties.storage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionalPrinterColumns"]) -> typing.Union[MetaOapg.properties.additionalPrinterColumns, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deprecated"]) -> typing.Union[MetaOapg.properties.deprecated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deprecationWarning"]) -> typing.Union[MetaOapg.properties.deprecationWarning, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema"]) -> typing.Union['V1CustomResourceValidation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subresources"]) -> typing.Union['V1CustomResourceSubresources', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "served", "storage", "additionalPrinterColumns", "deprecated", "deprecationWarning", "schema", "subresources", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        served: typing.Union[MetaOapg.properties.served, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        storage: typing.Union[MetaOapg.properties.storage, bool, ],
        additionalPrinterColumns: typing.Union[MetaOapg.properties.additionalPrinterColumns, list, tuple, schemas.Unset] = schemas.unset,
        deprecated: typing.Union[MetaOapg.properties.deprecated, bool, schemas.Unset] = schemas.unset,
        deprecationWarning: typing.Union[MetaOapg.properties.deprecationWarning, str, schemas.Unset] = schemas.unset,
        schema: typing.Union['V1CustomResourceValidation', schemas.Unset] = schemas.unset,
        subresources: typing.Union['V1CustomResourceSubresources', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1CustomResourceDefinitionVersion':
        return super().__new__(
            cls,
            *args,
            served=served,
            name=name,
            storage=storage,
            additionalPrinterColumns=additionalPrinterColumns,
            deprecated=deprecated,
            deprecationWarning=deprecationWarning,
            schema=schema,
            subresources=subresources,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_custom_resource_column_definition import V1CustomResourceColumnDefinition
from kubernetes.client.model.v1_custom_resource_subresources import V1CustomResourceSubresources
from kubernetes.client.model.v1_custom_resource_validation import V1CustomResourceValidation
