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


class V1CSINode(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to create the CSINode object directly. As long as they use the node-driver-registrar sidecar container, the kubelet will automatically populate the CSINode object for the CSI driver as part of kubelet plugin registration. CSINode has the same name as a node. If the object is missing, it means either there are no CSI Drivers available on the node, or the Kubelet version is low enough that it doesn't create this object. CSINode has an OwnerReference that points to the corresponding node object.
    """


    class MetaOapg:
        required = {
            "spec",
        }
        
        class properties:
        
            @staticmethod
            def spec() -> typing.Type['V1CSINodeSpec']:
                return V1CSINodeSpec
            apiVersion = schemas.StrSchema
            kind = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['V1ObjectMeta']:
                return V1ObjectMeta
            __annotations__ = {
                "spec": spec,
                "apiVersion": apiVersion,
                "kind": kind,
                "metadata": metadata,
            }
    
    spec: 'V1CSINodeSpec'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spec"]) -> 'V1CSINodeSpec': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiVersion"]) -> MetaOapg.properties.apiVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'V1ObjectMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["spec", "apiVersion", "kind", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spec"]) -> 'V1CSINodeSpec': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiVersion"]) -> typing.Union[MetaOapg.properties.apiVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union[MetaOapg.properties.kind, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['V1ObjectMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["spec", "apiVersion", "kind", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        spec: 'V1CSINodeSpec',
        apiVersion: typing.Union[MetaOapg.properties.apiVersion, str, schemas.Unset] = schemas.unset,
        kind: typing.Union[MetaOapg.properties.kind, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['V1ObjectMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1CSINode':
        return super().__new__(
            cls,
            *args,
            spec=spec,
            apiVersion=apiVersion,
            kind=kind,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_csi_node_spec import V1CSINodeSpec
from client.model.v1_object_meta import V1ObjectMeta
