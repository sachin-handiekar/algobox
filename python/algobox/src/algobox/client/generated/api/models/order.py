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


class Order(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, created_on=None, updated_on=None, state=None, amount=None, instrument=None, type=None, direction=None, worst_accepted_price=None, close_strategy=None):
        """
        Order - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'created_on': 'int',
            'updated_on': 'int',
            'state': 'str',
            'amount': 'float',
            'instrument': 'str',
            'type': 'str',
            'direction': 'str',
            'worst_accepted_price': 'float',
            'close_strategy': 'CloseStrategy'
        }

        self.attribute_map = {
            'id': 'id',
            'created_on': 'createdOn',
            'updated_on': 'updatedOn',
            'state': 'state',
            'amount': 'amount',
            'instrument': 'instrument',
            'type': 'type',
            'direction': 'direction',
            'worst_accepted_price': 'worstAcceptedPrice',
            'close_strategy': 'closeStrategy'
        }

        self._id = id
        self._created_on = created_on
        self._updated_on = updated_on
        self._state = state
        self._amount = amount
        self._instrument = instrument
        self._type = type
        self._direction = direction
        self._worst_accepted_price = worst_accepted_price
        self._close_strategy = close_strategy


    @property
    def id(self):
        """
        Gets the id of this Order.


        :return: The id of this Order.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Order.


        :param id: The id of this Order.
        :type: str
        """

        self._id = id

    @property
    def created_on(self):
        """
        Gets the created_on of this Order.


        :return: The created_on of this Order.
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this Order.


        :param created_on: The created_on of this Order.
        :type: int
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """
        Gets the updated_on of this Order.


        :return: The updated_on of this Order.
        :rtype: int
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """
        Sets the updated_on of this Order.


        :param updated_on: The updated_on of this Order.
        :type: int
        """

        self._updated_on = updated_on

    @property
    def state(self):
        """
        Gets the state of this Order.


        :return: The state of this Order.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Order.


        :param state: The state of this Order.
        :type: str
        """
        allowed_values = ["PENDING", "FILLED", "CANCELLED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def amount(self):
        """
        Gets the amount of this Order.


        :return: The amount of this Order.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Order.


        :param amount: The amount of this Order.
        :type: float
        """

        self._amount = amount

    @property
    def instrument(self):
        """
        Gets the instrument of this Order.


        :return: The instrument of this Order.
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """
        Sets the instrument of this Order.


        :param instrument: The instrument of this Order.
        :type: str
        """

        self._instrument = instrument

    @property
    def type(self):
        """
        Gets the type of this Order.


        :return: The type of this Order.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Order.


        :param type: The type of this Order.
        :type: str
        """
        allowed_values = ["MARKET", "LIMIT", "STOP", "TAKE_PROFIT", "STOP_LOSS"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def direction(self):
        """
        Gets the direction of this Order.


        :return: The direction of this Order.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this Order.


        :param direction: The direction of this Order.
        :type: str
        """
        allowed_values = ["SHORT", "LONG"]
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def worst_accepted_price(self):
        """
        Gets the worst_accepted_price of this Order.


        :return: The worst_accepted_price of this Order.
        :rtype: float
        """
        return self._worst_accepted_price

    @worst_accepted_price.setter
    def worst_accepted_price(self, worst_accepted_price):
        """
        Sets the worst_accepted_price of this Order.


        :param worst_accepted_price: The worst_accepted_price of this Order.
        :type: float
        """

        self._worst_accepted_price = worst_accepted_price

    @property
    def close_strategy(self):
        """
        Gets the close_strategy of this Order.


        :return: The close_strategy of this Order.
        :rtype: CloseStrategy
        """
        return self._close_strategy

    @close_strategy.setter
    def close_strategy(self, close_strategy):
        """
        Sets the close_strategy of this Order.


        :param close_strategy: The close_strategy of this Order.
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
