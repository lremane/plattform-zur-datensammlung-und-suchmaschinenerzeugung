# qa_client.FreeTextJobControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**free_text_job_list_using_get**](FreeTextJobControllerApi.md#free_text_job_list_using_get) | **GET** /api/freeText/job/list | freeTextJobList
[**free_text_job_terminated_using_get**](FreeTextJobControllerApi.md#free_text_job_terminated_using_get) | **GET** /api/freeText/job_terminated | freeTextJobTerminated
[**free_text_job_update_using_put**](FreeTextJobControllerApi.md#free_text_job_update_using_put) | **PUT** /api/freeText/job | freeTextJobUpdate


# **free_text_job_list_using_get**
> [JobModel] free_text_job_list_using_get()

freeTextJobList

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_job_controller_api
from qa_client.model.job_model import JobModel
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
    api_instance = free_text_job_controller_api.FreeTextJobControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # freeTextJobList
        api_response = api_instance.free_text_job_list_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextJobControllerApi->free_text_job_list_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[JobModel]**](JobModel.md)

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

# **free_text_job_terminated_using_get**
> free_text_job_terminated_using_get(job_id, job_status, job_type, username)

freeTextJobTerminated

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_job_controller_api
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
    api_instance = free_text_job_controller_api.FreeTextJobControllerApi(api_client)
    job_id = "jobId_example" # str | jobId
    job_status = "jobStatus_example" # str | jobStatus
    job_type = "jobType_example" # str | jobType
    username = "username_example" # str | username

    # example passing only required values which don't have defaults set
    try:
        # freeTextJobTerminated
        api_instance.free_text_job_terminated_using_get(job_id, job_status, job_type, username)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextJobControllerApi->free_text_job_terminated_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| jobId |
 **job_status** | **str**| jobStatus |
 **job_type** | **str**| jobType |
 **username** | **str**| username |

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

# **free_text_job_update_using_put**
> GeneralResponse free_text_job_update_using_put(job_id, job_status)

freeTextJobUpdate

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_job_controller_api
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
    api_instance = free_text_job_controller_api.FreeTextJobControllerApi(api_client)
    job_id = "jobId_example" # str | jobId
    job_status = "jobStatus_example" # str | jobStatus

    # example passing only required values which don't have defaults set
    try:
        # freeTextJobUpdate
        api_response = api_instance.free_text_job_update_using_put(job_id, job_status)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextJobControllerApi->free_text_job_update_using_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| jobId |
 **job_status** | **str**| jobStatus |

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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

