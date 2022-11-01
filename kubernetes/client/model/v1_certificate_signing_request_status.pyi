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


class V1CertificateSigningRequestStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate.
    """


    class MetaOapg:
        
        class properties:
            
            
            class certificate(
                schemas.StrSchema
            ):
                pass
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1CertificateSigningRequestCondition']:
                        return V1CertificateSigningRequestCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1CertificateSigningRequestCondition'], typing.List['V1CertificateSigningRequestCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1CertificateSigningRequestCondition':
                    return super().__getitem__(i)
            __annotations__ = {
                "certificate": certificate,
                "conditions": conditions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["certificate"]) -> MetaOapg.properties.certificate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["certificate", "conditions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["certificate"]) -> typing.Union[MetaOapg.properties.certificate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["certificate", "conditions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        certificate: typing.Union[MetaOapg.properties.certificate, str, schemas.Unset] = schemas.unset,
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1CertificateSigningRequestStatus':
        return super().__new__(
            cls,
            *args,
            certificate=certificate,
            conditions=conditions,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_certificate_signing_request_condition import V1CertificateSigningRequestCondition
