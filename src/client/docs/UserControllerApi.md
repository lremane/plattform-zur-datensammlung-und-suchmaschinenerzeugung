# qa_client.UserControllerApi

All URIs are relative to *http://qanswer-core1.univ-st-etienne.fr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_all_using_get**](UserControllerApi.md#admin_all_using_get) | **GET** /api/user/admin/all | Get a list of all users
[**admin_remove_using_post**](UserControllerApi.md#admin_remove_using_post) | **POST** /api/user/admin/remove | Remove a user
[**admin_signup_using_post**](UserControllerApi.md#admin_signup_using_post) | **POST** /api/user/admin/signup | Create a new user
[**change_password_admin_using_post**](UserControllerApi.md#change_password_admin_using_post) | **POST** /api/user/admin/changePassword | Change the password for a user
[**change_password_login_using_post**](UserControllerApi.md#change_password_login_using_post) | **POST** /api/user/change_password_when_logged_in | Change the password for a user that is able to login
[**change_password_using_post**](UserControllerApi.md#change_password_using_post) | **POST** /api/user/changePassword | Change the password for a user using the key send by email
[**check_email_availability_using_get**](UserControllerApi.md#check_email_availability_using_get) | **GET** /api/user/checkEmailAvailability | Check if e-mail is available
[**check_username_availability_using_get**](UserControllerApi.md#check_username_availability_using_get) | **GET** /api/user/checkUsernameAvailability | Check if username is available
[**confirm_registration_using_get**](UserControllerApi.md#confirm_registration_using_get) | **GET** /api/user/registrationConfirm | Confirm key of a user send by e-mail on registration
[**me_using_get**](UserControllerApi.md#me_using_get) | **GET** /api/user/me | Information of a user
[**remove_using_get**](UserControllerApi.md#remove_using_get) | **GET** /api/user/remove | Remove a user
[**reset_password_using_post**](UserControllerApi.md#reset_password_using_post) | **POST** /api/user/resetPassword | Ask to reset a password for a user
[**set_cookie_using_get**](UserControllerApi.md#set_cookie_using_get) | **GET** /api/user/set_cookie | Set a cookie for the user
[**signin_using_post**](UserControllerApi.md#signin_using_post) | **POST** /api/user/signin | User login
[**signup_using_post**](UserControllerApi.md#signup_using_post) | **POST** /api/user/signup | Create a new user


# **admin_all_using_get**
> [UserProfile] admin_all_using_get()

Get a list of all users

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.user_profile import UserProfile
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
    api_instance = user_controller_api.UserControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of all users
        api_response = api_instance.admin_all_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->admin_all_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserProfile]**](UserProfile.md)

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

# **admin_remove_using_post**
> ApiResponse admin_remove_using_post(username)

Remove a user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    username = "username_example" # str | username

    # example passing only required values which don't have defaults set
    try:
        # Remove a user
        api_response = api_instance.admin_remove_using_post(username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->admin_remove_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username |

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

# **admin_signup_using_post**
> ApiResponse admin_signup_using_post(sign_up_request)

Create a new user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.sign_up_request import SignUpRequest
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    sign_up_request = SignUpRequest(
        email="email_example",
        name="name_example",
        password="password_example",
        username="username_example",
    ) # SignUpRequest | signUpRequest

    # example passing only required values which don't have defaults set
    try:
        # Create a new user
        api_response = api_instance.admin_signup_using_post(sign_up_request)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->admin_signup_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_up_request** | [**SignUpRequest**](SignUpRequest.md)| signUpRequest |

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **change_password_admin_using_post**
> ApiResponse change_password_admin_using_post(change_password)

Change the password for a user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.api_response import ApiResponse
from qa_client.model.change_password_admin import ChangePasswordAdmin
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    change_password = ChangePasswordAdmin(
        password="password_example",
        username="username_example",
    ) # ChangePasswordAdmin | changePassword

    # example passing only required values which don't have defaults set
    try:
        # Change the password for a user
        api_response = api_instance.change_password_admin_using_post(change_password)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->change_password_admin_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password** | [**ChangePasswordAdmin**](ChangePasswordAdmin.md)| changePassword |

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **change_password_login_using_post**
> ApiResponse change_password_login_using_post(password)

Change the password for a user that is able to login

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.api_response import ApiResponse
from qa_client.model.password import Password
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    password = Password(
        password="password_example",
    ) # Password | password

    # example passing only required values which don't have defaults set
    try:
        # Change the password for a user that is able to login
        api_response = api_instance.change_password_login_using_post(password)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->change_password_login_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | [**Password**](Password.md)| password |

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **change_password_using_post**
> ApiResponse change_password_using_post(change_password)

Change the password for a user using the key send by email

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.change_password import ChangePassword
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    change_password = ChangePassword(
        password="password_example",
        token="token_example",
    ) # ChangePassword | changePassword

    # example passing only required values which don't have defaults set
    try:
        # Change the password for a user using the key send by email
        api_response = api_instance.change_password_using_post(change_password)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->change_password_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password** | [**ChangePassword**](ChangePassword.md)| changePassword |

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **check_email_availability_using_get**
> UserIdentityAvailability check_email_availability_using_get(email)

Check if e-mail is available

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.user_identity_availability import UserIdentityAvailability
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    email = "email_example" # str | email

    # example passing only required values which don't have defaults set
    try:
        # Check if e-mail is available
        api_response = api_instance.check_email_availability_using_get(email)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->check_email_availability_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email |

### Return type

[**UserIdentityAvailability**](UserIdentityAvailability.md)

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

# **check_username_availability_using_get**
> UserIdentityAvailability check_username_availability_using_get(username)

Check if username is available

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.user_identity_availability import UserIdentityAvailability
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    username = "username_example" # str | username

    # example passing only required values which don't have defaults set
    try:
        # Check if username is available
        api_response = api_instance.check_username_availability_using_get(username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->check_username_availability_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username |

### Return type

[**UserIdentityAvailability**](UserIdentityAvailability.md)

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

# **confirm_registration_using_get**
> ApiResponse confirm_registration_using_get(token)

Confirm key of a user send by e-mail on registration

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    token = "token_example" # str | token

    # example passing only required values which don't have defaults set
    try:
        # Confirm key of a user send by e-mail on registration
        api_response = api_instance.confirm_registration_using_get(token)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->confirm_registration_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_using_get**
> UserProfile me_using_get()

Information of a user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.user_profile import UserProfile
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
    api_instance = user_controller_api.UserControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Information of a user
        api_response = api_instance.me_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->me_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

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

# **remove_using_get**
> ApiResponse remove_using_get()

Remove a user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
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
    api_instance = user_controller_api.UserControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Remove a user
        api_response = api_instance.remove_using_get()
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->remove_using_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_using_post**
> ApiResponse reset_password_using_post(reset_password)

Ask to reset a password for a user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.reset_password import ResetPassword
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    reset_password = ResetPassword(
        email="email_example",
    ) # ResetPassword | resetPassword

    # example passing only required values which don't have defaults set
    try:
        # Ask to reset a password for a user
        api_response = api_instance.reset_password_using_post(reset_password)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->reset_password_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password** | [**ResetPassword**](ResetPassword.md)| resetPassword |

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **set_cookie_using_get**
> str set_cookie_using_get(jwt, username)

Set a cookie for the user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    jwt = "jwt_example" # str | jwt
    username = "username_example" # str | username

    # example passing only required values which don't have defaults set
    try:
        # Set a cookie for the user
        api_response = api_instance.set_cookie_using_get(jwt, username)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->set_cookie_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| jwt |
 **username** | **str**| username |

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

# **signin_using_post**
> JwtAuthenticationResponse signin_using_post(login_request)

User login

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.jwt_authentication_response import JwtAuthenticationResponse
from qa_client.model.login_request import LoginRequest
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    login_request = LoginRequest(
        password="password_example",
        username_or_email="username_or_email_example",
    ) # LoginRequest | loginRequest

    # example passing only required values which don't have defaults set
    try:
        # User login
        api_response = api_instance.signin_using_post(login_request)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->signin_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)| loginRequest |

### Return type

[**JwtAuthenticationResponse**](JwtAuthenticationResponse.md)

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

# **signup_using_post**
> ApiResponse signup_using_post(sign_up_request)

Create a new user

### Example

* Api Key Authentication (JWT):

```python
import time
import qa_client
from qa_client.api import user_controller_api
from qa_client.model.sign_up_request import SignUpRequest
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
    api_instance = user_controller_api.UserControllerApi(api_client)
    sign_up_request = SignUpRequest(
        email="email_example",
        name="name_example",
        password="password_example",
        username="username_example",
    ) # SignUpRequest | signUpRequest

    # example passing only required values which don't have defaults set
    try:
        # Create a new user
        api_response = api_instance.signup_using_post(sign_up_request)
        pprint(api_response)
    except qa_client.ApiException as e:
        print("Exception when calling UserControllerApi->signup_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_up_request** | [**SignUpRequest**](SignUpRequest.md)| signUpRequest |

### Return type

[**ApiResponse**](ApiResponse.md)

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

