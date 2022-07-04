# qa_client.AnswerControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**answer_context_using_get**](AnswerControllerApi.md#answer_context_using_get) | **GET** /api/answer/context | Given a SPARQL query returns all information about the answer entities like label, description, images ... 
[**table_context_using_get**](AnswerControllerApi.md#table_context_using_get) | **GET** /api/answer/table | Given a SPARQL query returns the information about the answer entities in the form of a table.


# **answer_context_using_get**
> QaContexts answer_context_using_get(sparql_query)

Given a SPARQL query returns all information about the answer entities like label, description, images ... 

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import answer_controller_api
from qa_client.model.qa_contexts import QaContexts
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
    api_instance = answer_controller_api.AnswerControllerApi(api_client)
    sparql_query = "sparqlQuery_example" # str | sparqlQuery
    kb = "wikidata" # str | kb (optional) if omitted the server will use the default value of "wikidata"
    lang = "en" # str | lang (optional) if omitted the server will use the default value of "en"
    timeout = 7 # int | timeout (optional) if omitted the server will use the default value of 7
    user = "user_example" # str | user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Given a SPARQL query returns all information about the answer entities like label, description, images ... 
        api_response = api_instance.answer_context_using_get(sparql_query)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling AnswerControllerApi->answer_context_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Given a SPARQL query returns all information about the answer entities like label, description, images ... 
        api_response = api_instance.answer_context_using_get(sparql_query, kb=kb, lang=lang, timeout=timeout, user=user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling AnswerControllerApi->answer_context_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sparql_query** | **str**| sparqlQuery |
 **kb** | **str**| kb | [optional] if omitted the server will use the default value of "wikidata"
 **lang** | **str**| lang | [optional] if omitted the server will use the default value of "en"
 **timeout** | **int**| timeout | [optional] if omitted the server will use the default value of 7
 **user** | **str**| user | [optional]

### Return type

[**QaContexts**](QaContexts.md)

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

# **table_context_using_get**
> QaTable table_context_using_get(sparql_query)

Given a SPARQL query returns the information about the answer entities in the form of a table.

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import answer_controller_api
from qa_client.model.qa_table import QaTable
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
    api_instance = answer_controller_api.AnswerControllerApi(api_client)
    sparql_query = "sparqlQuery_example" # str | sparqlQuery
    kb = "wikidata" # str | kb (optional) if omitted the server will use the default value of "wikidata"
    lang = "en" # str | lang (optional) if omitted the server will use the default value of "en"
    limit = 25 # int | limit (optional) if omitted the server will use the default value of 25
    offset = 0 # int | offset (optional) if omitted the server will use the default value of 0
    timeout = 5 # int | timeout (optional) if omitted the server will use the default value of 5
    user = "user_example" # str | user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Given a SPARQL query returns the information about the answer entities in the form of a table.
        api_response = api_instance.table_context_using_get(sparql_query)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling AnswerControllerApi->table_context_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Given a SPARQL query returns the information about the answer entities in the form of a table.
        api_response = api_instance.table_context_using_get(sparql_query, kb=kb, lang=lang, limit=limit, offset=offset, timeout=timeout, user=user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling AnswerControllerApi->table_context_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sparql_query** | **str**| sparqlQuery |
 **kb** | **str**| kb | [optional] if omitted the server will use the default value of "wikidata"
 **lang** | **str**| lang | [optional] if omitted the server will use the default value of "en"
 **limit** | **int**| limit | [optional] if omitted the server will use the default value of 25
 **offset** | **int**| offset | [optional] if omitted the server will use the default value of 0
 **timeout** | **int**| timeout | [optional] if omitted the server will use the default value of 5
 **user** | **str**| user | [optional]

### Return type

[**QaTable**](QaTable.md)

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

