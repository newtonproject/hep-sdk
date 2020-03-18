# coding: utf-8

"""
    HEP REST API

    The REST API for HEP protocol  # noqa: E501

    OpenAPI spec version: v1
    Contact: xiawu@zeuux.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RoundData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'round_id': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'votes': 'int',
        'rank': 'int',
        'node_status': 'int',
        'locked_amount': 'str',
        'reward_newforce': 'str',
        'reward_token': 'str',
        'is_partner_node': 'bool',
        'partner_reward_newforce': 'str',
        'partner_reward_token': 'str',
        'partner_node_management_fee': 'str',
        'partner_newforce_data': 'list[NewForceData]',
        'voter_newforce_data': 'list[NewForceData]'
    }

    attribute_map = {
        'round_id': 'round_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'votes': 'votes',
        'rank': 'rank',
        'node_status': 'node_status',
        'locked_amount': 'locked_amount',
        'reward_newforce': 'reward_newforce',
        'reward_token': 'reward_token',
        'is_partner_node': 'is_partner_node',
        'partner_reward_newforce': 'partner_reward_newforce',
        'partner_reward_token': 'partner_reward_token',
        'partner_node_management_fee': 'partner_node_management_fee',
        'partner_newforce_data': 'partner_newforce_data',
        'voter_newforce_data': 'voter_newforce_data'
    }

    def __init__(self, round_id=None, start_time=None, end_time=None, votes=None, rank=None, node_status=None, locked_amount=None, reward_newforce=None, reward_token=None, is_partner_node=None, partner_reward_newforce=None, partner_reward_token=None, partner_node_management_fee=None, partner_newforce_data=None, voter_newforce_data=None):  # noqa: E501
        """RoundData - a model defined in Swagger"""  # noqa: E501
        self._round_id = None
        self._start_time = None
        self._end_time = None
        self._votes = None
        self._rank = None
        self._node_status = None
        self._locked_amount = None
        self._reward_newforce = None
        self._reward_token = None
        self._is_partner_node = None
        self._partner_reward_newforce = None
        self._partner_reward_token = None
        self._partner_node_management_fee = None
        self._partner_newforce_data = None
        self._voter_newforce_data = None
        self.discriminator = None
        self.round_id = round_id
        self.start_time = start_time
        self.end_time = end_time
        self.votes = votes
        self.rank = rank
        self.node_status = node_status
        self.locked_amount = locked_amount
        self.reward_newforce = reward_newforce
        self.reward_token = reward_token
        self.is_partner_node = is_partner_node
        self.partner_reward_newforce = partner_reward_newforce
        self.partner_reward_token = partner_reward_token
        self.partner_node_management_fee = partner_node_management_fee
        self.partner_newforce_data = partner_newforce_data
        self.voter_newforce_data = voter_newforce_data

    @property
    def round_id(self):
        """Gets the round_id of this RoundData.  # noqa: E501


        :return: The round_id of this RoundData.  # noqa: E501
        :rtype: int
        """
        return self._round_id

    @round_id.setter
    def round_id(self, round_id):
        """Sets the round_id of this RoundData.


        :param round_id: The round_id of this RoundData.  # noqa: E501
        :type: int
        """
        if round_id is None:
            raise ValueError("Invalid value for `round_id`, must not be `None`")  # noqa: E501

        self._round_id = round_id

    @property
    def start_time(self):
        """Gets the start_time of this RoundData.  # noqa: E501


        :return: The start_time of this RoundData.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RoundData.


        :param start_time: The start_time of this RoundData.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this RoundData.  # noqa: E501


        :return: The end_time of this RoundData.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RoundData.


        :param end_time: The end_time of this RoundData.  # noqa: E501
        :type: int
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def votes(self):
        """Gets the votes of this RoundData.  # noqa: E501


        :return: The votes of this RoundData.  # noqa: E501
        :rtype: int
        """
        return self._votes

    @votes.setter
    def votes(self, votes):
        """Sets the votes of this RoundData.


        :param votes: The votes of this RoundData.  # noqa: E501
        :type: int
        """
        if votes is None:
            raise ValueError("Invalid value for `votes`, must not be `None`")  # noqa: E501

        self._votes = votes

    @property
    def rank(self):
        """Gets the rank of this RoundData.  # noqa: E501


        :return: The rank of this RoundData.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this RoundData.


        :param rank: The rank of this RoundData.  # noqa: E501
        :type: int
        """
        if rank is None:
            raise ValueError("Invalid value for `rank`, must not be `None`")  # noqa: E501

        self._rank = rank

    @property
    def node_status(self):
        """Gets the node_status of this RoundData.  # noqa: E501


        :return: The node_status of this RoundData.  # noqa: E501
        :rtype: int
        """
        return self._node_status

    @node_status.setter
    def node_status(self, node_status):
        """Sets the node_status of this RoundData.


        :param node_status: The node_status of this RoundData.  # noqa: E501
        :type: int
        """
        if node_status is None:
            raise ValueError("Invalid value for `node_status`, must not be `None`")  # noqa: E501

        self._node_status = node_status

    @property
    def locked_amount(self):
        """Gets the locked_amount of this RoundData.  # noqa: E501


        :return: The locked_amount of this RoundData.  # noqa: E501
        :rtype: str
        """
        return self._locked_amount

    @locked_amount.setter
    def locked_amount(self, locked_amount):
        """Sets the locked_amount of this RoundData.


        :param locked_amount: The locked_amount of this RoundData.  # noqa: E501
        :type: str
        """
        if locked_amount is None:
            raise ValueError("Invalid value for `locked_amount`, must not be `None`")  # noqa: E501

        self._locked_amount = locked_amount

    @property
    def reward_newforce(self):
        """Gets the reward_newforce of this RoundData.  # noqa: E501


        :return: The reward_newforce of this RoundData.  # noqa: E501
        :rtype: str
        """
        return self._reward_newforce

    @reward_newforce.setter
    def reward_newforce(self, reward_newforce):
        """Sets the reward_newforce of this RoundData.


        :param reward_newforce: The reward_newforce of this RoundData.  # noqa: E501
        :type: str
        """
        if reward_newforce is None:
            raise ValueError("Invalid value for `reward_newforce`, must not be `None`")  # noqa: E501

        self._reward_newforce = reward_newforce

    @property
    def reward_token(self):
        """Gets the reward_token of this RoundData.  # noqa: E501


        :return: The reward_token of this RoundData.  # noqa: E501
        :rtype: str
        """
        return self._reward_token

    @reward_token.setter
    def reward_token(self, reward_token):
        """Sets the reward_token of this RoundData.


        :param reward_token: The reward_token of this RoundData.  # noqa: E501
        :type: str
        """
        if reward_token is None:
            raise ValueError("Invalid value for `reward_token`, must not be `None`")  # noqa: E501

        self._reward_token = reward_token

    @property
    def is_partner_node(self):
        """Gets the is_partner_node of this RoundData.  # noqa: E501


        :return: The is_partner_node of this RoundData.  # noqa: E501
        :rtype: bool
        """
        return self._is_partner_node

    @is_partner_node.setter
    def is_partner_node(self, is_partner_node):
        """Sets the is_partner_node of this RoundData.


        :param is_partner_node: The is_partner_node of this RoundData.  # noqa: E501
        :type: bool
        """
        if is_partner_node is None:
            raise ValueError("Invalid value for `is_partner_node`, must not be `None`")  # noqa: E501

        self._is_partner_node = is_partner_node

    @property
    def partner_reward_newforce(self):
        """Gets the partner_reward_newforce of this RoundData.  # noqa: E501


        :return: The partner_reward_newforce of this RoundData.  # noqa: E501
        :rtype: str
        """
        return self._partner_reward_newforce

    @partner_reward_newforce.setter
    def partner_reward_newforce(self, partner_reward_newforce):
        """Sets the partner_reward_newforce of this RoundData.


        :param partner_reward_newforce: The partner_reward_newforce of this RoundData.  # noqa: E501
        :type: str
        """
        if partner_reward_newforce is None:
            raise ValueError("Invalid value for `partner_reward_newforce`, must not be `None`")  # noqa: E501

        self._partner_reward_newforce = partner_reward_newforce

    @property
    def partner_reward_token(self):
        """Gets the partner_reward_token of this RoundData.  # noqa: E501


        :return: The partner_reward_token of this RoundData.  # noqa: E501
        :rtype: str
        """
        return self._partner_reward_token

    @partner_reward_token.setter
    def partner_reward_token(self, partner_reward_token):
        """Sets the partner_reward_token of this RoundData.


        :param partner_reward_token: The partner_reward_token of this RoundData.  # noqa: E501
        :type: str
        """
        if partner_reward_token is None:
            raise ValueError("Invalid value for `partner_reward_token`, must not be `None`")  # noqa: E501

        self._partner_reward_token = partner_reward_token

    @property
    def partner_node_management_fee(self):
        """Gets the partner_node_management_fee of this RoundData.  # noqa: E501


        :return: The partner_node_management_fee of this RoundData.  # noqa: E501
        :rtype: str
        """
        return self._partner_node_management_fee

    @partner_node_management_fee.setter
    def partner_node_management_fee(self, partner_node_management_fee):
        """Sets the partner_node_management_fee of this RoundData.


        :param partner_node_management_fee: The partner_node_management_fee of this RoundData.  # noqa: E501
        :type: str
        """
        if partner_node_management_fee is None:
            raise ValueError("Invalid value for `partner_node_management_fee`, must not be `None`")  # noqa: E501

        self._partner_node_management_fee = partner_node_management_fee

    @property
    def partner_newforce_data(self):
        """Gets the partner_newforce_data of this RoundData.  # noqa: E501


        :return: The partner_newforce_data of this RoundData.  # noqa: E501
        :rtype: list[NewForceData]
        """
        return self._partner_newforce_data

    @partner_newforce_data.setter
    def partner_newforce_data(self, partner_newforce_data):
        """Sets the partner_newforce_data of this RoundData.


        :param partner_newforce_data: The partner_newforce_data of this RoundData.  # noqa: E501
        :type: list[NewForceData]
        """
        if partner_newforce_data is None:
            raise ValueError("Invalid value for `partner_newforce_data`, must not be `None`")  # noqa: E501

        self._partner_newforce_data = partner_newforce_data

    @property
    def voter_newforce_data(self):
        """Gets the voter_newforce_data of this RoundData.  # noqa: E501


        :return: The voter_newforce_data of this RoundData.  # noqa: E501
        :rtype: list[NewForceData]
        """
        return self._voter_newforce_data

    @voter_newforce_data.setter
    def voter_newforce_data(self, voter_newforce_data):
        """Sets the voter_newforce_data of this RoundData.


        :param voter_newforce_data: The voter_newforce_data of this RoundData.  # noqa: E501
        :type: list[NewForceData]
        """
        if voter_newforce_data is None:
            raise ValueError("Invalid value for `voter_newforce_data`, must not be `None`")  # noqa: E501

        self._voter_newforce_data = voter_newforce_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(RoundData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RoundData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other