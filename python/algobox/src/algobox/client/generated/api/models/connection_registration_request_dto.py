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

from pprint import pformat
from six import iteritems
import re


class ConnectionRegistrationRequestDto(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, connection_id=None, connector_id=None, parameters=None, keep_alive=False):
        """
        ConnectionRegistrationRequestDto - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'connection_id': 'str',
            'connector_id': 'str',
            'parameters': 'dict(str, str)',
            'keep_alive': 'bool'
        }

        self.attribute_map = {
            'connection_id': 'connectionId',
            'connector_id': 'connectorId',
            'parameters': 'parameters',
            'keep_alive': 'keepAlive'
        }

        self._connection_id = connection_id
        self._connector_id = connector_id
        self._parameters = parameters
        self._keep_alive = keep_alive


    @property
    def connection_id(self):
        """
        Gets the connection_id of this ConnectionRegistrationRequestDto.


        :return: The connection_id of this ConnectionRegistrationRequestDto.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this ConnectionRegistrationRequestDto.


        :param connection_id: The connection_id of this ConnectionRegistrationRequestDto.
        :type: str
        """

        self._connection_id = connection_id

    @property
    def connector_id(self):
        """
        Gets the connector_id of this ConnectionRegistrationRequestDto.


        :return: The connector_id of this ConnectionRegistrationRequestDto.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this ConnectionRegistrationRequestDto.


        :param connector_id: The connector_id of this ConnectionRegistrationRequestDto.
        :type: str
        """

        self._connector_id = connector_id

    @property
    def parameters(self):
        """
        Gets the parameters of this ConnectionRegistrationRequestDto.


        :return: The parameters of this ConnectionRegistrationRequestDto.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ConnectionRegistrationRequestDto.


        :param parameters: The parameters of this ConnectionRegistrationRequestDto.
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def keep_alive(self):
        """
        Gets the keep_alive of this ConnectionRegistrationRequestDto.


        :return: The keep_alive of this ConnectionRegistrationRequestDto.
        :rtype: bool
        """
        return self._keep_alive

    @keep_alive.setter
    def keep_alive(self, keep_alive):
        """
        Sets the keep_alive of this ConnectionRegistrationRequestDto.


        :param keep_alive: The keep_alive of this ConnectionRegistrationRequestDto.
        :type: bool
        """

        self._keep_alive = keep_alive

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
