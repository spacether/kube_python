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


class V1HTTPIngressRuleValue(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example: http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this resource will be used to match against everything after the last '/' and before the first '?' or '#'.
    """


    class MetaOapg:
        required = {
            "paths",
        }
        
        class properties:
            
            
            class paths(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1HTTPIngressPath']:
                        return V1HTTPIngressPath
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1HTTPIngressPath'], typing.List['V1HTTPIngressPath']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'paths':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1HTTPIngressPath':
                    return super().__getitem__(i)
            __annotations__ = {
                "paths": paths,
            }
    
    paths: MetaOapg.properties.paths
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paths"]) -> MetaOapg.properties.paths: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["paths", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paths"]) -> MetaOapg.properties.paths: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["paths", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        paths: typing.Union[MetaOapg.properties.paths, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1HTTPIngressRuleValue':
        return super().__new__(
            cls,
            *args,
            paths=paths,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_http_ingress_path import V1HTTPIngressPath
