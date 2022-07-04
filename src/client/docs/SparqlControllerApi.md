# qa_client.SparqlControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sparql_compare_answers_using_get**](SparqlControllerApi.md#sparql_compare_answers_using_get) | **GET** /api/sparql/sparqlCompareAnswers | Compares two sparql query based on the answer set
[**sparql_compare_sparql_using_get**](SparqlControllerApi.md#sparql_compare_sparql_using_get) | **GET** /api/sparql/sparqlCompare | Compares two sparql query based on the structure
[**sparql_to_user_using_get**](SparqlControllerApi.md#sparql_to_user_using_get) | **GET** /api/sparql/sparqlToUser | Convertes a SPARQL query in a human readable interpretation


# **sparql_compare_answers_using_get**
> bool sparql_compare_answers_using_get(sparql1)

Compares two sparql query based on the answer set

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import sparql_controller_api
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
    api_instance = sparql_controller_api.SparqlControllerApi(api_client)
    sparql1 = "sparql1_example" # str | sparql1
    kb1 = "kb1_example" # str | kb1 (optional)
    kb2 = "kb2_example" # str | kb2 (optional)
    sparql2 = "sparql2_example" # str | sparql2 (optional)
    user = [
        "user_example",
    ] # [str] | user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Compares two sparql query based on the answer set
        api_response = api_instance.sparql_compare_answers_using_get(sparql1)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling SparqlControllerApi->sparql_compare_answers_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Compares two sparql query based on the answer set
        api_response = api_instance.sparql_compare_answers_using_get(sparql1, kb1=kb1, kb2=kb2, sparql2=sparql2, user=user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling SparqlControllerApi->sparql_compare_answers_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sparql1** | **str**| sparql1 |
 **kb1** | **str**| kb1 | [optional]
 **kb2** | **str**| kb2 | [optional]
 **sparql2** | **str**| sparql2 | [optional]
 **user** | **[str]**| user | [optional]

### Return type

**bool**

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

# **sparql_compare_sparql_using_get**
> bool sparql_compare_sparql_using_get(sparql1)

Compares two sparql query based on the structure

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import sparql_controller_api
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
    api_instance = sparql_controller_api.SparqlControllerApi(api_client)
    sparql1 = "sparql1_example" # str | sparql1
    kb1 = "kb1_example" # str | kb1 (optional)
    kb2 = "kb2_example" # str | kb2 (optional)
    sparql2 = "sparql2_example" # str | sparql2 (optional)
    user = [
        "user_example",
    ] # [str] | user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Compares two sparql query based on the structure
        api_response = api_instance.sparql_compare_sparql_using_get(sparql1)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling SparqlControllerApi->sparql_compare_sparql_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Compares two sparql query based on the structure
        api_response = api_instance.sparql_compare_sparql_using_get(sparql1, kb1=kb1, kb2=kb2, sparql2=sparql2, user=user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling SparqlControllerApi->sparql_compare_sparql_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sparql1** | **str**| sparql1 |
 **kb1** | **str**| kb1 | [optional]
 **kb2** | **str**| kb2 | [optional]
 **sparql2** | **str**| sparql2 | [optional]
 **user** | **[str]**| user | [optional]

### Return type

**bool**

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

# **sparql_to_user_using_get**
> SPARQLToUser sparql_to_user_using_get(dataset, sparql, user)

Convertes a SPARQL query in a human readable interpretation

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import sparql_controller_api
from qa_client.model.sparqlto_user import SPARQLToUser
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
    api_instance = sparql_controller_api.SparqlControllerApi(api_client)
    dataset = "dataset_example" # str | dataset
    sparql = "sparql_example" # str | sparql
    user = "user_example" # str | user
    lang = "en" # str | lang (optional) if omitted the server will use the default value of "en"

    # example passing only required values which don't have defaults set
    try:
        # Convertes a SPARQL query in a human readable interpretation
        api_response = api_instance.sparql_to_user_using_get(dataset, sparql, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling SparqlControllerApi->sparql_to_user_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Convertes a SPARQL query in a human readable interpretation
        api_response = api_instance.sparql_to_user_using_get(dataset, sparql, user, lang=lang)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling SparqlControllerApi->sparql_to_user_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **sparql** | **str**| sparql |
 **user** | **str**| user |
 **lang** | **str**| lang | [optional] if omitted the server will use the default value of "en"

### Return type

[**SPARQLToUser**](SPARQLToUser.md)

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

