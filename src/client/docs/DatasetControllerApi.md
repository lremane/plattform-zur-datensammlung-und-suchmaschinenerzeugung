# qa_client.DatasetControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_all_datasets_using_get**](DatasetControllerApi.md#get_list_all_datasets_using_get) | **GET** /api/dataset_new/list_all | Lists all datasets uploaded by the user
[**get_logo_using_get**](DatasetControllerApi.md#get_logo_using_get) | **GET** /api/dataset_new/dataset/logo | Retrieves the logo of a specific dataset
[**remove_using_post**](DatasetControllerApi.md#remove_using_post) | **POST** /api/dataset_new/remove | To remove a specific dataset


# **get_list_all_datasets_using_get**
> [DatasetDetail] get_list_all_datasets_using_get()

Lists all datasets uploaded by the user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_api
from qa_client.model.dataset_detail import DatasetDetail
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
    api_instance = dataset_controller_api.DatasetControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Lists all datasets uploaded by the user
        api_response = api_instance.get_list_all_datasets_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerApi->get_list_all_datasets_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[DatasetDetail]**](DatasetDetail.md)

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

# **get_logo_using_get**
> str get_logo_using_get(dataset)

Retrieves the logo of a specific dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_api
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
    api_instance = dataset_controller_api.DatasetControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # Retrieves the logo of a specific dataset
        api_response = api_instance.get_logo_using_get(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerApi->get_logo_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_using_post**
> ApiResponse remove_using_post(dataset)

To remove a specific dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_api
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
    api_instance = dataset_controller_api.DatasetControllerApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # To remove a specific dataset
        api_response = api_instance.remove_using_post(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerApi->remove_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

