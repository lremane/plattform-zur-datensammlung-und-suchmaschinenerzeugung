# qa_client.QuestionLogControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate_using_get2**](QuestionLogControllerApi.md#evaluate_using_get2) | **GET** /api/question/log/get | Evaluate the current model on the uploaded question-answer pairs
[**log_question_using_post**](QuestionLogControllerApi.md#log_question_using_post) | **POST** /api/question/log/create | Give new question
[**question_log_remove_all_using_post**](QuestionLogControllerApi.md#question_log_remove_all_using_post) | **POST** /api/question/log/removeall | Remove all the feedback given
[**question_log_remove_using_post**](QuestionLogControllerApi.md#question_log_remove_using_post) | **POST** /api/question/log/remove | Remove one question-answer pair


# **evaluate_using_get2**
> [QuestionLog] evaluate_using_get2()

Evaluate the current model on the uploaded question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import question_log_controller_api
from qa_client.model.question_log import QuestionLog
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
    api_instance = question_log_controller_api.QuestionLogControllerApi(api_client)
    kbs = [
        "kbs_example",
    ] # [str] | kbs (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Evaluate the current model on the uploaded question-answer pairs
        api_response = api_instance.evaluate_using_get2(kbs=kbs)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QuestionLogControllerApi->evaluate_using_get2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kbs** | **[str]**| kbs | [optional]

### Return type

[**[QuestionLog]**](QuestionLog.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_question_using_post**
> ApiResponse log_question_using_post(question)

Give new question

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import question_log_controller_api
from qa_client.model.api_response import ApiResponse
from qa_client.model.question_log import QuestionLog
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
    api_instance = question_log_controller_api.QuestionLogControllerApi(api_client)
    question = QuestionLog(
        answers="answers_example",
        confidence=3.14,
        context="context_example",
        correct=True,
        current_model_right=True,
        id=1,
        kb="kb_example",
        label=3.14,
        language="language_example",
        question="question_example",
        sparql="sparql_example",
        sparql_kb="sparql_kb_example",
        user_id=1,
        user_name="user_name_example",
        validated=True,
    ) # QuestionLog | question

    # example passing only required values which don't have defaults set
    try:
        # Give new question
        api_response = api_instance.log_question_using_post(question)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QuestionLogControllerApi->log_question_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | [**QuestionLog**](QuestionLog.md)| question |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
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

# **question_log_remove_all_using_post**
> bool, date, datetime, dict, float, int, list, str, none_type question_log_remove_all_using_post()

Remove all the feedback given

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import question_log_controller_api
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
    api_instance = question_log_controller_api.QuestionLogControllerApi(api_client)
    kb = [
        "kb_example",
    ] # [str] | kb (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove all the feedback given
        api_response = api_instance.question_log_remove_all_using_post(kb=kb)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QuestionLogControllerApi->question_log_remove_all_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb** | **[str]**| kb | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **question_log_remove_using_post**
> ApiResponse question_log_remove_using_post(question_ids)

Remove one question-answer pair

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import question_log_controller_api
from qa_client.model.remove_request import RemoveRequest
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
    api_instance = question_log_controller_api.QuestionLogControllerApi(api_client)
    question_ids = RemoveRequest(
        question_ids=[
            1,
        ],
    ) # RemoveRequest | questionIds

    # example passing only required values which don't have defaults set
    try:
        # Remove one question-answer pair
        api_response = api_instance.question_log_remove_using_post(question_ids)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QuestionLogControllerApi->question_log_remove_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_ids** | [**RemoveRequest**](RemoveRequest.md)| questionIds |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
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

