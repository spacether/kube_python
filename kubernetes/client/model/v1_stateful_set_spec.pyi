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


class V1StatefulSetSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A StatefulSetSpec is the specification of a StatefulSet.
    """


    class MetaOapg:
        required = {
            "template",
            "selector",
            "serviceName",
        }
        
        class properties:
        
            @staticmethod
            def selector() -> typing.Type['V1LabelSelector']:
                return V1LabelSelector
            serviceName = schemas.StrSchema
        
            @staticmethod
            def template() -> typing.Type['V1PodTemplateSpec']:
                return V1PodTemplateSpec
            minReadySeconds = schemas.Int32Schema
        
            @staticmethod
            def persistentVolumeClaimRetentionPolicy() -> typing.Type['V1StatefulSetPersistentVolumeClaimRetentionPolicy']:
                return V1StatefulSetPersistentVolumeClaimRetentionPolicy
            podManagementPolicy = schemas.StrSchema
            replicas = schemas.Int32Schema
            revisionHistoryLimit = schemas.Int32Schema
        
            @staticmethod
            def updateStrategy() -> typing.Type['V1StatefulSetUpdateStrategy']:
                return V1StatefulSetUpdateStrategy
            
            
            class volumeClaimTemplates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1PersistentVolumeClaim']:
                        return V1PersistentVolumeClaim
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1PersistentVolumeClaim'], typing.List['V1PersistentVolumeClaim']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'volumeClaimTemplates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1PersistentVolumeClaim':
                    return super().__getitem__(i)
            __annotations__ = {
                "selector": selector,
                "serviceName": serviceName,
                "template": template,
                "minReadySeconds": minReadySeconds,
                "persistentVolumeClaimRetentionPolicy": persistentVolumeClaimRetentionPolicy,
                "podManagementPolicy": podManagementPolicy,
                "replicas": replicas,
                "revisionHistoryLimit": revisionHistoryLimit,
                "updateStrategy": updateStrategy,
                "volumeClaimTemplates": volumeClaimTemplates,
            }
    
    template: 'V1PodTemplateSpec'
    selector: 'V1LabelSelector'
    serviceName: MetaOapg.properties.serviceName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selector"]) -> 'V1LabelSelector': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceName"]) -> MetaOapg.properties.serviceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template"]) -> 'V1PodTemplateSpec': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minReadySeconds"]) -> MetaOapg.properties.minReadySeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["persistentVolumeClaimRetentionPolicy"]) -> 'V1StatefulSetPersistentVolumeClaimRetentionPolicy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["podManagementPolicy"]) -> MetaOapg.properties.podManagementPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replicas"]) -> MetaOapg.properties.replicas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revisionHistoryLimit"]) -> MetaOapg.properties.revisionHistoryLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateStrategy"]) -> 'V1StatefulSetUpdateStrategy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volumeClaimTemplates"]) -> MetaOapg.properties.volumeClaimTemplates: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["selector", "serviceName", "template", "minReadySeconds", "persistentVolumeClaimRetentionPolicy", "podManagementPolicy", "replicas", "revisionHistoryLimit", "updateStrategy", "volumeClaimTemplates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selector"]) -> 'V1LabelSelector': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceName"]) -> MetaOapg.properties.serviceName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> 'V1PodTemplateSpec': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minReadySeconds"]) -> typing.Union[MetaOapg.properties.minReadySeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["persistentVolumeClaimRetentionPolicy"]) -> typing.Union['V1StatefulSetPersistentVolumeClaimRetentionPolicy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["podManagementPolicy"]) -> typing.Union[MetaOapg.properties.podManagementPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replicas"]) -> typing.Union[MetaOapg.properties.replicas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revisionHistoryLimit"]) -> typing.Union[MetaOapg.properties.revisionHistoryLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateStrategy"]) -> typing.Union['V1StatefulSetUpdateStrategy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volumeClaimTemplates"]) -> typing.Union[MetaOapg.properties.volumeClaimTemplates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["selector", "serviceName", "template", "minReadySeconds", "persistentVolumeClaimRetentionPolicy", "podManagementPolicy", "replicas", "revisionHistoryLimit", "updateStrategy", "volumeClaimTemplates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        template: 'V1PodTemplateSpec',
        selector: 'V1LabelSelector',
        serviceName: typing.Union[MetaOapg.properties.serviceName, str, ],
        minReadySeconds: typing.Union[MetaOapg.properties.minReadySeconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        persistentVolumeClaimRetentionPolicy: typing.Union['V1StatefulSetPersistentVolumeClaimRetentionPolicy', schemas.Unset] = schemas.unset,
        podManagementPolicy: typing.Union[MetaOapg.properties.podManagementPolicy, str, schemas.Unset] = schemas.unset,
        replicas: typing.Union[MetaOapg.properties.replicas, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        revisionHistoryLimit: typing.Union[MetaOapg.properties.revisionHistoryLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updateStrategy: typing.Union['V1StatefulSetUpdateStrategy', schemas.Unset] = schemas.unset,
        volumeClaimTemplates: typing.Union[MetaOapg.properties.volumeClaimTemplates, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1StatefulSetSpec':
        return super().__new__(
            cls,
            *args,
            template=template,
            selector=selector,
            serviceName=serviceName,
            minReadySeconds=minReadySeconds,
            persistentVolumeClaimRetentionPolicy=persistentVolumeClaimRetentionPolicy,
            podManagementPolicy=podManagementPolicy,
            replicas=replicas,
            revisionHistoryLimit=revisionHistoryLimit,
            updateStrategy=updateStrategy,
            volumeClaimTemplates=volumeClaimTemplates,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_label_selector import V1LabelSelector
from client.model.v1_persistent_volume_claim import V1PersistentVolumeClaim
from client.model.v1_pod_template_spec import V1PodTemplateSpec
from client.model.v1_stateful_set_persistent_volume_claim_retention_policy import V1StatefulSetPersistentVolumeClaimRetentionPolicy
from client.model.v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy
