# qa_client.AutoCompleteControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete_using_post**](AutoCompleteControllerApi.md#autocomplete_using_post) | **POST** /api/autocomplete | Given a prefix 
[**index_autocomplete_data_using_get**](AutoCompleteControllerApi.md#index_autocomplete_data_using_get) | **GET** /api/autocomplete/index/data | Creates the autocompletion index given the data
[**index_autocomplete_questions_using_get**](AutoCompleteControllerApi.md#index_autocomplete_questions_using_get) | **GET** /api/autocomplete/index/questions | Creates the autocompletion index given the questions


# **autocomplete_using_post**
> [[Chunk]] autocomplete_using_post(kb, lang, size, user, prefix)

Given a prefix 

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import auto_complete_controller_api
from qa_client.model.chunk import Chunk
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
    api_instance = auto_complete_controller_api.AutoCompleteControllerApi(api_client)
    kb = [
        "kb_example",
    ] # [str] | kb
    lang = [
        "lang_example",
    ] # [str] | lang
    size = 1 # int | size
    user = [
        "user_example",
    ] # [str] | user
    prefix = [
        Chunk(
            disambiguation="disambiguation_example",
            image="image_example",
            text="text_example",
            type="type_example",
            uri="uri_example",
            uuid="uuid_example",
        ),
    ] # [Chunk] | prefix

    # example passing only required values which don't have defaults set
    try:
        # Given a prefix 
        api_response = api_instance.autocomplete_using_post(kb, lang, size, user, prefix)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling AutoCompleteControllerApi->autocomplete_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb** | **[str]**| kb |
 **lang** | **[str]**| lang |
 **size** | **int**| size |
 **user** | **[str]**| user |
 **prefix** | [**[Chunk]**](Chunk.md)| prefix |

### Return type

**[[Chunk]]**

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

# **index_autocomplete_data_using_get**
> ApiResponse index_autocomplete_data_using_get(kb, user)

Creates the autocompletion index given the data

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import auto_complete_controller_api
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
    api_instance = auto_complete_controller_api.AutoCompleteControllerApi(api_client)
    kb = [
        "kb_example",
    ] # [str] | kb
    user = [
        "user_example",
    ] # [str] | user

    # example passing only required values which don't have defaults set
    try:
        # Creates the autocompletion index given the data
        api_response = api_instance.index_autocomplete_data_using_get(kb, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling AutoCompleteControllerApi->index_autocomplete_data_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb** | **[str]**| kb |
 **user** | **[str]**| user |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_autocomplete_questions_using_get**
> ApiResponse index_autocomplete_questions_using_get(kb, user)

Creates the autocompletion index given the questions

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import auto_complete_controller_api
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
    api_instance = auto_complete_controller_api.AutoCompleteControllerApi(api_client)
    kb = [
        "kb_example",
    ] # [str] | kb
    user = [
        "user_example",
    ] # [str] | user

    # example passing only required values which don't have defaults set
    try:
        # Creates the autocompletion index given the questions
        api_response = api_instance.index_autocomplete_questions_using_get(kb, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling AutoCompleteControllerApi->index_autocomplete_questions_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb** | **[str]**| kb |
 **user** | **[str]**| user |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

