# qa_client.RdfFacetBrowserControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rdf_using_get**](RdfFacetBrowserControllerApi.md#rdf_using_get) | **GET** /api/browser/{user}/{dataset}/facet | Gets back the RDF content to render


# **rdf_using_get**
> bool, date, datetime, dict, float, int, list, str, none_type rdf_using_get(accept, dataset, url, user)

Gets back the RDF content to render

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import rdf_facet_browser_controller_api
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
    api_instance = rdf_facet_browser_controller_api.RdfFacetBrowserControllerApi(api_client)
    accept = [
        "accept_example",
    ] # [str] | accept
    dataset = "dataset_example" # str | dataset
    url = "url_example" # str | url
    user = "user_example" # str | user
    language = "en" # str | language (optional) if omitted the server will use the default value of "en"

    # example passing only required values which don't have defaults set
    try:
        # Gets back the RDF content to render
        api_response = api_instance.rdf_using_get(accept, dataset, url, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling RdfFacetBrowserControllerApi->rdf_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets back the RDF content to render
        api_response = api_instance.rdf_using_get(accept, dataset, url, user, language=language)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling RdfFacetBrowserControllerApi->rdf_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **[str]**| accept |
 **dataset** | **str**| dataset |
 **url** | **str**| url |
 **user** | **str**| user |
 **language** | **str**| language | [optional] if omitted the server will use the default value of "en"

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

