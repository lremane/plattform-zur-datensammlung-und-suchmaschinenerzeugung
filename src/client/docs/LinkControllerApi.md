# qa_client.LinkControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate_using_get1**](LinkControllerApi.md#evaluate_using_get1) | **GET** /api/linkDev/evaluate | evaluate
[**link2_using_post**](LinkControllerApi.md#link2_using_post) | **POST** /api/linkDev/link2 | link2
[**link3_train_using_post**](LinkControllerApi.md#link3_train_using_post) | **POST** /api/linkDev/link3/train | link3Train
[**link3_upload_using_post**](LinkControllerApi.md#link3_upload_using_post) | **POST** /api/linkDev/link3/upload | link3Upload
[**link3_using_post**](LinkControllerApi.md#link3_using_post) | **POST** /api/linkDev/link3 | link3
[**link3generate_features_using_post**](LinkControllerApi.md#link3generate_features_using_post) | **POST** /api/linkDev/link3/generate_features | link3generateFeatures
[**link_aggregate_using_get**](LinkControllerApi.md#link_aggregate_using_get) | **GET** /api/linkDev/link/aggregate | linkAggregate
[**link_aggregate_using_post**](LinkControllerApi.md#link_aggregate_using_post) | **POST** /api/linkDev/link/aggregate | linkAggregate
[**link_analyze_using_post**](LinkControllerApi.md#link_analyze_using_post) | **POST** /api/linkDev/link/analyze | linkAnalyze
[**link_delete_using_post**](LinkControllerApi.md#link_delete_using_post) | **POST** /api/linkDev/link/delete | Deletes a dataset for linking. The request contains the dataset name
[**link_evaluate_using_get**](LinkControllerApi.md#link_evaluate_using_get) | **GET** /api/linkDev/link/evaluate | linkEvaluate
[**link_evaluate_using_post**](LinkControllerApi.md#link_evaluate_using_post) | **POST** /api/linkDev/link/evaluate | linkEvaluate
[**link_kohesio_using_get**](LinkControllerApi.md#link_kohesio_using_get) | **GET** /api/linkDev/link_kohesio | linkKohesio
[**link_list_using_get**](LinkControllerApi.md#link_list_using_get) | **GET** /api/linkDev/link/list | Loads a new dataset to link. The request contains the dataset name, the Knowledgegraph to link to, the languages and the text,uri pairs
[**link_load_using_post**](LinkControllerApi.md#link_load_using_post) | **POST** /api/linkDev/link/upload | Loads a new dataset to link. The request contains the dataset name, the Knowledgegraph to link to, the languages and the text,uri pairs
[**link_result_using_get**](LinkControllerApi.md#link_result_using_get) | **GET** /api/linkDev/link/result | linkResult
[**link_train_using_post**](LinkControllerApi.md#link_train_using_post) | **POST** /api/linkDev/link/train | linkTrain
[**link_using_get**](LinkControllerApi.md#link_using_get) | **GET** /api/linkDev/link | link
[**link_using_post**](LinkControllerApi.md#link_using_post) | **POST** /api/linkDev/link | link


# **evaluate_using_get1**
> evaluate_using_get1()

evaluate

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # evaluate
        api_instance.evaluate_using_get1()
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->evaluate_using_get1: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link2_using_post**
> bool, date, datetime, dict, float, int, list, str, none_type link2_using_post(link)

link2

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.link_range import LinkRange
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    link = LinkRange(
        knowledgebase="knowledgebase_example",
        language="language_example",
        limit=1,
        range=[
            "range_example",
        ],
        texts=[
            "texts_example",
        ],
        user="user_example",
    ) # LinkRange | link

    # example passing only required values which don't have defaults set
    try:
        # link2
        api_response = api_instance.link2_using_post(link)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link2_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | [**LinkRange**](LinkRange.md)| link |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link3_train_using_post**
> link3_train_using_post(dataset)

link3Train

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # link3Train
        api_instance.link3_train_using_post(dataset)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link3_train_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link3_upload_using_post**
> link3_upload_using_post(dataset_pairs)

link3Upload

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.dataset_pairs import DatasetPairs
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset_pairs = DatasetPairs(
        dataset="dataset_example",
        knowledgebase="knowledgebase_example",
        language=[
            "language_example",
        ],
        pairs=[
            Pair(
                text="text_example",
                uris=[
                    "uris_example",
                ],
            ),
        ],
        user="user_example",
    ) # DatasetPairs | datasetPairs

    # example passing only required values which don't have defaults set
    try:
        # link3Upload
        api_instance.link3_upload_using_post(dataset_pairs)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link3_upload_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_pairs** | [**DatasetPairs**](DatasetPairs.md)| datasetPairs |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link3_using_post**
> bool, date, datetime, dict, float, int, list, str, none_type link3_using_post(link)

link3

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.link_enchanced import LinkEnchanced
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    link = LinkEnchanced(
        dataset="dataset_example",
        limit=1,
        texts=[
            "texts_example",
        ],
    ) # LinkEnchanced | link

    # example passing only required values which don't have defaults set
    try:
        # link3
        api_response = api_instance.link3_using_post(link)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link3_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | [**LinkEnchanced**](LinkEnchanced.md)| link |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link3generate_features_using_post**
> link3generate_features_using_post(dataset)

link3generateFeatures

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # link3generateFeatures
        api_instance.link3generate_features_using_post(dataset)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link3generate_features_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_aggregate_using_get**
> [Aggregate] link_aggregate_using_get(dataset)

linkAggregate

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.aggregate import Aggregate
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # linkAggregate
        api_response = api_instance.link_aggregate_using_get(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_aggregate_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

[**[Aggregate]**](Aggregate.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_aggregate_using_post**
> ApiResponse link_aggregate_using_post(dataset, aggregate_list)

linkAggregate

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.aggregate import Aggregate
from qa_client.model.api_response import ApiResponse
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset
    aggregate_list = [
        Aggregate(
            answer_context=QaContext(
                audio=[
                    "audio_example",
                ],
                description="description_example",
                disambiguation="disambiguation_example",
                geo=[
                    Coordinates(
                        latitude=3.14,
                        longitude=3.14,
                    ),
                ],
                geo_json="geo_json_example",
                images=[
                    "images_example",
                ],
                kb="kb_example",
                label="label_example",
                links={
                    "key": "key_example",
                },
                literal="literal_example",
                optional={
                    "key": [
                        "key_example",
                    ],
                },
                page_rank=3.14,
                time="time_example",
                time_series="time_series_example",
                uri="uri_example",
                user="user_example",
                video=[
                    "video_example",
                ],
            ),
            excluded=True,
            occurance=1,
            uri="uri_example",
        ),
    ] # [Aggregate] | aggregateList

    # example passing only required values which don't have defaults set
    try:
        # linkAggregate
        api_response = api_instance.link_aggregate_using_post(dataset, aggregate_list)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_aggregate_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **aggregate_list** | [**[Aggregate]**](Aggregate.md)| aggregateList |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_analyze_using_post**
> LinkingResult link_analyze_using_post(dataset)

linkAnalyze

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.linking_result import LinkingResult
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # linkAnalyze
        api_response = api_instance.link_analyze_using_post(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_analyze_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

[**LinkingResult**](LinkingResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_delete_using_post**
> link_delete_using_post(dataset)

Deletes a dataset for linking. The request contains the dataset name

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # Deletes a dataset for linking. The request contains the dataset name
        api_instance.link_delete_using_post(dataset)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_delete_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_evaluate_using_get**
> LinkingResult link_evaluate_using_get(dataset)

linkEvaluate

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.linking_result import LinkingResult
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # linkEvaluate
        api_response = api_instance.link_evaluate_using_get(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_evaluate_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

[**LinkingResult**](LinkingResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_evaluate_using_post**
> ApiResponse link_evaluate_using_post(dataset, linking_result)

linkEvaluate

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.linking_result import LinkingResult
from qa_client.model.api_response import ApiResponse
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset
    linking_result = LinkingResult(
        aggregate_list=[
            Aggregate(
                answer_context=QaContext(
                    audio=[
                        "audio_example",
                    ],
                    description="description_example",
                    disambiguation="disambiguation_example",
                    geo=[
                        Coordinates(
                            latitude=3.14,
                            longitude=3.14,
                        ),
                    ],
                    geo_json="geo_json_example",
                    images=[
                        "images_example",
                    ],
                    kb="kb_example",
                    label="label_example",
                    links={
                        "key": "key_example",
                    },
                    literal="literal_example",
                    optional={
                        "key": [
                            "key_example",
                        ],
                    },
                    page_rank=3.14,
                    time="time_example",
                    time_series="time_series_example",
                    uri="uri_example",
                    user="user_example",
                    video=[
                        "video_example",
                    ],
                ),
                excluded=True,
                occurance=1,
                uri="uri_example",
            ),
        ],
        links_list=[
            Links(
                links=[
                    Link(
                        answer_context=QaContext(
                            audio=[
                                "audio_example",
                            ],
                            description="description_example",
                            disambiguation="disambiguation_example",
                            geo=[
                                Coordinates(
                                    latitude=3.14,
                                    longitude=3.14,
                                ),
                            ],
                            geo_json="geo_json_example",
                            images=[
                                "images_example",
                            ],
                            kb="kb_example",
                            label="label_example",
                            links={
                                "key": "key_example",
                            },
                            literal="literal_example",
                            optional={
                                "key": [
                                    "key_example",
                                ],
                            },
                            page_rank=3.14,
                            time="time_example",
                            time_series="time_series_example",
                            uri="uri_example",
                            user="user_example",
                            video=[
                                "video_example",
                            ],
                        ),
                        concept_cloud=[
                            "concept_cloud_example",
                        ],
                        confidence=3.14,
                        excluded=True,
                        excluded_concepts=[
                            "excluded_concepts_example",
                        ],
                        match=True,
                        uri="uri_example",
                    ),
                ],
                text="text_example",
            ),
        ],
    ) # LinkingResult | linkingResult

    # example passing only required values which don't have defaults set
    try:
        # linkEvaluate
        api_response = api_instance.link_evaluate_using_post(dataset, linking_result)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_evaluate_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **linking_result** | [**LinkingResult**](LinkingResult.md)| linkingResult |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_kohesio_using_get**
> [Link] link_kohesio_using_get(dataset, text)

linkKohesio

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.link import Link
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset
    text = "text_example" # str | text

    # example passing only required values which don't have defaults set
    try:
        # linkKohesio
        api_response = api_instance.link_kohesio_using_get(dataset, text)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_kohesio_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **text** | **str**| text |

### Return type

[**[Link]**](Link.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_list_using_get**
> [str] link_list_using_get()

Loads a new dataset to link. The request contains the dataset name, the Knowledgegraph to link to, the languages and the text,uri pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Loads a new dataset to link. The request contains the dataset name, the Knowledgegraph to link to, the languages and the text,uri pairs
        api_response = api_instance.link_list_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_list_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_load_using_post**
> link_load_using_post(dataset_pairs)

Loads a new dataset to link. The request contains the dataset name, the Knowledgegraph to link to, the languages and the text,uri pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.dataset_pairs import DatasetPairs
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset_pairs = DatasetPairs(
        dataset="dataset_example",
        knowledgebase="knowledgebase_example",
        language=[
            "language_example",
        ],
        pairs=[
            Pair(
                text="text_example",
                uris=[
                    "uris_example",
                ],
            ),
        ],
        user="user_example",
    ) # DatasetPairs | datasetPairs

    # example passing only required values which don't have defaults set
    try:
        # Loads a new dataset to link. The request contains the dataset name, the Knowledgegraph to link to, the languages and the text,uri pairs
        api_instance.link_load_using_post(dataset_pairs)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_load_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_pairs** | [**DatasetPairs**](DatasetPairs.md)| datasetPairs |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_result_using_get**
> link_result_using_get(dataset)

linkResult

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # linkResult
        api_instance.link_result_using_get(dataset)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_result_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_train_using_post**
> link_train_using_post(dataset)

linkTrain

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # linkTrain
        api_instance.link_train_using_post(dataset)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_train_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_using_get**
> bool, date, datetime, dict, float, int, list, str, none_type link_using_get(knowledgebase, language, text, user)

link

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    knowledgebase = "knowledgebase_example" # str | knowledgebase
    language = "language_example" # str | language
    text = "text_example" # str | text
    user = "user_example" # str | user
    concept_must = [
        "conceptMust_example",
    ] # [str] | conceptMust (optional)
    query = "query_example" # str | query (optional)

    # example passing only required values which don't have defaults set
    try:
        # link
        api_response = api_instance.link_using_get(knowledgebase, language, text, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # link
        api_response = api_instance.link_using_get(knowledgebase, language, text, user, concept_must=concept_must, query=query)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **knowledgebase** | **str**| knowledgebase |
 **language** | **str**| language |
 **text** | **str**| text |
 **user** | **str**| user |
 **concept_must** | **[str]**| conceptMust | [optional]
 **query** | **str**| query | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_using_post**
> bool, date, datetime, dict, float, int, list, str, none_type link_using_post(link_payload)

link

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import link_controller_api
from qa_client.model.link_payload import LinkPayload
from pprint import pprint
# Defining the host is optional and defaults to http://qanswer-core1.univ-st-etienne.fr
# See configuration.py for a list of all supported configuration parameters.
configuration = qa_client.Configuration(
    host = "http://qanswer-core1.univ-st-etienne.fr"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with qa_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_controller_api.LinkControllerApi(api_client)
    link_payload = LinkPayload(
        knowledgebase="knowledgebase_example",
        language="language_example",
        limit=1,
        texts=[
            "texts_example",
        ],
        user="user_example",
    ) # LinkPayload | linkPayload

    # example passing only required values which don't have defaults set
    try:
        # link
        api_response = api_instance.link_using_post(link_payload)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling LinkControllerApi->link_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_payload** | [**LinkPayload**](LinkPayload.md)| linkPayload |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

