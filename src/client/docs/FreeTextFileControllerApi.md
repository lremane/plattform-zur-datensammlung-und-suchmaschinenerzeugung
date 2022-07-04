# qa_client.FreeTextFileControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**free_text_file_convert_using_post**](FreeTextFileControllerApi.md#free_text_file_convert_using_post) | **POST** /api/freeText/file/convert | freeTextFileConvert
[**free_text_file_upload_using_post**](FreeTextFileControllerApi.md#free_text_file_upload_using_post) | **POST** /api/freeText/file/upload | freeTextFileUpload


# **free_text_file_convert_using_post**
> JobSubmissionResponse free_text_file_convert_using_post(index_name, session_id)

freeTextFileConvert

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_file_controller_api
from qa_client.model.job_submission_response import JobSubmissionResponse
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
    api_instance = free_text_file_controller_api.FreeTextFileControllerApi(api_client)
    index_name = "indexName_example" # str | indexName
    session_id = "sessionId_example" # str | sessionId

    # example passing only required values which don't have defaults set
    try:
        # freeTextFileConvert
        api_response = api_instance.free_text_file_convert_using_post(index_name, session_id)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextFileControllerApi->free_text_file_convert_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| indexName |
 **session_id** | **str**| sessionId |

### Return type

[**JobSubmissionResponse**](JobSubmissionResponse.md)

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

# **free_text_file_upload_using_post**
> GeneralResponse free_text_file_upload_using_post(session_id, file)

freeTextFileUpload

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_file_controller_api
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
    api_instance = free_text_file_controller_api.FreeTextFileControllerApi(api_client)
    session_id = "sessionId_example" # str | sessionId
    file = open('/path/to/file', 'rb') # file_type | file

    # example passing only required values which don't have defaults set
    try:
        # freeTextFileUpload
        api_response = api_instance.free_text_file_upload_using_post(session_id, file)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextFileControllerApi->free_text_file_upload_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| sessionId |
 **file** | **file_type**| file |

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

