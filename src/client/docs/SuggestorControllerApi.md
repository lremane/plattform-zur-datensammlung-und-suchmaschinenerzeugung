# qa_client.SuggestorControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**example_questions_using_get**](SuggestorControllerApi.md#example_questions_using_get) | **GET** /api/suggestor/get | Returns example questions based on the questions that are approved in the training dataset


# **example_questions_using_get**
> [Suggestion] example_questions_using_get(kb, lang, user)

Returns example questions based on the questions that are approved in the training dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import suggestor_controller_api
from qa_client.model.suggestion import Suggestion
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
    api_instance = suggestor_controller_api.SuggestorControllerApi(api_client)
    kb = [
        "kb_example",
    ] # [str] | kb
    lang = [
        "lang_example",
    ] # [str] | lang
    user = [
        "user_example",
    ] # [str] | user

    # example passing only required values which don't have defaults set
    try:
        # Returns example questions based on the questions that are approved in the training dataset
        api_response = api_instance.example_questions_using_get(kb, lang, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling SuggestorControllerApi->example_questions_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb** | **[str]**| kb |
 **lang** | **[str]**| lang |
 **user** | **[str]**| user |

### Return type

[**[Suggestion]**](Suggestion.md)

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

