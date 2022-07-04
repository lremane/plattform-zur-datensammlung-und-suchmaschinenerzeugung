# qa_client.FeedbackControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_train_using_get**](FeedbackControllerApi.md#admin_train_using_get) | **GET** /api/feedback/admin/trainAll | Retrain all datasets models based on the uploaded question-answer pairs
[**create_features_api_using_post**](FeedbackControllerApi.md#create_features_api_using_post) | **POST** /api/feedback/create | Give new feedback for a question answer pair
[**dump_admin_using_get**](FeedbackControllerApi.md#dump_admin_using_get) | **GET** /api/feedback/admin/dump | Download all question-answer pairs
[**dump_features_using_get**](FeedbackControllerApi.md#dump_features_using_get) | **GET** /api/feedback/dump_features | Train a model based on the uploaded question-answer pairs
[**dump_qald_using_get**](FeedbackControllerApi.md#dump_qald_using_get) | **GET** /api/feedback/dump_qald | Download all question-answer pairs in QALD format
[**dump_suggestor_using_get**](FeedbackControllerApi.md#dump_suggestor_using_get) | **GET** /api/feedback/dump_suggestor | dumpSuggestor
[**dump_using_get**](FeedbackControllerApi.md#dump_using_get) | **GET** /api/feedback/dump | Download all question-answer pairs
[**evaluate_using_get**](FeedbackControllerApi.md#evaluate_using_get) | **GET** /api/feedback/evaluate | Evaluate the current model on the uploaded question-answer pairs
[**feedback_upload_using_post**](FeedbackControllerApi.md#feedback_upload_using_post) | **POST** /api/feedback/upload | Upload question-answer pairs
[**remove_all_admin_using_post**](FeedbackControllerApi.md#remove_all_admin_using_post) | **POST** /api/feedback/admin/removeall | Remove all the feedback given
[**remove_all_using_post**](FeedbackControllerApi.md#remove_all_using_post) | **POST** /api/feedback/remove-all-questions | Remove all given question-answer pairs
[**remove_using_post2**](FeedbackControllerApi.md#remove_using_post2) | **POST** /api/feedback/remove | Remove one question-answer pair
[**train_using_get**](FeedbackControllerApi.md#train_using_get) | **GET** /api/feedback/train | Train a model based on the uploaded question-answer pairs
[**upload_admin_using_post**](FeedbackControllerApi.md#upload_admin_using_post) | **POST** /api/feedback/admin/upload | Upload question-answer pairs
[**upload_qald_using_post**](FeedbackControllerApi.md#upload_qald_using_post) | **POST** /api/feedback/upload_qald | Upload question-answer pairs in QALD format
[**upload_specific_using_post**](FeedbackControllerApi.md#upload_specific_using_post) | **POST** /api/feedback/{dataset}/upload | Upload question-answer pairs for specific dataset


# **admin_train_using_get**
> ApiResponse admin_train_using_get()

Retrain all datasets models based on the uploaded question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrain all datasets models based on the uploaded question-answer pairs
        api_response = api_instance.admin_train_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->admin_train_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_features_api_using_post**
> ApiResponse create_features_api_using_post(feedback_request)

Give new feedback for a question answer pair

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
from qa_client.model.feedback_request import FeedbackRequest
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    feedback_request = FeedbackRequest(
        context=[
            [
                QuestionContext(
                    knowledge_graph="knowledge_graph_example",
                    uri="uri_example",
                    user="user_example",
                ),
            ],
        ],
        correct=True,
        knowledgebase=[
            "knowledgebase_example",
        ],
        language=[
            "language_example",
        ],
        question="question_example",
        question_id=1,
        sparql="sparql_example",
        sparql_kb="sparql_kb_example",
        user="user_example",
        validated=True,
    ) # FeedbackRequest | feedbackRequest

    # example passing only required values which don't have defaults set
    try:
        # Give new feedback for a question answer pair
        api_response = api_instance.create_features_api_using_post(feedback_request)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->create_features_api_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_request** | [**FeedbackRequest**](FeedbackRequest.md)| feedbackRequest |

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

# **dump_admin_using_get**
> str dump_admin_using_get()

Download all question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Download all question-answer pairs
        api_response = api_instance.dump_admin_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->dump_admin_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **dump_features_using_get**
> dump_features_using_get()

Train a model based on the uploaded question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    kbs = [
        "kbs_example",
    ] # [str] | kbs (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Train a model based on the uploaded question-answer pairs
        api_instance.dump_features_using_get(kbs=kbs)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->dump_features_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kbs** | **[str]**| kbs | [optional]

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

# **dump_qald_using_get**
> str dump_qald_using_get()

Download all question-answer pairs in QALD format

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    kbs = [
        "kbs_example",
    ] # [str] | kbs (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download all question-answer pairs in QALD format
        api_response = api_instance.dump_qald_using_get(kbs=kbs)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->dump_qald_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kbs** | **[str]**| kbs | [optional]

### Return type

**str**

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

# **dump_suggestor_using_get**
> str dump_suggestor_using_get()

dumpSuggestor

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    kbs = [
        "kbs_example",
    ] # [str] | kbs (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # dumpSuggestor
        api_response = api_instance.dump_suggestor_using_get(kbs=kbs)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->dump_suggestor_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kbs** | **[str]**| kbs | [optional]

### Return type

**str**

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

# **dump_using_get**
> str dump_using_get()

Download all question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    kbs = [
        "kbs_example",
    ] # [str] | kbs (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download all question-answer pairs
        api_response = api_instance.dump_using_get(kbs=kbs)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->dump_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kbs** | **[str]**| kbs | [optional]

### Return type

**str**

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

# **evaluate_using_get**
> FeedbackEvaluation evaluate_using_get()

Evaluate the current model on the uploaded question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
from qa_client.model.feedback_evaluation import FeedbackEvaluation
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    kbs = [
        "kbs_example",
    ] # [str] | kbs (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Evaluate the current model on the uploaded question-answer pairs
        api_response = api_instance.evaluate_using_get(kbs=kbs)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->evaluate_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kbs** | **[str]**| kbs | [optional]

### Return type

[**FeedbackEvaluation**](FeedbackEvaluation.md)

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

# **feedback_upload_using_post**
> ApiResponse feedback_upload_using_post(json)

Upload question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    json = open('/path/to/file', 'rb') # file_type | json

    # example passing only required values which don't have defaults set
    try:
        # Upload question-answer pairs
        api_response = api_instance.feedback_upload_using_post(json)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->feedback_upload_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | **file_type**| json |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **remove_all_admin_using_post**
> bool, date, datetime, dict, float, int, list, str, none_type remove_all_admin_using_post()

Remove all the feedback given

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    kbs = [
        "kbs_example",
    ] # [str] | kbs (optional)
    username = "username_example" # str | username (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove all the feedback given
        api_response = api_instance.remove_all_admin_using_post(kbs=kbs, username=username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->remove_all_admin_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kbs** | **[str]**| kbs | [optional]
 **username** | **str**| username | [optional]

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

# **remove_all_using_post**
> ApiResponse remove_all_using_post(remove_all_request)

Remove all given question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
from qa_client.model.remove_all_questions import RemoveAllQuestions
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    remove_all_request = RemoveAllQuestions(
        knowledge_graphs=[
            "knowledge_graphs_example",
        ],
    ) # RemoveAllQuestions | removeAllRequest

    # example passing only required values which don't have defaults set
    try:
        # Remove all given question-answer pairs
        api_response = api_instance.remove_all_using_post(remove_all_request)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->remove_all_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_all_request** | [**RemoveAllQuestions**](RemoveAllQuestions.md)| removeAllRequest |

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

# **remove_using_post2**
> ApiResponse remove_using_post2(question_ids)

Remove one question-answer pair

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    question_ids = RemoveRequest(
        question_ids=[
            1,
        ],
    ) # RemoveRequest | questionIds

    # example passing only required values which don't have defaults set
    try:
        # Remove one question-answer pair
        api_response = api_instance.remove_using_post2(question_ids)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->remove_using_post2: %s\n" % e)
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

# **train_using_get**
> ApiResponse train_using_get()

Train a model based on the uploaded question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    kbs = [
        "kbs_example",
    ] # [str] | kbs (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Train a model based on the uploaded question-answer pairs
        api_response = api_instance.train_using_get(kbs=kbs)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->train_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kbs** | **[str]**| kbs | [optional]

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_admin_using_post**
> ApiResponse upload_admin_using_post(json)

Upload question-answer pairs

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    json = open('/path/to/file', 'rb') # file_type | json

    # example passing only required values which don't have defaults set
    try:
        # Upload question-answer pairs
        api_response = api_instance.upload_admin_using_post(json)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->upload_admin_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | **file_type**| json |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **upload_qald_using_post**
> ApiResponse upload_qald_using_post(qald_json)

Upload question-answer pairs in QALD format

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    qald_json = open('/path/to/file', 'rb') # file_type | qaldJson

    # example passing only required values which don't have defaults set
    try:
        # Upload question-answer pairs in QALD format
        api_response = api_instance.upload_qald_using_post(qald_json)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->upload_qald_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qald_json** | **file_type**| qaldJson |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **upload_specific_using_post**
> ApiResponse upload_specific_using_post(dataset, json)

Upload question-answer pairs for specific dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import feedback_controller_api
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
    api_instance = feedback_controller_api.FeedbackControllerApi(api_client)
    dataset = "dataset_example" # str | dataset
    json = open('/path/to/file', 'rb') # file_type | json

    # example passing only required values which don't have defaults set
    try:
        # Upload question-answer pairs for specific dataset
        api_response = api_instance.upload_specific_using_post(dataset, json)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FeedbackControllerApi->upload_specific_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **json** | **file_type**| json |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

