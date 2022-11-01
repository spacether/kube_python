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

from kubernetes.client.model.authentication_v1_token_request import AuthenticationV1TokenRequest

from . import path

# Query params
DryRunSchema = schemas.StrSchema
FieldManagerSchema = schemas.StrSchema
FieldValidationSchema = schemas.StrSchema
PrettySchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'dryRun': typing.Union[DryRunSchema, str, ],
        'fieldManager': typing.Union[FieldManagerSchema, str, ],
        'fieldValidation': typing.Union[FieldValidationSchema, str, ],
        'pretty': typing.Union[PrettySchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_dry_run = api_client.QueryParameter(
    name="dryRun",
    schema=DryRunSchema,
)
request_query_field_manager = api_client.QueryParameter(
    name="fieldManager",
    schema=FieldManagerSchema,
)
request_query_field_validation = api_client.QueryParameter(
    name="fieldValidation",
    schema=FieldValidationSchema,
)
request_query_pretty = api_client.QueryParameter(
    name="pretty",
    schema=PrettySchema,
)
# Path params
NameSchema = schemas.StrSchema
NamespaceSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'name': typing.Union[NameSchema, str, ],
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


request_path_name = api_client.PathParameter(
    name="name",
    schema=NameSchema,
    required=True,
)
request_path_namespace = api_client.PathParameter(
    name="namespace",
    schema=NamespaceSchema,
    required=True,
)
# body param
SchemaForRequestBody = AuthenticationV1TokenRequest


request_body_body = api_client.RequestBody(
    content={
        '*/*': api_client.MediaType(
            schema=SchemaForRequestBody),
    },
    required=True,
)
_auth = [
    'BearerToken',
]
SchemaFor200ResponseBodyApplicationJson = AuthenticationV1TokenRequest
SchemaFor200ResponseBodyApplicationYaml = AuthenticationV1TokenRequest
SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf = AuthenticationV1TokenRequest


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
SchemaFor201ResponseBodyApplicationJson = AuthenticationV1TokenRequest
SchemaFor201ResponseBodyApplicationYaml = AuthenticationV1TokenRequest
SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf = AuthenticationV1TokenRequest


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor201ResponseBodyApplicationJson,
        SchemaFor201ResponseBodyApplicationYaml,
        SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
        'application/yaml': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationYaml),
        'application/vnd.kubernetes.protobuf': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf),
    },
)
SchemaFor202ResponseBodyApplicationJson = AuthenticationV1TokenRequest
SchemaFor202ResponseBodyApplicationYaml = AuthenticationV1TokenRequest
SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf = AuthenticationV1TokenRequest


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor202ResponseBodyApplicationJson,
        SchemaFor202ResponseBodyApplicationYaml,
        SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
        'application/yaml': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationYaml),
        'application/vnd.kubernetes.protobuf': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf),
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
    '201': _response_for_201,
    '202': _response_for_202,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
    'application/yaml',
    'application/vnd.kubernetes.protobuf',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _create_namespaced_service_account_token_oapg(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: typing_extensions.Literal["*/*"] = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
    ]: ...

    @typing.overload
    def _create_namespaced_service_account_token_oapg(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
    ]: ...


    @typing.overload
    def _create_namespaced_service_account_token_oapg(
        self,
        body: typing.Union[SchemaForRequestBody,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _create_namespaced_service_account_token_oapg(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _create_namespaced_service_account_token_oapg(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: str = '*/*',
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
            request_path_name,
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
            request_query_dry_run,
            request_query_field_manager,
            request_query_field_validation,
            request_query_pretty,
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

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_body.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
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


class CreateNamespacedServiceAccountToken(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def create_namespaced_service_account_token(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: typing_extensions.Literal["*/*"] = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
    ]: ...

    @typing.overload
    def create_namespaced_service_account_token(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
    ]: ...


    @typing.overload
    def create_namespaced_service_account_token(
        self,
        body: typing.Union[SchemaForRequestBody,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def create_namespaced_service_account_token(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def create_namespaced_service_account_token(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: str = '*/*',
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._create_namespaced_service_account_token_oapg(
            body=body,
            query_params=query_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: typing_extensions.Literal["*/*"] = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
    ]: ...


    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBody,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        body: typing.Union[SchemaForRequestBody,],
        content_type: str = '*/*',
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._create_namespaced_service_account_token_oapg(
            body=body,
            query_params=query_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


