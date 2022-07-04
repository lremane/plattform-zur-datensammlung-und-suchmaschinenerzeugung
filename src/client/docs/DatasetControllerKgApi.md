# qa_client.DatasetControllerKgApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_using_get**](DatasetControllerKgApi.md#download_using_get) | **GET** /api/dataset/download | To download an uploaded RDF dataset in N-triples
[**edit_using_post**](DatasetControllerKgApi.md#edit_using_post) | **POST** /api/dataset/edit | To change the RDF dataset in N-triples of a dataset
[**get_config_using_get**](DatasetControllerKgApi.md#get_config_using_get) | **GET** /api/dataset/config | Get all config parameters of the dataset
[**get_context_using_get**](DatasetControllerKgApi.md#get_context_using_get) | **GET** /api/dataset/mappings | Get all specified properties for contextual information
[**get_list_all_datasets_using_get1**](DatasetControllerKgApi.md#get_list_all_datasets_using_get1) | **GET** /api/dataset/list_all | Lists all datasets uploaded by the user
[**get_list_datasets_admin_using_get**](DatasetControllerKgApi.md#get_list_datasets_admin_using_get) | **GET** /api/dataset/admin/list | List all datasets of a user
[**get_list_datasets_using_get**](DatasetControllerKgApi.md#get_list_datasets_using_get) | **GET** /api/dataset/list | Lists all datasets uploaded by the user
[**get_logo_using_get1**](DatasetControllerKgApi.md#get_logo_using_get1) | **GET** /api/dataset/logo | Retrives the logo of a specific dataset
[**get_open_using_get**](DatasetControllerKgApi.md#get_open_using_get) | **GET** /api/dataset/access | To check the current access of the dataset
[**get_share_using_get**](DatasetControllerKgApi.md#get_share_using_get) | **GET** /api/dataset/share | To check the current access of the dataset
[**index_using_post**](DatasetControllerKgApi.md#index_using_post) | **POST** /api/dataset/index | To index an already uploded RDF dataset before it can be queried
[**remove_using_post1**](DatasetControllerKgApi.md#remove_using_post1) | **POST** /api/dataset/remove | To remove a specific dataset
[**set_config_using_post**](DatasetControllerKgApi.md#set_config_using_post) | **POST** /api/dataset/config | Specify config parameters for the dataset
[**set_context_using_post**](DatasetControllerKgApi.md#set_context_using_post) | **POST** /api/dataset/mappings | Specify specific properties for contextual information
[**set_default_model_using_post**](DatasetControllerKgApi.md#set_default_model_using_post) | **POST** /api/dataset/set_default_model | Set the ML model to the default ones
[**set_open_using_post**](DatasetControllerKgApi.md#set_open_using_post) | **POST** /api/dataset/access | To change the access of the dataset to everyone or only to loggedin users
[**set_share_using_post**](DatasetControllerKgApi.md#set_share_using_post) | **POST** /api/dataset/share | To change the access of the dataset to everyone or only to logged in users
[**upload_using_post**](DatasetControllerKgApi.md#upload_using_post) | **POST** /api/dataset/upload | To upload a new RDF dataset


# **download_using_get**
> bool, date, datetime, dict, float, int, list, str, none_type download_using_get(dataset)

To download an uploaded RDF dataset in N-triples

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # To download an uploaded RDF dataset in N-triples
        api_response = api_instance.download_using_get(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->download_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

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

# **edit_using_post**
> ApiResponse edit_using_post(dataset, file)

To change the RDF dataset in N-triples of a dataset

The N-triples file needs to be syntactically correct!

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = "dataset_example" # str | dataset
    file = open('/path/to/file', 'rb') # file_type | file
    lang = [
        "lang_example",
    ] # [str] | lang (optional)

    # example passing only required values which don't have defaults set
    try:
        # To change the RDF dataset in N-triples of a dataset
        api_response = api_instance.edit_using_post(dataset, file)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->edit_using_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # To change the RDF dataset in N-triples of a dataset
        api_response = api_instance.edit_using_post(dataset, file, lang=lang)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->edit_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **file** | **file_type**| file |
 **lang** | **[str]**| lang | [optional]

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

# **get_config_using_get**
> [DatasetConfigRequest] get_config_using_get(dataset, user)

Get all config parameters of the dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
from qa_client.model.dataset_config_request import DatasetConfigRequest
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = [
        "dataset_example",
    ] # [str] | dataset
    user = [
        "user_example",
    ] # [str] | user

    # example passing only required values which don't have defaults set
    try:
        # Get all config parameters of the dataset
        api_response = api_instance.get_config_using_get(dataset, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->get_config_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **[str]**| dataset |
 **user** | **[str]**| user |

### Return type

[**[DatasetConfigRequest]**](DatasetConfigRequest.md)

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

# **get_context_using_get**
> UIMappings get_context_using_get(dataset)

Get all specified properties for contextual information

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
from qa_client.model.ui_mappings import UIMappings
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # Get all specified properties for contextual information
        api_response = api_instance.get_context_using_get(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->get_context_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

[**UIMappings**](UIMappings.md)

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

# **get_list_all_datasets_using_get1**
> [DatasetDetail] get_list_all_datasets_using_get1()

Lists all datasets uploaded by the user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
from qa_client.model.dataset_detail import DatasetDetail
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Lists all datasets uploaded by the user
        api_response = api_instance.get_list_all_datasets_using_get1()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->get_list_all_datasets_using_get1: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[DatasetDetail]**](DatasetDetail.md)

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

# **get_list_datasets_admin_using_get**
> [UserDataset] get_list_datasets_admin_using_get(username)

List all datasets of a user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
from qa_client.model.user_dataset import UserDataset
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    username = "username_example" # str | username

    # example passing only required values which don't have defaults set
    try:
        # List all datasets of a user
        api_response = api_instance.get_list_datasets_admin_using_get(username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->get_list_datasets_admin_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username |

### Return type

[**[UserDataset]**](UserDataset.md)

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

# **get_list_datasets_using_get**
> [UserDataset] get_list_datasets_using_get()

Lists all datasets uploaded by the user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
from qa_client.model.user_dataset import UserDataset
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Lists all datasets uploaded by the user
        api_response = api_instance.get_list_datasets_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->get_list_datasets_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserDataset]**](UserDataset.md)

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

# **get_logo_using_get1**
> str get_logo_using_get1(dataset, user)

Retrives the logo of a specific dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = "dataset_example" # str | dataset
    user = "user_example" # str | user

    # example passing only required values which don't have defaults set
    try:
        # Retrives the logo of a specific dataset
        api_response = api_instance.get_logo_using_get1(dataset, user)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->get_logo_using_get1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **user** | **str**| user |

### Return type

**str**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_using_get**
> bool get_open_using_get(dataset)

To check the current access of the dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # To check the current access of the dataset
        api_response = api_instance.get_open_using_get(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->get_open_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

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

# **get_share_using_get**
> [str] get_share_using_get(dataset)

To check the current access of the dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # To check the current access of the dataset
        api_response = api_instance.get_share_using_get(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->get_share_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

**[str]**

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

# **index_using_post**
> ApiResponse index_using_post(index_config)

To index an already uploded RDF dataset before it can be queried

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
from qa_client.model.index_config import IndexConfig
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    index_config = IndexConfig(
        dataset="dataset_example",
        lang=[
            "lang_example",
        ],
        properties=[
            "properties_example",
        ],
        subclass=[
            "subclass_example",
        ],
        type=[
            "type_example",
        ],
    ) # IndexConfig | indexConfig

    # example passing only required values which don't have defaults set
    try:
        # To index an already uploded RDF dataset before it can be queried
        api_response = api_instance.index_using_post(index_config)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->index_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_config** | [**IndexConfig**](IndexConfig.md)| indexConfig |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
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

# **remove_using_post1**
> ApiResponse remove_using_post1(dataset)

To remove a specific dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # To remove a specific dataset
        api_response = api_instance.remove_using_post1(dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->remove_using_post1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **set_config_using_post**
> ApiResponse set_config_using_post(dataset_config_request)

Specify config parameters for the dataset

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
from qa_client.model.dataset_config_request import DatasetConfigRequest
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset_config_request = DatasetConfigRequest(
        autocompletion_config=AutocompletionConfig(
            data_suggestion=True,
            graph_suggestion=True,
            question_suggestion=True,
        ),
        dataset="dataset_example",
        feature_types=[
            "feature_types_example",
        ],
        instance_mappings={
            "key": [
                UriMapping(
                    lexicalization="lexicalization_example",
                    uri="uri_example",
                ),
            ],
        },
        languages=[
            "languages_example",
        ],
        number_triples=1,
        properties_modifiers_expansion={
            "key": "key_example",
        },
        properties_properties_expansion={
            "key": "key_example",
        },
        property_mappings={
            "key": [
                UriMapping(
                    lexicalization="lexicalization_example",
                    uri="uri_example",
                ),
            ],
        },
        ranker_config=RankerConfig(
            learning_rate=3.14,
            min_leaf_support=1,
            n_tree_leaves=1,
            n_trees=1,
        ),
        recursive_iteration=1,
        stop_words={
            "key": [
                "key_example",
            ],
        },
        type_properties=[
            "type_properties_example",
        ],
        ui_mappings=UIMappings(
            coordinate=[
                "coordinate_example",
            ],
            dataset="dataset_example",
            description=[
                "description_example",
            ],
            disambiguation=[
                "disambiguation_example",
            ],
            doi=[
                "doi_example",
            ],
            facebook=[
                "facebook_example",
            ],
            geometry=[
                "geometry_example",
            ],
            github=[
                "github_example",
            ],
            homepage=[
                "homepage_example",
            ],
            ignore=[
                "ignore_example",
            ],
            image=[
                "image_example",
            ],
            instagram=[
                "instagram_example",
            ],
            label=[
                "label_example",
            ],
            latitude=[
                "latitude_example",
            ],
            linkedin=[
                "linkedin_example",
            ],
            longitude=[
                "longitude_example",
            ],
            main_label="main_label_example",
            optional=[
                "optional_example",
            ],
            orcid=[
                "orcid_example",
            ],
            osm_relation=[
                "osm_relation_example",
            ],
            time=[
                "time_example",
            ],
            time_series=[
                "time_series_example",
            ],
            twitter=[
                "twitter_example",
            ],
            wikipedia=[
                "wikipedia_example",
            ],
            youtube=[
                "youtube_example",
            ],
        ),
        visualization_order=[
            "SIMPLE",
        ],
    ) # DatasetConfigRequest | datasetConfigRequest

    # example passing only required values which don't have defaults set
    try:
        # Specify config parameters for the dataset
        api_response = api_instance.set_config_using_post(dataset_config_request)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->set_config_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_config_request** | [**DatasetConfigRequest**](DatasetConfigRequest.md)| datasetConfigRequest |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
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

# **set_context_using_post**
> ApiResponse set_context_using_post(ui_mappings)

Specify specific properties for contextual information

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
from qa_client.model.api_response import ApiResponse
from qa_client.model.ui_mappings import UIMappings
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    ui_mappings = UIMappings(
        coordinate=[
            "coordinate_example",
        ],
        dataset="dataset_example",
        description=[
            "description_example",
        ],
        disambiguation=[
            "disambiguation_example",
        ],
        doi=[
            "doi_example",
        ],
        facebook=[
            "facebook_example",
        ],
        geometry=[
            "geometry_example",
        ],
        github=[
            "github_example",
        ],
        homepage=[
            "homepage_example",
        ],
        ignore=[
            "ignore_example",
        ],
        image=[
            "image_example",
        ],
        instagram=[
            "instagram_example",
        ],
        label=[
            "label_example",
        ],
        latitude=[
            "latitude_example",
        ],
        linkedin=[
            "linkedin_example",
        ],
        longitude=[
            "longitude_example",
        ],
        main_label="main_label_example",
        optional=[
            "optional_example",
        ],
        orcid=[
            "orcid_example",
        ],
        osm_relation=[
            "osm_relation_example",
        ],
        time=[
            "time_example",
        ],
        time_series=[
            "time_series_example",
        ],
        twitter=[
            "twitter_example",
        ],
        wikipedia=[
            "wikipedia_example",
        ],
        youtube=[
            "youtube_example",
        ],
    ) # UIMappings | UIMappings

    # example passing only required values which don't have defaults set
    try:
        # Specify specific properties for contextual information
        api_response = api_instance.set_context_using_post(ui_mappings)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->set_context_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ui_mappings** | [**UIMappings**](UIMappings.md)| UIMappings |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
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

# **set_default_model_using_post**
> ApiResponse set_default_model_using_post()

Set the ML model to the default ones

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    kbs = [
        "kbs_example",
    ] # [str] | kbs (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set the ML model to the default ones
        api_response = api_instance.set_default_model_using_post(kbs=kbs)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->set_default_model_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kbs** | **[str]**| kbs | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **set_open_using_post**
> ApiResponse set_open_using_post(access, dataset)

To change the access of the dataset to everyone or only to loggedin users

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    access = True # bool | access
    dataset = "dataset_example" # str | dataset

    # example passing only required values which don't have defaults set
    try:
        # To change the access of the dataset to everyone or only to loggedin users
        api_response = api_instance.set_open_using_post(access, dataset)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->set_open_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access** | **bool**| access |
 **dataset** | **str**| dataset |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **set_share_using_post**
> ApiResponse set_share_using_post(dataset, users)

To change the access of the dataset to everyone or only to logged in users

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = "dataset_example" # str | dataset
    users = [
        "users_example",
    ] # [str] | users

    # example passing only required values which don't have defaults set
    try:
        # To change the access of the dataset to everyone or only to logged in users
        api_response = api_instance.set_share_using_post(dataset, users)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->set_share_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **users** | **[str]**| users |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **upload_using_post**
> ApiResponse upload_using_post(dataset, file)

To upload a new RDF dataset

The RDF file needs to be syntactically correct! The logo needs to be a 50x50px PNG image. It is optional.

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import dataset_controller_kg_api
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
    api_instance = dataset_controller_kg_api.DatasetControllerKgApi(api_client)
    dataset = "dataset_example" # str | dataset
    file = open('/path/to/file', 'rb') # file_type | file
    logo = open('/path/to/file', 'rb') # file_type | logo (optional)

    # example passing only required values which don't have defaults set
    try:
        # To upload a new RDF dataset
        api_response = api_instance.upload_using_post(dataset, file)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->upload_using_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # To upload a new RDF dataset
        api_response = api_instance.upload_using_post(dataset, file, logo=logo)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling DatasetControllerKgApi->upload_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| dataset |
 **file** | **file_type**| file |
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

