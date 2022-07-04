# qa_client.SummaServerControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**summa_using_get**](SummaServerControllerApi.md#summa_using_get) | **GET** /api/summaserver/{dataset} | Generates summaries, i.e. most relevant top-k properties, for an item in a dataset


# **summa_using_get**
> SummaServer summa_using_get(dataset, entity, user)

Generates summaries, i.e. most relevant top-k properties, for an item in a dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import summa_server_controller_api
from qa_client.model.summa_server import SummaServer
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
    api_instance = summa_server_controller_api.SummaServerControllerApi(api_client)
    dataset = "dataset_example" # str | dataset
    entity = "entity_example" # str | entity
    user = [
        "user_example",
    ] # [str] | user
    language = "en" # str | language (optional) if omitted the server will use the default value of "en"
    top_k = 5 # int | topK (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # Generates summaries, i.e. most relevant top-k properties, for an item in a dataset
        api_response = api_instance.summa_using_get(dataset, entity, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling SummaServerControllerApi->summa_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generates summaries, i.e. most relevant top-k properties, for an item in a dataset
        api_response = api_instance.summa_using_get(dataset, entity, user, language=language, top_k=top_k)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling SummaServerControllerApi->summa_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **entity** | **str**| entity |
 **user** | **[str]**| user |
 **language** | **str**| language | [optional] if omitted the server will use the default value of "en"
 **top_k** | **int**| topK | [optional] if omitted the server will use the default value of 5

### Return type

[**SummaServer**](SummaServer.md)

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

