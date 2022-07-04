# qa_client.FreeTextSourceControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_snippet_using_post**](FreeTextSourceControllerApi.md#extract_snippet_using_post) | **POST** /api/source/extract_snippet | extract_snippet
[**extract_website_using_post**](FreeTextSourceControllerApi.md#extract_website_using_post) | **POST** /api/source/extract_website | extract_website
[**store_website_using_post**](FreeTextSourceControllerApi.md#store_website_using_post) | **POST** /api/source/store_website | store_website


# **extract_snippet_using_post**
> ExtractSnippetResponse extract_snippet_using_post(snippet)

extract_snippet

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_source_controller_api
from qa_client.model.extract_snippet_response import ExtractSnippetResponse
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
    api_instance = free_text_source_controller_api.FreeTextSourceControllerApi(api_client)
    snippet = "snippet_example" # str | snippet

    # example passing only required values which don't have defaults set
    try:
        # extract_snippet
        api_response = api_instance.extract_snippet_using_post(snippet)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextSourceControllerApi->extract_snippet_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet** | **str**| snippet |

### Return type

[**ExtractSnippetResponse**](ExtractSnippetResponse.md)

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

# **extract_website_using_post**
> ExtractContentResponse extract_website_using_post(url)

extract_website

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_source_controller_api
from qa_client.model.extract_content_response import ExtractContentResponse
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
    api_instance = free_text_source_controller_api.FreeTextSourceControllerApi(api_client)
    url = "url_example" # str | url

    # example passing only required values which don't have defaults set
    try:
        # extract_website
        api_response = api_instance.extract_website_using_post(url)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextSourceControllerApi->extract_website_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| url |

### Return type

[**ExtractContentResponse**](ExtractContentResponse.md)

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

# **store_website_using_post**
> StoreWebsiteResponse store_website_using_post(url)

store_website

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_source_controller_api
from qa_client.model.store_website_response import StoreWebsiteResponse
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
    api_instance = free_text_source_controller_api.FreeTextSourceControllerApi(api_client)
    url = "url_example" # str | url

    # example passing only required values which don't have defaults set
    try:
        # store_website
        api_response = api_instance.store_website_using_post(url)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextSourceControllerApi->store_website_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| url |

### Return type

[**StoreWebsiteResponse**](StoreWebsiteResponse.md)

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

