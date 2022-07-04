# qa_client.FreeTextGeneralControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**free_text_check_elastic_search_using_get**](FreeTextGeneralControllerApi.md#free_text_check_elastic_search_using_get) | **GET** /api/freeText/check_elasticsearch | freeTextCheckElasticSearch


# **free_text_check_elastic_search_using_get**
> GeneralResponse free_text_check_elastic_search_using_get()

freeTextCheckElasticSearch

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import free_text_general_controller_api
from qa_client.model.general_response import GeneralResponse
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
    api_instance = free_text_general_controller_api.FreeTextGeneralControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # freeTextCheckElasticSearch
        api_response = api_instance.free_text_check_elastic_search_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling FreeTextGeneralControllerApi->free_text_check_elastic_search_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralResponse**](GeneralResponse.md)

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

