# qa_client.TimeControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**time_using_get**](TimeControllerApi.md#time_using_get) | **GET** /api/time/annotate | Identifies dates in a sentence


# **time_using_get**
> [Time] time_using_get()

Identifies dates in a sentence

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import time_controller_api
from qa_client.model.time import Time
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
    api_instance = time_controller_api.TimeControllerApi(api_client)
    lang = "en" # str | lang (optional) if omitted the server will use the default value of "en"
    sentence = "sentence_example" # str | sentence (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Identifies dates in a sentence
        api_response = api_instance.time_using_get(lang=lang, sentence=sentence)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling TimeControllerApi->time_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| lang | [optional] if omitted the server will use the default value of "en"
 **sentence** | **str**| sentence | [optional]

### Return type

[**[Time]**](Time.md)

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

