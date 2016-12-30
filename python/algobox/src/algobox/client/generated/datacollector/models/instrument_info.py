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


class InstrumentInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, instrument_id=None, instrument_type=None, name=None):
        """
        InstrumentInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'instrument_id': 'str',
            'instrument_type': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'instrument_id': 'instrumentId',
            'instrument_type': 'instrumentType',
            'name': 'name'
        }

        self._instrument_id = instrument_id
        self._instrument_type = instrument_type
        self._name = name


    @property
    def instrument_id(self):
        """
        Gets the instrument_id of this InstrumentInfo.


        :return: The instrument_id of this InstrumentInfo.
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """
        Sets the instrument_id of this InstrumentInfo.


        :param instrument_id: The instrument_id of this InstrumentInfo.
        :type: str
        """

        self._instrument_id = instrument_id

    @property
    def instrument_type(self):
        """
        Gets the instrument_type of this InstrumentInfo.


        :return: The instrument_type of this InstrumentInfo.
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """
        Sets the instrument_type of this InstrumentInfo.


        :param instrument_type: The instrument_type of this InstrumentInfo.
        :type: str
        """

        self._instrument_type = instrument_type

    @property
    def name(self):
        """
        Gets the name of this InstrumentInfo.


        :return: The name of this InstrumentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InstrumentInfo.


        :param name: The name of this InstrumentInfo.
        :type: str
        """

        self._name = name

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
