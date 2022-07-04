# qa_client.ChatControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotation_using_post**](ChatControllerApi.md#annotation_using_post) | **POST** /api/chat/annotation | annotation
[**chat_full_using_post**](ChatControllerApi.md#chat_full_using_post) | **POST** /api/chat/full | chatFull
[**chat_sparql_using_post**](ChatControllerApi.md#chat_sparql_using_post) | **POST** /api/chat/sparql | chatSparql


# **annotation_using_post**
> MyAnnotation annotation_using_post(chat_request_train)

annotation

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import chat_controller_api
from qa_client.model.my_annotation import MyAnnotation
from qa_client.model.chat_request_train import ChatRequestTrain
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
    api_instance = chat_controller_api.ChatControllerApi(api_client)
    chat_request_train = ChatRequestTrain(
        knowledge_graph=[
            "knowledge_graph_example",
        ],
        language=[
            "language_example",
        ],
        question="question_example",
        question_context=[
            [
                QuestionContext(
                    knowledge_graph="knowledge_graph_example",
                    uri="uri_example",
                    user="user_example",
                ),
            ],
        ],
        sparql="sparql_example",
        user=[
            "user_example",
        ],
    ) # ChatRequestTrain | chatRequestTrain

    # example passing only required values which don't have defaults set
    try:
        # annotation
        api_response = api_instance.annotation_using_post(chat_request_train)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling ChatControllerApi->annotation_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_request_train** | [**ChatRequestTrain**](ChatRequestTrain.md)| chatRequestTrain |

### Return type

[**MyAnnotation**](MyAnnotation.md)

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

# **chat_full_using_post**
> QaResult chat_full_using_post(chat_request)

chatFull

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import chat_controller_api
from qa_client.model.chat_request import ChatRequest
from qa_client.model.qa_result import QaResult
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
    api_instance = chat_controller_api.ChatControllerApi(api_client)
    chat_request = ChatRequest(
        chat=True,
        id=1,
        knowledge_graph=[
            "knowledge_graph_example",
        ],
        language=[
            "language_example",
        ],
        question="question_example",
        question_context=[
            [
                QuestionContext(
                    knowledge_graph="knowledge_graph_example",
                    uri="uri_example",
                    user="user_example",
                ),
            ],
        ],
        timeout=1,
        user=[
            "user_example",
        ],
    ) # ChatRequest | chatRequest

    # example passing only required values which don't have defaults set
    try:
        # chatFull
        api_response = api_instance.chat_full_using_post(chat_request)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling ChatControllerApi->chat_full_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_request** | [**ChatRequest**](ChatRequest.md)| chatRequest |

### Return type

[**QaResult**](QaResult.md)

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

# **chat_sparql_using_post**
> QaResult chat_sparql_using_post(chat_request)

chatSparql

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import chat_controller_api
from qa_client.model.chat_request import ChatRequest
from qa_client.model.qa_result import QaResult
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
    api_instance = chat_controller_api.ChatControllerApi(api_client)
    chat_request = ChatRequest(
        chat=True,
        id=1,
        knowledge_graph=[
            "knowledge_graph_example",
        ],
        language=[
            "language_example",
        ],
        question="question_example",
        question_context=[
            [
                QuestionContext(
                    knowledge_graph="knowledge_graph_example",
                    uri="uri_example",
                    user="user_example",
                ),
            ],
        ],
        timeout=1,
        user=[
            "user_example",
        ],
    ) # ChatRequest | chatRequest

    # example passing only required values which don't have defaults set
    try:
        # chatSparql
        api_response = api_instance.chat_sparql_using_post(chat_request)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling ChatControllerApi->chat_sparql_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_request** | [**ChatRequest**](ChatRequest.md)| chatRequest |

### Return type

[**QaResult**](QaResult.md)

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

