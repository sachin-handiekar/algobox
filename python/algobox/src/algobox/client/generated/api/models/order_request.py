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


class OrderRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, order_request_id=None, connection_id=None, instrument_id=None, amount=None, price_tick=None, open_strategy=None, close_strategy=None):
        """
        OrderRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'order_request_id': 'str',
            'connection_id': 'str',
            'instrument_id': 'str',
            'amount': 'float',
            'price_tick': 'PriceTick',
            'open_strategy': 'OpenStrategy',
            'close_strategy': 'CloseStrategy'
        }

        self.attribute_map = {
            'order_request_id': 'orderRequestId',
            'connection_id': 'connectionId',
            'instrument_id': 'instrumentId',
            'amount': 'amount',
            'price_tick': 'priceTick',
            'open_strategy': 'openStrategy',
            'close_strategy': 'closeStrategy'
        }

        self._order_request_id = order_request_id
        self._connection_id = connection_id
        self._instrument_id = instrument_id
        self._amount = amount
        self._price_tick = price_tick
        self._open_strategy = open_strategy
        self._close_strategy = close_strategy


    @property
    def order_request_id(self):
        """
        Gets the order_request_id of this OrderRequest.


        :return: The order_request_id of this OrderRequest.
        :rtype: str
        """
        return self._order_request_id

    @order_request_id.setter
    def order_request_id(self, order_request_id):
        """
        Sets the order_request_id of this OrderRequest.


        :param order_request_id: The order_request_id of this OrderRequest.
        :type: str
        """

        self._order_request_id = order_request_id

    @property
    def connection_id(self):
        """
        Gets the connection_id of this OrderRequest.


        :return: The connection_id of this OrderRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this OrderRequest.


        :param connection_id: The connection_id of this OrderRequest.
        :type: str
        """

        self._connection_id = connection_id

    @property
    def instrument_id(self):
        """
        Gets the instrument_id of this OrderRequest.


        :return: The instrument_id of this OrderRequest.
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """
        Sets the instrument_id of this OrderRequest.


        :param instrument_id: The instrument_id of this OrderRequest.
        :type: str
        """

        self._instrument_id = instrument_id

    @property
    def amount(self):
        """
        Gets the amount of this OrderRequest.


        :return: The amount of this OrderRequest.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this OrderRequest.


        :param amount: The amount of this OrderRequest.
        :type: float
        """

        self._amount = amount

    @property
    def price_tick(self):
        """
        Gets the price_tick of this OrderRequest.


        :return: The price_tick of this OrderRequest.
        :rtype: PriceTick
        """
        return self._price_tick

    @price_tick.setter
    def price_tick(self, price_tick):
        """
        Sets the price_tick of this OrderRequest.


        :param price_tick: The price_tick of this OrderRequest.
        :type: PriceTick
        """

        self._price_tick = price_tick

    @property
    def open_strategy(self):
        """
        Gets the open_strategy of this OrderRequest.


        :return: The open_strategy of this OrderRequest.
        :rtype: OpenStrategy
        """
        return self._open_strategy

    @open_strategy.setter
    def open_strategy(self, open_strategy):
        """
        Sets the open_strategy of this OrderRequest.


        :param open_strategy: The open_strategy of this OrderRequest.
        :type: OpenStrategy
        """

        self._open_strategy = open_strategy

    @property
    def close_strategy(self):
        """
        Gets the close_strategy of this OrderRequest.


        :return: The close_strategy of this OrderRequest.
        :rtype: CloseStrategy
        """
        return self._close_strategy

    @close_strategy.setter
    def close_strategy(self, close_strategy):
        """
        Sets the close_strategy of this OrderRequest.


        :param close_strategy: The close_strategy of this OrderRequest.
        :type: CloseStrategy
        """

        self._close_strategy = close_strategy

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
