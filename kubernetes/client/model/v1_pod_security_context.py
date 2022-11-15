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


class V1PodSecurityContext(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext.  Field values of container.securityContext take precedence over field values of PodSecurityContext.
    """


    class MetaOapg:
        
        class properties:
            fsGroup = schemas.Int64Schema
            fsGroupChangePolicy = schemas.StrSchema
            runAsGroup = schemas.Int64Schema
            runAsNonRoot = schemas.BoolSchema
            runAsUser = schemas.Int64Schema
        
            @staticmethod
            def seLinuxOptions() -> typing.Type['V1SELinuxOptions']:
                return V1SELinuxOptions
        
            @staticmethod
            def seccompProfile() -> typing.Type['V1SeccompProfile']:
                return V1SeccompProfile
            
            
            class supplementalGroups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'supplementalGroups':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class sysctls(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1Sysctl']:
                        return V1Sysctl
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1Sysctl'], typing.List['V1Sysctl']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sysctls':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1Sysctl':
                    return super().__getitem__(i)
        
            @staticmethod
            def windowsOptions() -> typing.Type['V1WindowsSecurityContextOptions']:
                return V1WindowsSecurityContextOptions
            __annotations__ = {
                "fsGroup": fsGroup,
                "fsGroupChangePolicy": fsGroupChangePolicy,
                "runAsGroup": runAsGroup,
                "runAsNonRoot": runAsNonRoot,
                "runAsUser": runAsUser,
                "seLinuxOptions": seLinuxOptions,
                "seccompProfile": seccompProfile,
                "supplementalGroups": supplementalGroups,
                "sysctls": sysctls,
                "windowsOptions": windowsOptions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fsGroup"]) -> MetaOapg.properties.fsGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fsGroupChangePolicy"]) -> MetaOapg.properties.fsGroupChangePolicy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runAsGroup"]) -> MetaOapg.properties.runAsGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runAsNonRoot"]) -> MetaOapg.properties.runAsNonRoot: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runAsUser"]) -> MetaOapg.properties.runAsUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seLinuxOptions"]) -> 'V1SELinuxOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seccompProfile"]) -> 'V1SeccompProfile': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supplementalGroups"]) -> MetaOapg.properties.supplementalGroups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sysctls"]) -> MetaOapg.properties.sysctls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["windowsOptions"]) -> 'V1WindowsSecurityContextOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fsGroup", "fsGroupChangePolicy", "runAsGroup", "runAsNonRoot", "runAsUser", "seLinuxOptions", "seccompProfile", "supplementalGroups", "sysctls", "windowsOptions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fsGroup"]) -> typing.Union[MetaOapg.properties.fsGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fsGroupChangePolicy"]) -> typing.Union[MetaOapg.properties.fsGroupChangePolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runAsGroup"]) -> typing.Union[MetaOapg.properties.runAsGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runAsNonRoot"]) -> typing.Union[MetaOapg.properties.runAsNonRoot, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runAsUser"]) -> typing.Union[MetaOapg.properties.runAsUser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seLinuxOptions"]) -> typing.Union['V1SELinuxOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seccompProfile"]) -> typing.Union['V1SeccompProfile', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supplementalGroups"]) -> typing.Union[MetaOapg.properties.supplementalGroups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sysctls"]) -> typing.Union[MetaOapg.properties.sysctls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["windowsOptions"]) -> typing.Union['V1WindowsSecurityContextOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fsGroup", "fsGroupChangePolicy", "runAsGroup", "runAsNonRoot", "runAsUser", "seLinuxOptions", "seccompProfile", "supplementalGroups", "sysctls", "windowsOptions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        fsGroup: typing.Union[MetaOapg.properties.fsGroup, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fsGroupChangePolicy: typing.Union[MetaOapg.properties.fsGroupChangePolicy, str, schemas.Unset] = schemas.unset,
        runAsGroup: typing.Union[MetaOapg.properties.runAsGroup, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        runAsNonRoot: typing.Union[MetaOapg.properties.runAsNonRoot, bool, schemas.Unset] = schemas.unset,
        runAsUser: typing.Union[MetaOapg.properties.runAsUser, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        seLinuxOptions: typing.Union['V1SELinuxOptions', schemas.Unset] = schemas.unset,
        seccompProfile: typing.Union['V1SeccompProfile', schemas.Unset] = schemas.unset,
        supplementalGroups: typing.Union[MetaOapg.properties.supplementalGroups, list, tuple, schemas.Unset] = schemas.unset,
        sysctls: typing.Union[MetaOapg.properties.sysctls, list, tuple, schemas.Unset] = schemas.unset,
        windowsOptions: typing.Union['V1WindowsSecurityContextOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1PodSecurityContext':
        return super().__new__(
            cls,
            *args,
            fsGroup=fsGroup,
            fsGroupChangePolicy=fsGroupChangePolicy,
            runAsGroup=runAsGroup,
            runAsNonRoot=runAsNonRoot,
            runAsUser=runAsUser,
            seLinuxOptions=seLinuxOptions,
            seccompProfile=seccompProfile,
            supplementalGroups=supplementalGroups,
            sysctls=sysctls,
            windowsOptions=windowsOptions,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_se_linux_options import V1SELinuxOptions
from kubernetes.client.model.v1_seccomp_profile import V1SeccompProfile
from kubernetes.client.model.v1_sysctl import V1Sysctl
from kubernetes.client.model.v1_windows_security_context_options import V1WindowsSecurityContextOptions