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


class ConnectionInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, connection_status=None, connection_date_utc=None):
        """
        ConnectionInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'connection_status': 'str',
            'connection_date_utc': 'int'
        }

        self.attribute_map = {
            'connection_status': 'connectionStatus',
            'connection_date_utc': 'connectionDateUtc'
        }

        self._connection_status = connection_status
        self._connection_date_utc = connection_date_utc


    @property
    def connection_status(self):
        """
        Gets the connection_status of this ConnectionInfo.


        :return: The connection_status of this ConnectionInfo.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this ConnectionInfo.


        :param connection_status: The connection_status of this ConnectionInfo.
        :type: str
        """
        allowed_values = ["CONNECTED", "CONNECTING", "DISCONNECTING", "DISCONNECTED"]
        if connection_status not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_status` ({0}), must be one of {1}"
                .format(connection_status, allowed_values)
            )

        self._connection_status = connection_status

    @property
    def connection_date_utc(self):
        """
        Gets the connection_date_utc of this ConnectionInfo.


        :return: The connection_date_utc of this ConnectionInfo.
        :rtype: int
        """
        return self._connection_date_utc

    @connection_date_utc.setter
    def connection_date_utc(self, connection_date_utc):
        """
        Sets the connection_date_utc of this ConnectionInfo.


        :param connection_date_utc: The connection_date_utc of this ConnectionInfo.
        :type: int
        """

        self._connection_date_utc = connection_date_utc

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
