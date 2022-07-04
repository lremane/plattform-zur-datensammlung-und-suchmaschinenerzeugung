# qa_client.QaControllerKbApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gerbil_using_post**](QaControllerKbApi.md#gerbil_using_post) | **POST** /api/gerbil | Takes a question and returns the answer in the format specified by the GERBIL API
[**qa_full_interpretation_using_get**](QaControllerKbApi.md#qa_full_interpretation_using_get) | **GET** /api/qa/fullInterpretation | Takes a question and returns the SPARQL query, the answer, contextual information about the answer and the interpretation.
[**qa_full_using_get**](QaControllerKbApi.md#qa_full_using_get) | **GET** /api/qa/full | Takes a question and returns the SPARQL query, the answer and contextual information about the answer.
[**qa_sparql_using_get**](QaControllerKbApi.md#qa_sparql_using_get) | **GET** /api/qa/sparql | Takes a question and returns the corresponding SPARQL query.


# **gerbil_using_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type,)} gerbil_using_post(query)

Takes a question and returns the answer in the format specified by the GERBIL API

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import qa_controller_kb_api
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
    api_instance = qa_controller_kb_api.QaControllerKbApi(api_client)
    query = "query_example" # str | query
    kb = "wikidata" # str | kb (optional) if omitted the server will use the default value of "wikidata"
    lang = "en" # str | lang (optional) if omitted the server will use the default value of "en"
    user = [
        "user_example",
    ] # [str] | user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Takes a question and returns the answer in the format specified by the GERBIL API
        api_response = api_instance.gerbil_using_post(query)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerKbApi->gerbil_using_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Takes a question and returns the answer in the format specified by the GERBIL API
        api_response = api_instance.gerbil_using_post(query, kb=kb, lang=lang, user=user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerKbApi->gerbil_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query |
 **kb** | **str**| kb | [optional] if omitted the server will use the default value of "wikidata"
 **lang** | **str**| lang | [optional] if omitted the server will use the default value of "en"
 **user** | **[str]**| user | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type,)}**

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

# **qa_full_interpretation_using_get**
> QaResult qa_full_interpretation_using_get(question)

Takes a question and returns the SPARQL query, the answer, contextual information about the answer and the interpretation.

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import qa_controller_kb_api
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
    api_instance = qa_controller_kb_api.QaControllerKbApi(api_client)
    question = "question_example" # str | question
    id = 1 # int | id (optional)
    kb = [
        "kb_example",
    ] # [str] | kb (optional)
    lang = [
        "lang_example",
    ] # [str] | lang (optional)
    timeout = 5 # int | timeout (optional) if omitted the server will use the default value of 5
    user = [
        "user_example",
    ] # [str] | user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Takes a question and returns the SPARQL query, the answer, contextual information about the answer and the interpretation.
        api_response = api_instance.qa_full_interpretation_using_get(question)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerKbApi->qa_full_interpretation_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Takes a question and returns the SPARQL query, the answer, contextual information about the answer and the interpretation.
        api_response = api_instance.qa_full_interpretation_using_get(question, id=id, kb=kb, lang=lang, timeout=timeout, user=user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerKbApi->qa_full_interpretation_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | **str**| question |
 **id** | **int**| id | [optional]
 **kb** | **[str]**| kb | [optional]
 **lang** | **[str]**| lang | [optional]
 **timeout** | **int**| timeout | [optional] if omitted the server will use the default value of 5
 **user** | **[str]**| user | [optional]

### Return type

[**QaResult**](QaResult.md)

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

# **qa_full_using_get**
> QaResult qa_full_using_get(question)

Takes a question and returns the SPARQL query, the answer and contextual information about the answer.

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import qa_controller_kb_api
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
    api_instance = qa_controller_kb_api.QaControllerKbApi(api_client)
    question = "question_example" # str | question
    id = 1 # int | id (optional)
    kb = [
        "kb_example",
    ] # [str] | kb (optional)
    lang = [
        "lang_example",
    ] # [str] | lang (optional)
    timeout = 5 # int | timeout (optional) if omitted the server will use the default value of 5
    user = [
        "user_example",
    ] # [str] | user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Takes a question and returns the SPARQL query, the answer and contextual information about the answer.
        api_response = api_instance.qa_full_using_get(question)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerKbApi->qa_full_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Takes a question and returns the SPARQL query, the answer and contextual information about the answer.
        api_response = api_instance.qa_full_using_get(question, id=id, kb=kb, lang=lang, timeout=timeout, user=user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerKbApi->qa_full_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | **str**| question |
 **id** | **int**| id | [optional]
 **kb** | **[str]**| kb | [optional]
 **lang** | **[str]**| lang | [optional]
 **timeout** | **int**| timeout | [optional] if omitted the server will use the default value of 5
 **user** | **[str]**| user | [optional]

### Return type

[**QaResult**](QaResult.md)

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

# **qa_sparql_using_get**
> QaResult qa_sparql_using_get(question)

Takes a question and returns the corresponding SPARQL query.

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import qa_controller_kb_api
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
    api_instance = qa_controller_kb_api.QaControllerKbApi(api_client)
    question = "question_example" # str | question
    id = 1 # int | id (optional)
    kb = [
        "kb_example",
    ] # [str] | kb (optional)
    lang = [
        "lang_example",
    ] # [str] | lang (optional)
    user = [
        "user_example",
    ] # [str] | user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Takes a question and returns the corresponding SPARQL query.
        api_response = api_instance.qa_sparql_using_get(question)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerKbApi->qa_sparql_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Takes a question and returns the corresponding SPARQL query.
        api_response = api_instance.qa_sparql_using_get(question, id=id, kb=kb, lang=lang, user=user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerKbApi->qa_sparql_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | **str**| question |
 **id** | **int**| id | [optional]
 **kb** | **[str]**| kb | [optional]
 **lang** | **[str]**| lang | [optional]
 **user** | **[str]**| user | [optional]

### Return type

[**QaResult**](QaResult.md)

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

