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


class V1GitRepoVolumeSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.

DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    """


    class MetaOapg:
        required = {
            "repository",
        }
        
        class properties:
            repository = schemas.StrSchema
            directory = schemas.StrSchema
            revision = schemas.StrSchema
            __annotations__ = {
                "repository": repository,
                "directory": directory,
                "revision": revision,
            }
    
    repository: MetaOapg.properties.repository
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repository"]) -> MetaOapg.properties.repository: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directory"]) -> MetaOapg.properties.directory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revision"]) -> MetaOapg.properties.revision: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["repository", "directory", "revision", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repository"]) -> MetaOapg.properties.repository: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directory"]) -> typing.Union[MetaOapg.properties.directory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revision"]) -> typing.Union[MetaOapg.properties.revision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["repository", "directory", "revision", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        repository: typing.Union[MetaOapg.properties.repository, str, ],
        directory: typing.Union[MetaOapg.properties.directory, str, schemas.Unset] = schemas.unset,
        revision: typing.Union[MetaOapg.properties.revision, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1GitRepoVolumeSource':
        return super().__new__(
            cls,
            *args,
            repository=repository,
            directory=directory,
            revision=revision,
            _configuration=_configuration,
            **kwargs,
        )
