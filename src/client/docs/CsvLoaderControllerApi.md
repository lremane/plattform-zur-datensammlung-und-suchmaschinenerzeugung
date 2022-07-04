# qa_client.CsvLoaderControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_csv_datatype_using_post**](CsvLoaderControllerApi.md#get_csv_datatype_using_post) | **POST** /api/loader/csv-datatype | Loads a CSV and resolve datatype of the columns
[**upload_csv_using_post**](CsvLoaderControllerApi.md#upload_csv_using_post) | **POST** /api/loader/csv | Loads a CSV and creates out of it a knowledge graph


# **get_csv_datatype_using_post**
> {str: (str,)} get_csv_datatype_using_post(file)

Loads a CSV and resolve datatype of the columns

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import csv_loader_controller_api
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
    api_instance = csv_loader_controller_api.CsvLoaderControllerApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | file
    separator = "," # str | separator (optional) if omitted the server will use the default value of ","
    split_columns = [
        "splitColumns_example",
    ] # [str] | splitColumns (optional)
    split_separator = "," # str | splitSeparator (optional) if omitted the server will use the default value of ","

    # example passing only required values which don't have defaults set
    try:
        # Loads a CSV and resolve datatype of the columns
        api_response = api_instance.get_csv_datatype_using_post(file)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling CsvLoaderControllerApi->get_csv_datatype_using_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Loads a CSV and resolve datatype of the columns
        api_response = api_instance.get_csv_datatype_using_post(file, separator=separator, split_columns=split_columns, split_separator=split_separator)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling CsvLoaderControllerApi->get_csv_datatype_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**| file |
 **separator** | **str**| separator | [optional] if omitted the server will use the default value of ","
 **split_columns** | **[str]**| splitColumns | [optional]
 **split_separator** | **str**| splitSeparator | [optional] if omitted the server will use the default value of ","

### Return type

**{str: (str,)}**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_csv_using_post**
> ApiResponse upload_csv_using_post(dataset, file)

Loads a CSV and creates out of it a knowledge graph

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import csv_loader_controller_api
from qa_client.model.api_response import ApiResponse
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
    api_instance = csv_loader_controller_api.CsvLoaderControllerApi(api_client)
    dataset = "dataset_example" # str | dataset
    file = open('/path/to/file', 'rb') # file_type | file
    column_label = "columnLabel_example" # str | columnLabel (optional)
    datatypes = "datatypes_example" # str | datatypes (optional)
    header_synonym = "headerSynonym_example" # str | headerSynonym (optional)
    languages = [
        "languages_example",
    ] # [str] | languages (optional)
    separator = "," # str | separator (optional) if omitted the server will use the default value of ","
    split_columns = [
        "splitColumns_example",
    ] # [str] | splitColumns (optional)
    split_separator = "," # str | splitSeparator (optional) if omitted the server will use the default value of ","
    logo = open('/path/to/file', 'rb') # file_type | logo (optional)

    # example passing only required values which don't have defaults set
    try:
        # Loads a CSV and creates out of it a knowledge graph
        api_response = api_instance.upload_csv_using_post(dataset, file)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling CsvLoaderControllerApi->upload_csv_using_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Loads a CSV and creates out of it a knowledge graph
        api_response = api_instance.upload_csv_using_post(dataset, file, column_label=column_label, datatypes=datatypes, header_synonym=header_synonym, languages=languages, separator=separator, split_columns=split_columns, split_separator=split_separator, logo=logo)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling CsvLoaderControllerApi->upload_csv_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **file** | **file_type**| file |
 **column_label** | **str**| columnLabel | [optional]
 **datatypes** | **str**| datatypes | [optional]
 **header_synonym** | **str**| headerSynonym | [optional]
 **languages** | **[str]**| languages | [optional]
 **separator** | **str**| separator | [optional] if omitted the server will use the default value of ","
 **split_columns** | **[str]**| splitColumns | [optional]
 **split_separator** | **str**| splitSeparator | [optional] if omitted the server will use the default value of ","
 **logo** | **file_type**| logo | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

