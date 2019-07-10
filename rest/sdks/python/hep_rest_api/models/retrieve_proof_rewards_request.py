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

from hep_rest_api.models.proof_data import ProofData  # noqa: F401,E501


class RetrieveProofRewardsRequest(object):
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
        'dapp_key': 'str',
        'protocol': 'str',
        'version': 'str',
        'ts': 'int',
        'nonce': 'str',
        'os': 'str',
        'language': 'str',
        'dapp_signature_method': 'str',
        'dapp_signature': 'str',
        'proof_data': 'list[ProofData]'
    }

    attribute_map = {
        'dapp_key': 'dapp_key',
        'protocol': 'protocol',
        'version': 'version',
        'ts': 'ts',
        'nonce': 'nonce',
        'os': 'os',
        'language': 'language',
        'dapp_signature_method': 'dapp_signature_method',
        'dapp_signature': 'dapp_signature',
        'proof_data': 'proof_data'
    }

    def __init__(self, dapp_key=None, protocol=None, version=None, ts=None, nonce=None, os=None, language=None, dapp_signature_method=None, dapp_signature=None, proof_data=None):  # noqa: E501
        """RetrieveProofRewardsRequest - a model defined in Swagger"""  # noqa: E501

        self._dapp_key = None
        self._protocol = None
        self._version = None
        self._ts = None
        self._nonce = None
        self._os = None
        self._language = None
        self._dapp_signature_method = None
        self._dapp_signature = None
        self._proof_data = None
        self.discriminator = None

        self.dapp_key = dapp_key
        self.protocol = protocol
        self.version = version
        self.ts = ts
        self.nonce = nonce
        self.os = os
        self.language = language
        self.dapp_signature_method = dapp_signature_method
        self.dapp_signature = dapp_signature
        self.proof_data = proof_data

    @property
    def dapp_key(self):
        """Gets the dapp_key of this RetrieveProofRewardsRequest.  # noqa: E501

        The decentralized application access key  # noqa: E501

        :return: The dapp_key of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dapp_key

    @dapp_key.setter
    def dapp_key(self, dapp_key):
        """Sets the dapp_key of this RetrieveProofRewardsRequest.

        The decentralized application access key  # noqa: E501

        :param dapp_key: The dapp_key of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: str
        """
        if dapp_key is None:
            raise ValueError("Invalid value for `dapp_key`, must not be `None`")  # noqa: E501
        if dapp_key is not None and len(dapp_key) > 64:
            raise ValueError("Invalid value for `dapp_key`, length must be less than or equal to `64`")  # noqa: E501
        if dapp_key is not None and len(dapp_key) < 1:
            raise ValueError("Invalid value for `dapp_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._dapp_key = dapp_key

    @property
    def protocol(self):
        """Gets the protocol of this RetrieveProofRewardsRequest.  # noqa: E501

        The protocol name. default is 'HEP'.  # noqa: E501

        :return: The protocol of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this RetrieveProofRewardsRequest.

        The protocol name. default is 'HEP'.  # noqa: E501

        :param protocol: The protocol of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        if protocol is not None and len(protocol) > 10:
            raise ValueError("Invalid value for `protocol`, length must be less than or equal to `10`")  # noqa: E501
        if protocol is not None and len(protocol) < 1:
            raise ValueError("Invalid value for `protocol`, length must be greater than or equal to `1`")  # noqa: E501

        self._protocol = protocol

    @property
    def version(self):
        """Gets the version of this RetrieveProofRewardsRequest.  # noqa: E501

        The protocol version such as '1.0'  # noqa: E501

        :return: The version of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RetrieveProofRewardsRequest.

        The protocol version such as '1.0'  # noqa: E501

        :param version: The version of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if version is not None and len(version) > 10:
            raise ValueError("Invalid value for `version`, length must be less than or equal to `10`")  # noqa: E501
        if version is not None and len(version) < 1:
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def ts(self):
        """Gets the ts of this RetrieveProofRewardsRequest.  # noqa: E501

        The current timestamp  # noqa: E501

        :return: The ts of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this RetrieveProofRewardsRequest.

        The current timestamp  # noqa: E501

        :param ts: The ts of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: int
        """
        if ts is None:
            raise ValueError("Invalid value for `ts`, must not be `None`")  # noqa: E501

        self._ts = ts

    @property
    def nonce(self):
        """Gets the nonce of this RetrieveProofRewardsRequest.  # noqa: E501

        The random string or auto-increment sequence  # noqa: E501

        :return: The nonce of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this RetrieveProofRewardsRequest.

        The random string or auto-increment sequence  # noqa: E501

        :param nonce: The nonce of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: str
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501
        if nonce is not None and len(nonce) > 64:
            raise ValueError("Invalid value for `nonce`, length must be less than or equal to `64`")  # noqa: E501
        if nonce is not None and len(nonce) < 1:
            raise ValueError("Invalid value for `nonce`, length must be greater than or equal to `1`")  # noqa: E501

        self._nonce = nonce

    @property
    def os(self):
        """Gets the os of this RetrieveProofRewardsRequest.  # noqa: E501

        The operating system of client such as ios, android, dweb,etc.  # noqa: E501

        :return: The os of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this RetrieveProofRewardsRequest.

        The operating system of client such as ios, android, dweb,etc.  # noqa: E501

        :param os: The os of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: str
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501
        if os is not None and len(os) > 10:
            raise ValueError("Invalid value for `os`, length must be less than or equal to `10`")  # noqa: E501
        if os is not None and len(os) < 1:
            raise ValueError("Invalid value for `os`, length must be greater than or equal to `1`")  # noqa: E501

        self._os = os

    @property
    def language(self):
        """Gets the language of this RetrieveProofRewardsRequest.  # noqa: E501

        The i18n language code such as zh, en, etc.  # noqa: E501

        :return: The language of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RetrieveProofRewardsRequest.

        The i18n language code such as zh, en, etc.  # noqa: E501

        :param language: The language of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501
        if language is not None and len(language) > 10:
            raise ValueError("Invalid value for `language`, length must be less than or equal to `10`")  # noqa: E501
        if language is not None and len(language) < 1:
            raise ValueError("Invalid value for `language`, length must be greater than or equal to `1`")  # noqa: E501

        self._language = language

    @property
    def dapp_signature_method(self):
        """Gets the dapp_signature_method of this RetrieveProofRewardsRequest.  # noqa: E501

        The signature method used by dapp.  # noqa: E501

        :return: The dapp_signature_method of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dapp_signature_method

    @dapp_signature_method.setter
    def dapp_signature_method(self, dapp_signature_method):
        """Sets the dapp_signature_method of this RetrieveProofRewardsRequest.

        The signature method used by dapp.  # noqa: E501

        :param dapp_signature_method: The dapp_signature_method of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: str
        """
        if dapp_signature_method is None:
            raise ValueError("Invalid value for `dapp_signature_method`, must not be `None`")  # noqa: E501
        if dapp_signature_method is not None and len(dapp_signature_method) > 64:
            raise ValueError("Invalid value for `dapp_signature_method`, length must be less than or equal to `64`")  # noqa: E501
        if dapp_signature_method is not None and len(dapp_signature_method) < 1:
            raise ValueError("Invalid value for `dapp_signature_method`, length must be greater than or equal to `1`")  # noqa: E501

        self._dapp_signature_method = dapp_signature_method

    @property
    def dapp_signature(self):
        """Gets the dapp_signature of this RetrieveProofRewardsRequest.  # noqa: E501

        The signature generated by dapp.  # noqa: E501

        :return: The dapp_signature of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dapp_signature

    @dapp_signature.setter
    def dapp_signature(self, dapp_signature):
        """Sets the dapp_signature of this RetrieveProofRewardsRequest.

        The signature generated by dapp.  # noqa: E501

        :param dapp_signature: The dapp_signature of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: str
        """
        if dapp_signature is None:
            raise ValueError("Invalid value for `dapp_signature`, must not be `None`")  # noqa: E501
        if dapp_signature is not None and len(dapp_signature) > 64:
            raise ValueError("Invalid value for `dapp_signature`, length must be less than or equal to `64`")  # noqa: E501
        if dapp_signature is not None and len(dapp_signature) < 1:
            raise ValueError("Invalid value for `dapp_signature`, length must be greater than or equal to `1`")  # noqa: E501

        self._dapp_signature = dapp_signature

    @property
    def proof_data(self):
        """Gets the proof_data of this RetrieveProofRewardsRequest.  # noqa: E501

        The proof data  # noqa: E501

        :return: The proof_data of this RetrieveProofRewardsRequest.  # noqa: E501
        :rtype: list[ProofData]
        """
        return self._proof_data

    @proof_data.setter
    def proof_data(self, proof_data):
        """Sets the proof_data of this RetrieveProofRewardsRequest.

        The proof data  # noqa: E501

        :param proof_data: The proof_data of this RetrieveProofRewardsRequest.  # noqa: E501
        :type: list[ProofData]
        """
        if proof_data is None:
            raise ValueError("Invalid value for `proof_data`, must not be `None`")  # noqa: E501

        self._proof_data = proof_data

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
        if issubclass(RetrieveProofRewardsRequest, dict):
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
        if not isinstance(other, RetrieveProofRewardsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
