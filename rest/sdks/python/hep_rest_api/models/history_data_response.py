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


class HistoryDataResponse(object):
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
        'total_page': 'int',
        'page_id': 'int',
        'page_size': 'int',
        'data_list': 'list[HistoryData]'
    }

    attribute_map = {
        'total_page': 'total_page',
        'page_id': 'page_id',
        'page_size': 'page_size',
        'data_list': 'data_list'
    }

    def __init__(self, total_page=None, page_id=None, page_size=None, data_list=None):  # noqa: E501
        """HistoryDataResponse - a model defined in Swagger"""  # noqa: E501
        self._total_page = None
        self._page_id = None
        self._page_size = None
        self._data_list = None
        self.discriminator = None
        self.total_page = total_page
        self.page_id = page_id
        self.page_size = page_size
        self.data_list = data_list

    @property
    def total_page(self):
        """Gets the total_page of this HistoryDataResponse.  # noqa: E501

        total number of pages  # noqa: E501

        :return: The total_page of this HistoryDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        """Sets the total_page of this HistoryDataResponse.

        total number of pages  # noqa: E501

        :param total_page: The total_page of this HistoryDataResponse.  # noqa: E501
        :type: int
        """
        if total_page is None:
            raise ValueError("Invalid value for `total_page`, must not be `None`")  # noqa: E501

        self._total_page = total_page

    @property
    def page_id(self):
        """Gets the page_id of this HistoryDataResponse.  # noqa: E501

        Page id  # noqa: E501

        :return: The page_id of this HistoryDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """Sets the page_id of this HistoryDataResponse.

        Page id  # noqa: E501

        :param page_id: The page_id of this HistoryDataResponse.  # noqa: E501
        :type: int
        """
        if page_id is None:
            raise ValueError("Invalid value for `page_id`, must not be `None`")  # noqa: E501

        self._page_id = page_id

    @property
    def page_size(self):
        """Gets the page_size of this HistoryDataResponse.  # noqa: E501

        Page size  # noqa: E501

        :return: The page_size of this HistoryDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this HistoryDataResponse.

        Page size  # noqa: E501

        :param page_size: The page_size of this HistoryDataResponse.  # noqa: E501
        :type: int
        """
        if page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

    @property
    def data_list(self):
        """Gets the data_list of this HistoryDataResponse.  # noqa: E501

        The history data  # noqa: E501

        :return: The data_list of this HistoryDataResponse.  # noqa: E501
        :rtype: list[HistoryData]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        """Sets the data_list of this HistoryDataResponse.

        The history data  # noqa: E501

        :param data_list: The data_list of this HistoryDataResponse.  # noqa: E501
        :type: list[HistoryData]
        """
        if data_list is None:
            raise ValueError("Invalid value for `data_list`, must not be `None`")  # noqa: E501

        self._data_list = data_list

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
        if issubclass(HistoryDataResponse, dict):
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
        if not isinstance(other, HistoryDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
