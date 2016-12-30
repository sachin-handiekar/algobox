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


class MarketHours(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, market_open=None, market_close=None, orb5min_open=None, orb5min_close=None, previous_market_open=None, previous_market_close=None):
        """
        MarketHours - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'market_open': 'int',
            'market_close': 'int',
            'orb5min_open': 'int',
            'orb5min_close': 'int',
            'previous_market_open': 'int',
            'previous_market_close': 'int'
        }

        self.attribute_map = {
            'market_open': 'marketOpen',
            'market_close': 'marketClose',
            'orb5min_open': 'orb5minOpen',
            'orb5min_close': 'orb5minClose',
            'previous_market_open': 'previousMarketOpen',
            'previous_market_close': 'previousMarketClose'
        }

        self._market_open = market_open
        self._market_close = market_close
        self._orb5min_open = orb5min_open
        self._orb5min_close = orb5min_close
        self._previous_market_open = previous_market_open
        self._previous_market_close = previous_market_close


    @property
    def market_open(self):
        """
        Gets the market_open of this MarketHours.


        :return: The market_open of this MarketHours.
        :rtype: int
        """
        return self._market_open

    @market_open.setter
    def market_open(self, market_open):
        """
        Sets the market_open of this MarketHours.


        :param market_open: The market_open of this MarketHours.
        :type: int
        """

        self._market_open = market_open

    @property
    def market_close(self):
        """
        Gets the market_close of this MarketHours.


        :return: The market_close of this MarketHours.
        :rtype: int
        """
        return self._market_close

    @market_close.setter
    def market_close(self, market_close):
        """
        Sets the market_close of this MarketHours.


        :param market_close: The market_close of this MarketHours.
        :type: int
        """

        self._market_close = market_close

    @property
    def orb5min_open(self):
        """
        Gets the orb5min_open of this MarketHours.


        :return: The orb5min_open of this MarketHours.
        :rtype: int
        """
        return self._orb5min_open

    @orb5min_open.setter
    def orb5min_open(self, orb5min_open):
        """
        Sets the orb5min_open of this MarketHours.


        :param orb5min_open: The orb5min_open of this MarketHours.
        :type: int
        """

        self._orb5min_open = orb5min_open

    @property
    def orb5min_close(self):
        """
        Gets the orb5min_close of this MarketHours.


        :return: The orb5min_close of this MarketHours.
        :rtype: int
        """
        return self._orb5min_close

    @orb5min_close.setter
    def orb5min_close(self, orb5min_close):
        """
        Sets the orb5min_close of this MarketHours.


        :param orb5min_close: The orb5min_close of this MarketHours.
        :type: int
        """

        self._orb5min_close = orb5min_close

    @property
    def previous_market_open(self):
        """
        Gets the previous_market_open of this MarketHours.


        :return: The previous_market_open of this MarketHours.
        :rtype: int
        """
        return self._previous_market_open

    @previous_market_open.setter
    def previous_market_open(self, previous_market_open):
        """
        Sets the previous_market_open of this MarketHours.


        :param previous_market_open: The previous_market_open of this MarketHours.
        :type: int
        """

        self._previous_market_open = previous_market_open

    @property
    def previous_market_close(self):
        """
        Gets the previous_market_close of this MarketHours.


        :return: The previous_market_close of this MarketHours.
        :rtype: int
        """
        return self._previous_market_close

    @previous_market_close.setter
    def previous_market_close(self, previous_market_close):
        """
        Sets the previous_market_close of this MarketHours.


        :param previous_market_close: The previous_market_close of this MarketHours.
        :type: int
        """

        self._previous_market_close = previous_market_close

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
