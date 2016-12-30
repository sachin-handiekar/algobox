# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TradesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def find_trades(self, connection_id, **kwargs):
        """
        Returns the list of trades.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_trades(connection_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connection_id:  (required)
        :param str state: 
        :return: list[Trade]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_trades_with_http_info(connection_id, **kwargs)
        else:
            (data) = self.find_trades_with_http_info(connection_id, **kwargs)
            return data

    def find_trades_with_http_info(self, connection_id, **kwargs):
        """
        Returns the list of trades.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_trades_with_http_info(connection_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str connection_id:  (required)
        :param str state: 
        :return: list[Trade]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connection_id', 'state']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_trades" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params) or (params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `find_trades`")


        collection_formats = {}

        resource_path = '/trades/{connectionId}'.replace('{format}', 'json')
        path_params = {}
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']

        query_params = {}
        if 'state' in params:
            query_params['state'] = params['state']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Trade]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
