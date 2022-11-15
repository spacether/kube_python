# kubernetes.client.model.v2_metric_spec.V2MetricSpec

MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | MetricSpec specifies how to scale based on a single metric (only &#x60;type&#x60; and one other matching field should be set at once). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | type is the type of metric source.  It should be one of \&quot;ContainerResource\&quot;, \&quot;External\&quot;, \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each mapping to a matching field in the object. Note: \&quot;ContainerResource\&quot; type is available on when the feature-gate HPAContainerMetrics is enabled | 
**containerResource** | [**V2ContainerResourceMetricSource**](V2ContainerResourceMetricSource.md) | [**V2ContainerResourceMetricSource**](V2ContainerResourceMetricSource.md) |  | [optional] 
**external** | [**V2ExternalMetricSource**](V2ExternalMetricSource.md) | [**V2ExternalMetricSource**](V2ExternalMetricSource.md) |  | [optional] 
**object** | [**V2ObjectMetricSource**](V2ObjectMetricSource.md) | [**V2ObjectMetricSource**](V2ObjectMetricSource.md) |  | [optional] 
**pods** | [**V2PodsMetricSource**](V2PodsMetricSource.md) | [**V2PodsMetricSource**](V2PodsMetricSource.md) |  | [optional] 
**resource** | [**V2ResourceMetricSource**](V2ResourceMetricSource.md) | [**V2ResourceMetricSource**](V2ResourceMetricSource.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
