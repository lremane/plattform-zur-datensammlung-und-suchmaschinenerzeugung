# qa_client.QaControllerFreeTextApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**free_text_qa_predict_on_text_using_get**](QaControllerFreeTextApi.md#free_text_qa_predict_on_text_using_get) | **GET** /api/freeText/predict_on_text | freeTextQAPredictOnText
[**free_text_qa_predict_on_website_using_get**](QaControllerFreeTextApi.md#free_text_qa_predict_on_website_using_get) | **GET** /api/freeText/predict_on_website | freeTextQAPredictOnWebsite
[**free_text_qa_predict_using_get**](QaControllerFreeTextApi.md#free_text_qa_predict_using_get) | **GET** /api/freeText/predict | freeTextQAPredict


# **free_text_qa_predict_on_text_using_get**
> PredictResult free_text_qa_predict_on_text_using_get(context, language, question)

freeTextQAPredictOnText

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import qa_controller_free_text_api
from qa_client.model.predict_result import PredictResult
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
    api_instance = qa_controller_free_text_api.QaControllerFreeTextApi(api_client)
    context = "context_example" # str | context
    language = "language_example" # str | language
    question = "question_example" # str | question

    # example passing only required values which don't have defaults set
    try:
        # freeTextQAPredictOnText
        api_response = api_instance.free_text_qa_predict_on_text_using_get(context, language, question)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerFreeTextApi->free_text_qa_predict_on_text_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| context |
 **language** | **str**| language |
 **question** | **str**| question |

### Return type

[**PredictResult**](PredictResult.md)

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

# **free_text_qa_predict_on_website_using_get**
> PredictResult free_text_qa_predict_on_website_using_get(language, question, url)

freeTextQAPredictOnWebsite

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import qa_controller_free_text_api
from qa_client.model.predict_result import PredictResult
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
    api_instance = qa_controller_free_text_api.QaControllerFreeTextApi(api_client)
    language = "language_example" # str | language
    question = "question_example" # str | question
    url = "url_example" # str | url

    # example passing only required values which don't have defaults set
    try:
        # freeTextQAPredictOnWebsite
        api_response = api_instance.free_text_qa_predict_on_website_using_get(language, question, url)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerFreeTextApi->free_text_qa_predict_on_website_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| language |
 **question** | **str**| question |
 **url** | **str**| url |

### Return type

[**PredictResult**](PredictResult.md)

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

# **free_text_qa_predict_using_get**
> PredictResult free_text_qa_predict_using_get(dataset, question, user)

freeTextQAPredict

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import qa_controller_free_text_api
from qa_client.model.predict_result import PredictResult
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
    api_instance = qa_controller_free_text_api.QaControllerFreeTextApi(api_client)
    dataset = "dataset_example" # str | dataset
    question = "question_example" # str | question
    user = "user_example" # str | user

    # example passing only required values which don't have defaults set
    try:
        # freeTextQAPredict
        api_response = api_instance.free_text_qa_predict_using_get(dataset, question, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerFreeTextApi->free_text_qa_predict_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **question** | **str**| question |
 **user** | **str**| user |

### Return type

[**PredictResult**](PredictResult.md)

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

