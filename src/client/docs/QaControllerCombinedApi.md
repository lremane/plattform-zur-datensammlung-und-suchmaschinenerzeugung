# qa_client.QaControllerCombinedApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qa_combined_using_post**](QaControllerCombinedApi.md#qa_combined_using_post) | **POST** /api/qa/ask | qaCombined


# **qa_combined_using_post**
> Answer qa_combined_using_post(question)

qaCombined

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import qa_controller_combined_api
from qa_client.model.eu_qanswer_core2_server_controller_payload_combined_question import EuQanswerCore2ServerControllerPayloadCombinedQuestion
from qa_client.model.answer import Answer
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
    api_instance = qa_controller_combined_api.QaControllerCombinedApi(api_client)
    question = EuQanswerCore2ServerControllerPayloadCombinedQuestion(
        datasets=[
            Dataset(
                name="name_example",
                type="GRAPH",
                user="user_example",
            ),
        ],
        language="language_example",
        question="question_example",
        timeout=1,
    ) # EuQanswerCore2ServerControllerPayloadCombinedQuestion | question

    # example passing only required values which don't have defaults set
    try:
        # qaCombined
        api_response = api_instance.qa_combined_using_post(question)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling QaControllerCombinedApi->qa_combined_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | [**EuQanswerCore2ServerControllerPayloadCombinedQuestion**](EuQanswerCore2ServerControllerPayloadCombinedQuestion.md)| question |

### Return type

[**Answer**](Answer.md)

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

