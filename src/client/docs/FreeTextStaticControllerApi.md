# qa_client.FreeTextStaticControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_pdf_using_get**](FreeTextStaticControllerApi.md#resource_pdf_using_get) | **GET** /resource/access_pdf | resource_pdf
[**resource_using_get**](FreeTextStaticControllerApi.md#resource_using_get) | **GET** /resource/{filename} | resource
[**resource_using_get1**](FreeTextStaticControllerApi.md#resource_using_get1) | **GET** /resource/{folder}/{filename} | resource
[**serve_iframe_using_get**](FreeTextStaticControllerApi.md#serve_iframe_using_get) | **GET** /resource/serve_iframe | serveIframe
[**serve_using_get**](FreeTextStaticControllerApi.md#serve_using_get) | **GET** / | serve


# **resource_pdf_using_get**
> str resource_pdf_using_get(filename)

resource_pdf

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_static_controller_api
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
    api_instance = free_text_static_controller_api.FreeTextStaticControllerApi(api_client)
    filename = "filename_example" # str | filename
    text = "text_example" # str | text (optional)
    username = "username_example" # str | username (optional)

    # example passing only required values which don't have defaults set
    try:
        # resource_pdf
        api_response = api_instance.resource_pdf_using_get(filename)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->resource_pdf_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # resource_pdf
        api_response = api_instance.resource_pdf_using_get(filename, text=text, username=username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->resource_pdf_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| filename |
 **text** | **str**| text | [optional]
 **username** | **str**| username | [optional]

### Return type

**str**

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

# **resource_using_get**
> str resource_using_get(filename)

resource

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_static_controller_api
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
    api_instance = free_text_static_controller_api.FreeTextStaticControllerApi(api_client)
    filename = "filename_example" # str | filename
    username = "username_example" # str | username (optional)

    # example passing only required values which don't have defaults set
    try:
        # resource
        api_response = api_instance.resource_using_get(filename)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->resource_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # resource
        api_response = api_instance.resource_using_get(filename, username=username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->resource_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| filename |
 **username** | **str**| username | [optional]

### Return type

**str**

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

# **resource_using_get1**
> str resource_using_get1(filename, folder)

resource

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_static_controller_api
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
    api_instance = free_text_static_controller_api.FreeTextStaticControllerApi(api_client)
    filename = "filename_example" # str | filename
    folder = "folder_example" # str | folder
    username = "username_example" # str | username (optional)

    # example passing only required values which don't have defaults set
    try:
        # resource
        api_response = api_instance.resource_using_get1(filename, folder)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->resource_using_get1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # resource
        api_response = api_instance.resource_using_get1(filename, folder, username=username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->resource_using_get1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| filename |
 **folder** | **str**| folder |
 **username** | **str**| username | [optional]

### Return type

**str**

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

# **serve_iframe_using_get**
> str serve_iframe_using_get(url)

serveIframe

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_static_controller_api
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
    api_instance = free_text_static_controller_api.FreeTextStaticControllerApi(api_client)
    url = "url_example" # str | url
    username = "username_example" # str | username (optional)

    # example passing only required values which don't have defaults set
    try:
        # serveIframe
        api_response = api_instance.serve_iframe_using_get(url)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->serve_iframe_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # serveIframe
        api_response = api_instance.serve_iframe_using_get(url, username=username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->serve_iframe_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| url |
 **username** | **str**| username | [optional]

### Return type

**str**

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

# **serve_using_get**
> str serve_using_get(url)

serve

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_static_controller_api
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
    api_instance = free_text_static_controller_api.FreeTextStaticControllerApi(api_client)
    url = "url_example" # str | url
    do_inspect = "do_inspect_example" # str | do_inspect (optional)
    username = "username_example" # str | username (optional)

    # example passing only required values which don't have defaults set
    try:
        # serve
        api_response = api_instance.serve_using_get(url)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->serve_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # serve
        api_response = api_instance.serve_using_get(url, do_inspect=do_inspect, username=username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextStaticControllerApi->serve_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| url |
 **do_inspect** | **str**| do_inspect | [optional]
 **username** | **str**| username | [optional]

### Return type

**str**

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

