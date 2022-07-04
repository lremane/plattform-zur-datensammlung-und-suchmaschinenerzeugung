# qa_client.DatasetControllerFreeTextApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**free_text_collection_creation_using_post**](DatasetControllerFreeTextApi.md#free_text_collection_creation_using_post) | **POST** /api/freeText/collection | freeTextCollectionCreation
[**free_text_collection_deletion_using_delete**](DatasetControllerFreeTextApi.md#free_text_collection_deletion_using_delete) | **DELETE** /api/freeText/collection | freeTextCollectionDeletion
[**free_text_collection_list_using_get**](DatasetControllerFreeTextApi.md#free_text_collection_list_using_get) | **GET** /api/freeText/collection/list | freeTextCollectionList
[**free_text_collection_read_using_get**](DatasetControllerFreeTextApi.md#free_text_collection_read_using_get) | **GET** /api/freeText/collection | freeTextCollectionRead
[**free_text_collection_update_using_put**](DatasetControllerFreeTextApi.md#free_text_collection_update_using_put) | **PUT** /api/freeText/collection | freeTextCollectionUpdate
[**free_text_document_deletion_using_delete**](DatasetControllerFreeTextApi.md#free_text_document_deletion_using_delete) | **DELETE** /api/freeText/collection/documents | freeTextDocumentDeletion
[**free_text_documents_list_using_get**](DatasetControllerFreeTextApi.md#free_text_documents_list_using_get) | **GET** /api/freeText/collection/documents | freeTextDocumentsList


# **free_text_collection_creation_using_post**
> GeneralResponse free_text_collection_creation_using_post(collection_model)

freeTextCollectionCreation

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_free_text_api
from qa_client.model.collection_model import CollectionModel
from qa_client.model.general_response import GeneralResponse
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
    api_instance = dataset_controller_free_text_api.DatasetControllerFreeTextApi(api_client)
    collection_model = CollectionModel(
        bm25_b=3.14,
        bm25_k1=3.14,
        clean_empty_lines=True,
        clean_header_footer=True,
        clean_whitespace=True,
        create_time="create_time_example",
        doc_stride=1,
        id="id_example",
        index_name="index_name_example",
        index_type="index_type_example",
        is_updating=True,
        language="language_example",
        max_seq_len=1,
        no_ans_boost=1,
        reader_option="reader_option_example",
        split_by="split_by_example",
        split_length=1,
        split_strategy="split_strategy_example",
        top_k_ranker=1,
        top_k_reader=1,
        top_k_retriever=1,
        use_fallback=True,
        use_ranker=True,
        use_reader=True,
        username="username_example",
        weight_text=3.14,
        weight_title=3.14,
    ) # CollectionModel | collectionModel

    # example passing only required values which don't have defaults set
    try:
        # freeTextCollectionCreation
        api_response = api_instance.free_text_collection_creation_using_post(collection_model)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerFreeTextApi->free_text_collection_creation_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_model** | [**CollectionModel**](CollectionModel.md)| collectionModel |

### Return type

[**GeneralResponse**](GeneralResponse.md)

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

# **free_text_collection_deletion_using_delete**
> GeneralResponse free_text_collection_deletion_using_delete(collection_id)

freeTextCollectionDeletion

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_free_text_api
from qa_client.model.general_response import GeneralResponse
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
    api_instance = dataset_controller_free_text_api.DatasetControllerFreeTextApi(api_client)
    collection_id = "collectionId_example" # str | collectionId

    # example passing only required values which don't have defaults set
    try:
        # freeTextCollectionDeletion
        api_response = api_instance.free_text_collection_deletion_using_delete(collection_id)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerFreeTextApi->free_text_collection_deletion_using_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| collectionId |

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **free_text_collection_list_using_get**
> [CollectionModel] free_text_collection_list_using_get()

freeTextCollectionList

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_free_text_api
from qa_client.model.collection_model import CollectionModel
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
    api_instance = dataset_controller_free_text_api.DatasetControllerFreeTextApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # freeTextCollectionList
        api_response = api_instance.free_text_collection_list_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerFreeTextApi->free_text_collection_list_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[CollectionModel]**](CollectionModel.md)

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

# **free_text_collection_read_using_get**
> CollectionModel free_text_collection_read_using_get(collection_id)

freeTextCollectionRead

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_free_text_api
from qa_client.model.collection_model import CollectionModel
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
    api_instance = dataset_controller_free_text_api.DatasetControllerFreeTextApi(api_client)
    collection_id = "collectionId_example" # str | collectionId

    # example passing only required values which don't have defaults set
    try:
        # freeTextCollectionRead
        api_response = api_instance.free_text_collection_read_using_get(collection_id)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerFreeTextApi->free_text_collection_read_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| collectionId |

### Return type

[**CollectionModel**](CollectionModel.md)

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

# **free_text_collection_update_using_put**
> GeneralResponse free_text_collection_update_using_put(collection_put_model)

freeTextCollectionUpdate

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_free_text_api
from qa_client.model.collection_put_model import CollectionPutModel
from qa_client.model.general_response import GeneralResponse
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
    api_instance = dataset_controller_free_text_api.DatasetControllerFreeTextApi(api_client)
    collection_put_model = CollectionPutModel(
        clean_empty_lines=True,
        clean_header_footer=True,
        clean_whitespace=True,
        doc_stride=1,
        id="id_example",
        max_seq_len=1,
        no_ans_boost=1,
        split_by="split_by_example",
        split_length=1,
        split_strategy="split_strategy_example",
        top_k_reader=1,
        top_k_retriever=1,
        use_fallback=True,
        use_reader=True,
    ) # CollectionPutModel | collectionPutModel

    # example passing only required values which don't have defaults set
    try:
        # freeTextCollectionUpdate
        api_response = api_instance.free_text_collection_update_using_put(collection_put_model)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerFreeTextApi->free_text_collection_update_using_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_put_model** | [**CollectionPutModel**](CollectionPutModel.md)| collectionPutModel |

### Return type

[**GeneralResponse**](GeneralResponse.md)

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

# **free_text_document_deletion_using_delete**
> GeneralResponse free_text_document_deletion_using_delete(index_name)

freeTextDocumentDeletion

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_free_text_api
from qa_client.model.general_response import GeneralResponse
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
    api_instance = dataset_controller_free_text_api.DatasetControllerFreeTextApi(api_client)
    index_name = "index_name_example" # str | indexName

    # example passing only required values which don't have defaults set
    try:
        # freeTextDocumentDeletion
        api_response = api_instance.free_text_document_deletion_using_delete(index_name)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerFreeTextApi->free_text_document_deletion_using_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| indexName |

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **free_text_documents_list_using_get**
> ReadDocumentsResponse free_text_documents_list_using_get()

freeTextDocumentsList

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_free_text_api
from qa_client.model.read_documents_response import ReadDocumentsResponse
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
    api_instance = dataset_controller_free_text_api.DatasetControllerFreeTextApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # freeTextDocumentsList
        api_response = api_instance.free_text_documents_list_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerFreeTextApi->free_text_documents_list_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ReadDocumentsResponse**](ReadDocumentsResponse.md)

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

