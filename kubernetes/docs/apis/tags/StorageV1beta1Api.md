<a name="__pageTop"></a>
# kubernetes.client.apis.tags.storage_v1beta1_api.StorageV1beta1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_csi_storage_capacity**](#create_namespaced_csi_storage_capacity) | **post** /apis/storage.k8s.io/v1beta1/namespaces/{namespace}/csistoragecapacities | 
[**delete_collection_namespaced_csi_storage_capacity**](#delete_collection_namespaced_csi_storage_capacity) | **delete** /apis/storage.k8s.io/v1beta1/namespaces/{namespace}/csistoragecapacities | 
[**delete_namespaced_csi_storage_capacity**](#delete_namespaced_csi_storage_capacity) | **delete** /apis/storage.k8s.io/v1beta1/namespaces/{namespace}/csistoragecapacities/{name} | 
[**get_api_resources**](#get_api_resources) | **get** /apis/storage.k8s.io/v1beta1/ | 
[**list_csi_storage_capacity_for_all_namespaces**](#list_csi_storage_capacity_for_all_namespaces) | **get** /apis/storage.k8s.io/v1beta1/csistoragecapacities | 
[**list_namespaced_csi_storage_capacity**](#list_namespaced_csi_storage_capacity) | **get** /apis/storage.k8s.io/v1beta1/namespaces/{namespace}/csistoragecapacities | 
[**patch_namespaced_csi_storage_capacity**](#patch_namespaced_csi_storage_capacity) | **patch** /apis/storage.k8s.io/v1beta1/namespaces/{namespace}/csistoragecapacities/{name} | 
[**read_namespaced_csi_storage_capacity**](#read_namespaced_csi_storage_capacity) | **get** /apis/storage.k8s.io/v1beta1/namespaces/{namespace}/csistoragecapacities/{name} | 
[**replace_namespaced_csi_storage_capacity**](#replace_namespaced_csi_storage_capacity) | **put** /apis/storage.k8s.io/v1beta1/namespaces/{namespace}/csistoragecapacities/{name} | 

# **create_namespaced_csi_storage_capacity**
<a name="create_namespaced_csi_storage_capacity"></a>
> V1beta1CSIStorageCapacity create_namespaced_csi_storage_capacity(namespacebody)



create a CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1beta1_api
from kubernetes.client.model.v1beta1_csi_storage_capacity import V1beta1CSIStorageCapacity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_v1beta1_api.StorageV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1beta1CSIStorageCapacity(
        api_version="api_version_example",
        capacity="capacity_example",
        kind="kind_example",
        maximum_volume_size="maximum_volume_size_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        node_topology=V1LabelSelector(
            match_expressions=[
                V1LabelSelectorRequirement(
                    key="key_example",
                    operator="operator_example",
                    values=[
                        "values_example"
                    ],
                )
            ],
            match_labels=dict(
                "key": "key_example",
            ),
        ),
        storage_class_name="storage_class_name_example",
    )
    try:
        api_response = api_instance.create_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->create_namespaced_csi_storage_capacity: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1beta1CSIStorageCapacity(
        api_version="api_version_example",
        capacity="capacity_example",
        kind="kind_example",
        maximum_volume_size="maximum_volume_size_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        node_topology=V1LabelSelector(
            match_expressions=[
                V1LabelSelectorRequirement(
                    key="key_example",
                    operator="operator_example",
                    values=[
                        "values_example"
                    ],
                )
            ],
            match_labels=dict(
                "key": "key_example",
            ),
        ),
        storage_class_name="storage_class_name_example",
    )
    try:
        api_response = api_instance.create_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->create_namespaced_csi_storage_capacity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_namespaced_csi_storage_capacity.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_namespaced_csi_storage_capacity.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### create_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


#### create_namespaced_csi_storage_capacity.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


#### create_namespaced_csi_storage_capacity.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


#### create_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_namespaced_csi_storage_capacity**
<a name="delete_collection_namespaced_csi_storage_capacity"></a>
> V1Status delete_collection_namespaced_csi_storage_capacity(namespace)



delete collection of CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1beta1_api
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
from kubernetes.client.model.v1_status import V1Status
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_v1beta1_api.StorageV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_collection_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->delete_collection_namespaced_csi_storage_capacity: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'continue': "continue_example",
        'dryRun': "dryRun_example",
        'fieldSelector': "fieldSelector_example",
        'gracePeriodSeconds': 1,
        'labelSelector': "labelSelector_example",
        'limit': 1,
        'orphanDependents': True,
        'propagationPolicy': "propagationPolicy_example",
        'resourceVersion': "resourceVersion_example",
        'resourceVersionMatch': "resourceVersionMatch_example",
        'timeoutSeconds': 1,
    }
    body = V1DeleteOptions(
        api_version="api_version_example",
        dry_run=[
            "dry_run_example"
        ],
        grace_period_seconds=1,
        kind="kind_example",
        orphan_dependents=True,
        preconditions=V1Preconditions(
            resource_version="resource_version_example",
            uid="uid_example",
        ),
        propagation_policy="propagation_policy_example",
    )
    try:
        api_response = api_instance.delete_collection_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->delete_collection_namespaced_csi_storage_capacity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1DeleteOptions**](../../models/V1DeleteOptions.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
continue | ModelContinueSchema | | optional
dryRun | DryRunSchema | | optional
fieldSelector | FieldSelectorSchema | | optional
gracePeriodSeconds | GracePeriodSecondsSchema | | optional
labelSelector | LabelSelectorSchema | | optional
limit | LimitSchema | | optional
orphanDependents | OrphanDependentsSchema | | optional
propagationPolicy | PropagationPolicySchema | | optional
resourceVersion | ResourceVersionSchema | | optional
resourceVersionMatch | ResourceVersionMatchSchema | | optional
timeoutSeconds | TimeoutSecondsSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModelContinueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GracePeriodSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LabelSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OrphanDependentsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PropagationPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeoutSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_collection_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### delete_collection_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


#### delete_collection_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_namespaced_csi_storage_capacity**
<a name="delete_namespaced_csi_storage_capacity"></a>
> V1Status delete_namespaced_csi_storage_capacity(namenamespace)



delete a CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1beta1_api
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
from kubernetes.client.model.v1_status import V1Status
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_v1beta1_api.StorageV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->delete_namespaced_csi_storage_capacity: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'gracePeriodSeconds': 1,
        'orphanDependents': True,
        'propagationPolicy': "propagationPolicy_example",
    }
    body = V1DeleteOptions(
        api_version="api_version_example",
        dry_run=[
            "dry_run_example"
        ],
        grace_period_seconds=1,
        kind="kind_example",
        orphan_dependents=True,
        preconditions=V1Preconditions(
            resource_version="resource_version_example",
            uid="uid_example",
        ),
        propagation_policy="propagation_policy_example",
    )
    try:
        api_response = api_instance.delete_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->delete_namespaced_csi_storage_capacity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1DeleteOptions**](../../models/V1DeleteOptions.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
gracePeriodSeconds | GracePeriodSecondsSchema | | optional
orphanDependents | OrphanDependentsSchema | | optional
propagationPolicy | PropagationPolicySchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GracePeriodSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OrphanDependentsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PropagationPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_namespaced_csi_storage_capacity.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### delete_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


#### delete_namespaced_csi_storage_capacity.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


#### delete_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_resources**
<a name="get_api_resources"></a>
> V1APIResourceList get_api_resources()



get available resources

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1beta1_api
from kubernetes.client.model.v1_api_resource_list import V1APIResourceList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_v1beta1_api.StorageV1beta1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_api_resources()
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->get_api_resources: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_resources.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_api_resources.ApiResponseFor401) | Unauthorized

#### get_api_resources.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1APIResourceList**](../../models/V1APIResourceList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1APIResourceList**](../../models/V1APIResourceList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1APIResourceList**](../../models/V1APIResourceList.md) |  | 


#### get_api_resources.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_csi_storage_capacity_for_all_namespaces**
<a name="list_csi_storage_capacity_for_all_namespaces"></a>
> V1beta1CSIStorageCapacityList list_csi_storage_capacity_for_all_namespaces()



list or watch objects of kind CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1beta1_api
from kubernetes.client.model.v1beta1_csi_storage_capacity_list import V1beta1CSIStorageCapacityList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_v1beta1_api.StorageV1beta1Api(api_client)

    # example passing only optional values
    query_params = {
        'allowWatchBookmarks': True,
        'continue': "continue_example",
        'fieldSelector': "fieldSelector_example",
        'labelSelector': "labelSelector_example",
        'limit': 1,
        'pretty': "pretty_example",
        'resourceVersion': "resourceVersion_example",
        'resourceVersionMatch': "resourceVersionMatch_example",
        'timeoutSeconds': 1,
        'watch': True,
    }
    try:
        api_response = api_instance.list_csi_storage_capacity_for_all_namespaces(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->list_csi_storage_capacity_for_all_namespaces: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', 'application/json;stream&#x3D;watch', 'application/vnd.kubernetes.protobuf;stream&#x3D;watch', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
allowWatchBookmarks | AllowWatchBookmarksSchema | | optional
continue | ModelContinueSchema | | optional
fieldSelector | FieldSelectorSchema | | optional
labelSelector | LabelSelectorSchema | | optional
limit | LimitSchema | | optional
pretty | PrettySchema | | optional
resourceVersion | ResourceVersionSchema | | optional
resourceVersionMatch | ResourceVersionMatchSchema | | optional
timeoutSeconds | TimeoutSecondsSchema | | optional
watch | WatchSchema | | optional


# AllowWatchBookmarksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ModelContinueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LabelSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeoutSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_csi_storage_capacity_for_all_namespaces.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_csi_storage_capacity_for_all_namespaces.ApiResponseFor401) | Unauthorized

#### list_csi_storage_capacity_for_all_namespaces.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


#### list_csi_storage_capacity_for_all_namespaces.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_namespaced_csi_storage_capacity**
<a name="list_namespaced_csi_storage_capacity"></a>
> V1beta1CSIStorageCapacityList list_namespaced_csi_storage_capacity(namespace)



list or watch objects of kind CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1beta1_api
from kubernetes.client.model.v1beta1_csi_storage_capacity_list import V1beta1CSIStorageCapacityList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_v1beta1_api.StorageV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->list_namespaced_csi_storage_capacity: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'allowWatchBookmarks': True,
        'continue': "continue_example",
        'fieldSelector': "fieldSelector_example",
        'labelSelector': "labelSelector_example",
        'limit': 1,
        'resourceVersion': "resourceVersion_example",
        'resourceVersionMatch': "resourceVersionMatch_example",
        'timeoutSeconds': 1,
        'watch': True,
    }
    try:
        api_response = api_instance.list_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->list_namespaced_csi_storage_capacity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', 'application/json;stream&#x3D;watch', 'application/vnd.kubernetes.protobuf;stream&#x3D;watch', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
allowWatchBookmarks | AllowWatchBookmarksSchema | | optional
continue | ModelContinueSchema | | optional
fieldSelector | FieldSelectorSchema | | optional
labelSelector | LabelSelectorSchema | | optional
limit | LimitSchema | | optional
resourceVersion | ResourceVersionSchema | | optional
resourceVersionMatch | ResourceVersionMatchSchema | | optional
timeoutSeconds | TimeoutSecondsSchema | | optional
watch | WatchSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AllowWatchBookmarksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ModelContinueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LabelSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ResourceVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeoutSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### list_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacityList**](../../models/V1beta1CSIStorageCapacityList.md) |  | 


#### list_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_namespaced_csi_storage_capacity**
<a name="patch_namespaced_csi_storage_capacity"></a>
> V1beta1CSIStorageCapacity patch_namespaced_csi_storage_capacity(namenamespacebody)



partially update the specified CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1beta1_api
from kubernetes.client.model.v1beta1_csi_storage_capacity import V1beta1CSIStorageCapacity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_v1beta1_api.StorageV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->patch_namespaced_csi_storage_capacity: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
        'force': True,
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->patch_namespaced_csi_storage_capacity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationMergePatchjson, SchemaForRequestBodyApplicationStrategicMergePatchjson, SchemaForRequestBodyApplicationApplyPatchyaml] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationStrategicMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationApplyPatchyaml

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional
force | ForceSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ForceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_namespaced_csi_storage_capacity.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### patch_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


#### patch_namespaced_csi_storage_capacity.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


#### patch_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_namespaced_csi_storage_capacity**
<a name="read_namespaced_csi_storage_capacity"></a>
> V1beta1CSIStorageCapacity read_namespaced_csi_storage_capacity(namenamespace)



read the specified CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1beta1_api
from kubernetes.client.model.v1beta1_csi_storage_capacity import V1beta1CSIStorageCapacity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_v1beta1_api.StorageV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->read_namespaced_csi_storage_capacity: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->read_namespaced_csi_storage_capacity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### read_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


#### read_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_namespaced_csi_storage_capacity**
<a name="replace_namespaced_csi_storage_capacity"></a>
> V1beta1CSIStorageCapacity replace_namespaced_csi_storage_capacity(namenamespacebody)



replace the specified CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1beta1_api
from kubernetes.client.model.v1beta1_csi_storage_capacity import V1beta1CSIStorageCapacity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_v1beta1_api.StorageV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1beta1CSIStorageCapacity(
        api_version="api_version_example",
        capacity="capacity_example",
        kind="kind_example",
        maximum_volume_size="maximum_volume_size_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        node_topology=V1LabelSelector(
            match_expressions=[
                V1LabelSelectorRequirement(
                    key="key_example",
                    operator="operator_example",
                    values=[
                        "values_example"
                    ],
                )
            ],
            match_labels=dict(
                "key": "key_example",
            ),
        ),
        storage_class_name="storage_class_name_example",
    )
    try:
        api_response = api_instance.replace_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->replace_namespaced_csi_storage_capacity: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1beta1CSIStorageCapacity(
        api_version="api_version_example",
        capacity="capacity_example",
        kind="kind_example",
        maximum_volume_size="maximum_volume_size_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        node_topology=V1LabelSelector(
            match_expressions=[
                V1LabelSelectorRequirement(
                    key="key_example",
                    operator="operator_example",
                    values=[
                        "values_example"
                    ],
                )
            ],
            match_labels=dict(
                "key": "key_example",
            ),
        ),
        storage_class_name="storage_class_name_example",
    )
    try:
        api_response = api_instance.replace_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1beta1Api->replace_namespaced_csi_storage_capacity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_namespaced_csi_storage_capacity.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### replace_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


#### replace_namespaced_csi_storage_capacity.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1CSIStorageCapacity**](../../models/V1beta1CSIStorageCapacity.md) |  | 


#### replace_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
