# qa_client.FreeTextFeedbackControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**free_text_feedback_creation_using_post**](FreeTextFeedbackControllerApi.md#free_text_feedback_creation_using_post) | **POST** /api/freeText/feedback | freeTextFeedbackCreation
[**free_text_feedback_deletion_using_delete**](FreeTextFeedbackControllerApi.md#free_text_feedback_deletion_using_delete) | **DELETE** /api/freeText/feedback | freeTextFeedbackDeletion
[**free_text_feedback_list_using_get**](FreeTextFeedbackControllerApi.md#free_text_feedback_list_using_get) | **GET** /api/freeText/feedback/list | freeTextFeedbackList


# **free_text_feedback_creation_using_post**
> ApiResponse free_text_feedback_creation_using_post(free_text_feedback)

freeTextFeedbackCreation

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_feedback_controller_api
from qa_client.model.api_response import ApiResponse
from qa_client.model.free_text_feedback import FreeTextFeedback
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
    api_instance = free_text_feedback_controller_api.FreeTextFeedbackControllerApi(api_client)
    free_text_feedback = FreeTextFeedback(
        answer_correct=True,
        answer_start=1,
        answer_text="answer_text_example",
        context="context_example",
        created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        document_correct=True,
        id=1,
        index_id=1,
        question="question_example",
        user_id=1,
    ) # FreeTextFeedback | freeTextFeedback

    # example passing only required values which don't have defaults set
    try:
        # freeTextFeedbackCreation
        api_response = api_instance.free_text_feedback_creation_using_post(free_text_feedback)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextFeedbackControllerApi->free_text_feedback_creation_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_text_feedback** | [**FreeTextFeedback**](FreeTextFeedback.md)| freeTextFeedback |

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

# **free_text_feedback_deletion_using_delete**
> ApiResponse free_text_feedback_deletion_using_delete(feedback_id)

freeTextFeedbackDeletion

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_feedback_controller_api
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
    api_instance = free_text_feedback_controller_api.FreeTextFeedbackControllerApi(api_client)
    feedback_id = 1 # int | feedbackId

    # example passing only required values which don't have defaults set
    try:
        # freeTextFeedbackDeletion
        api_response = api_instance.free_text_feedback_deletion_using_delete(feedback_id)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextFeedbackControllerApi->free_text_feedback_deletion_using_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **int**| feedbackId |

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **free_text_feedback_list_using_get**
> [FreeTextFeedback] free_text_feedback_list_using_get(index_id)

freeTextFeedbackList

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_feedback_controller_api
from qa_client.model.free_text_feedback import FreeTextFeedback
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
    api_instance = free_text_feedback_controller_api.FreeTextFeedbackControllerApi(api_client)
    index_id = 1 # int | indexId

    # example passing only required values which don't have defaults set
    try:
        # freeTextFeedbackList
        api_response = api_instance.free_text_feedback_list_using_get(index_id)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextFeedbackControllerApi->free_text_feedback_list_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_id** | **int**| indexId |

### Return type

[**[FreeTextFeedback]**](FreeTextFeedback.md)

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

