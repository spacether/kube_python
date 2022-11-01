# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from client import api_client, exceptions
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

from client.model.v1_delete_options import V1DeleteOptions
from client.model.v1_status import V1Status

# Query params
PrettySchema = schemas.StrSchema
ModelContinueSchema = schemas.StrSchema
DryRunSchema = schemas.StrSchema
FieldSelectorSchema = schemas.StrSchema
GracePeriodSecondsSchema = schemas.IntSchema
LabelSelectorSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
OrphanDependentsSchema = schemas.BoolSchema
PropagationPolicySchema = schemas.StrSchema
ResourceVersionSchema = schemas.StrSchema
ResourceVersionMatchSchema = schemas.StrSchema
TimeoutSecondsSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'pretty': typing.Union[PrettySchema, str, ],
        'continue': typing.Union[ModelContinueSchema, str, ],
        'dryRun': typing.Union[DryRunSchema, str, ],
        'fieldSelector': typing.Union[FieldSelectorSchema, str, ],
        'gracePeriodSeconds': typing.Union[GracePeriodSecondsSchema, decimal.Decimal, int, ],
        'labelSelector': typing.Union[LabelSelectorSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'orphanDependents': typing.Union[OrphanDependentsSchema, bool, ],
        'propagationPolicy': typing.Union[PropagationPolicySchema, str, ],
        'resourceVersion': typing.Union[ResourceVersionSchema, str, ],
        'resourceVersionMatch': typing.Union[ResourceVersionMatchSchema, str, ],
        'timeoutSeconds': typing.Union[TimeoutSecondsSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_pretty = api_client.QueryParameter(
    name="pretty",
    schema=PrettySchema,
)
request_query__continue = api_client.QueryParameter(
    name="continue",
    schema=ModelContinueSchema,
)
request_query_dry_run = api_client.QueryParameter(
    name="dryRun",
    schema=DryRunSchema,
)
request_query_field_selector = api_client.QueryParameter(
    name="fieldSelector",
    schema=FieldSelectorSchema,
)
request_query_grace_period_seconds = api_client.QueryParameter(
    name="gracePeriodSeconds",
    schema=GracePeriodSecondsSchema,
)
request_query_label_selector = api_client.QueryParameter(
    name="labelSelector",
    schema=LabelSelectorSchema,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    schema=LimitSchema,
)
request_query_orphan_dependents = api_client.QueryParameter(
    name="orphanDependents",
    schema=OrphanDependentsSchema,
)
request_query_propagation_policy = api_client.QueryParameter(
    name="propagationPolicy",
    schema=PropagationPolicySchema,
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
# Path params
NamespaceSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'namespace': typing.Union[NamespaceSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_namespace = api_client.PathParameter(
    name="namespace",
    schema=NamespaceSchema,
    required=True,
)
# body param
SchemaForRequestBody = V1DeleteOptions


request_body_body = api_client.RequestBody(
    content={
        '*/*': api_client.MediaType(
            schema=SchemaForRequestBody),
    },
)
SchemaFor200ResponseBodyApplicationJson = V1Status
SchemaFor200ResponseBodyApplicationYaml = V1Status
SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf = V1Status


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyApplicationYaml,
        SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf,
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
_all_accept_content_types = (
    'application/json',
    'application/yaml',
    'application/vnd.kubernetes.protobuf',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _delete_collection_namespaced_role_oapg(
        self,
        content_type: typing_extensions.Literal["*/*"] = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _delete_collection_namespaced_role_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def _delete_collection_namespaced_role_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _delete_collection_namespaced_role_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _delete_collection_namespaced_role_oapg(
        self,
        content_type: str = '*/*',
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
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
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_namespace,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_pretty,
            request_query__continue,
            request_query_dry_run,
            request_query_field_selector,
            request_query_grace_period_seconds,
            request_query_label_selector,
            request_query_limit,
            request_query_orphan_dependents,
            request_query_propagation_policy,
            request_query_resource_version,
            request_query_resource_version_match,
            request_query_timeout_seconds,
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

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='delete'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
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


class DeleteCollectionNamespacedRole(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def delete_collection_namespaced_role(
        self,
        content_type: typing_extensions.Literal["*/*"] = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def delete_collection_namespaced_role(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def delete_collection_namespaced_role(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def delete_collection_namespaced_role(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def delete_collection_namespaced_role(
        self,
        content_type: str = '*/*',
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._delete_collection_namespaced_role_oapg(
            body=body,
            query_params=query_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def delete(
        self,
        content_type: typing_extensions.Literal["*/*"] = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def delete(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def delete(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def delete(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def delete(
        self,
        content_type: str = '*/*',
        body: typing.Union[SchemaForRequestBody, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._delete_collection_namespaced_role_oapg(
            body=body,
            query_params=query_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


