# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from kubernetes.client import api_client, exceptions
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

from kubernetes.client.model.v1_persistent_volume_claim_list import V1PersistentVolumeClaimList

from . import path

# Query params
AllowWatchBookmarksSchema = schemas.BoolSchema
ModelContinueSchema = schemas.StrSchema
FieldSelectorSchema = schemas.StrSchema
LabelSelectorSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
PrettySchema = schemas.StrSchema
ResourceVersionSchema = schemas.StrSchema
ResourceVersionMatchSchema = schemas.StrSchema
TimeoutSecondsSchema = schemas.IntSchema
WatchSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'allowWatchBookmarks': typing.Union[AllowWatchBookmarksSchema, bool, ],
        'continue': typing.Union[ModelContinueSchema, str, ],
        'fieldSelector': typing.Union[FieldSelectorSchema, str, ],
        'labelSelector': typing.Union[LabelSelectorSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'pretty': typing.Union[PrettySchema, str, ],
        'resourceVersion': typing.Union[ResourceVersionSchema, str, ],
        'resourceVersionMatch': typing.Union[ResourceVersionMatchSchema, str, ],
        'timeoutSeconds': typing.Union[TimeoutSecondsSchema, decimal.Decimal, int, ],
        'watch': typing.Union[WatchSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_allow_watch_bookmarks = api_client.QueryParameter(
    name="allowWatchBookmarks",
    schema=AllowWatchBookmarksSchema,
)
request_query__continue = api_client.QueryParameter(
    name="continue",
    schema=ModelContinueSchema,
)
request_query_field_selector = api_client.QueryParameter(
    name="fieldSelector",
    schema=FieldSelectorSchema,
)
request_query_label_selector = api_client.QueryParameter(
    name="labelSelector",
    schema=LabelSelectorSchema,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    schema=LimitSchema,
)
request_query_pretty = api_client.QueryParameter(
    name="pretty",
    schema=PrettySchema,
)
request_query_resource_version = api_client.QueryParameter(
    name="resourceVersion",
    schema=ResourceVersionSchema,
)
request_query_resource_version_match = api_client.QueryParameter(
    name="resourceVersionMatch",
    schema=ResourceVersionMatchSchema,
)
request_query_timeout_seconds = api_client.QueryParameter(
    name="timeoutSeconds",
    schema=TimeoutSecondsSchema,
)
request_query_watch = api_client.QueryParameter(
    name="watch",
    schema=WatchSchema,
)
_auth = [
    'BearerToken',
]
SchemaFor200ResponseBodyApplicationJson = V1PersistentVolumeClaimList
SchemaFor200ResponseBodyApplicationYaml = V1PersistentVolumeClaimList
SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf = V1PersistentVolumeClaimList
SchemaFor200ResponseBodyApplicationJsonstreamwatch = V1PersistentVolumeClaimList
SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch = V1PersistentVolumeClaimList


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyApplicationYaml,
        SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf,
        SchemaFor200ResponseBodyApplicationJsonstreamwatch,
        SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/yaml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationYaml),
        'application/vnd.kubernetes.protobuf': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf),
        'application/json;stream=watch': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonstreamwatch),
        'application/vnd.kubernetes.protobuf;stream=watch': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch),
    },
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
    'application/yaml',
    'application/vnd.kubernetes.protobuf',
    'application/json;stream=watch',
    'application/vnd.kubernetes.protobuf;stream=watch',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _list_persistent_volume_claim_for_all_namespaces_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _list_persistent_volume_claim_for_all_namespaces_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _list_persistent_volume_claim_for_all_namespaces_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _list_persistent_volume_claim_for_all_namespaces_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_allow_watch_bookmarks,
            request_query__continue,
            request_query_field_selector,
            request_query_label_selector,
            request_query_limit,
            request_query_pretty,
            request_query_resource_version,
            request_query_resource_version_match,
            request_query_timeout_seconds,
            request_query_watch,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class ListPersistentVolumeClaimForAllNamespaces(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def list_persistent_volume_claim_for_all_namespaces(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def list_persistent_volume_claim_for_all_namespaces(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def list_persistent_volume_claim_for_all_namespaces(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def list_persistent_volume_claim_for_all_namespaces(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._list_persistent_volume_claim_for_all_namespaces_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._list_persistent_volume_claim_for_all_namespaces_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


