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


class RetrieveProofReceiptsRequest(object):
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
        'proof_hashes': 'list[str]'
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
        'proof_hashes': 'proof_hashes'
    }

    def __init__(self, dapp_key=None, protocol=None, version=None, ts=None, nonce=None, os=None, language=None, dapp_signature_method=None, dapp_signature=None, proof_hashes=None):  # noqa: E501
        """RetrieveProofReceiptsRequest - a model defined in Swagger"""  # noqa: E501
        self._dapp_key = None
        self._protocol = None
        self._version = None
        self._ts = None
        self._nonce = None
        self._os = None
        self._language = None
        self._dapp_signature_method = None
        self._dapp_signature = None
        self._proof_hashes = None
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
        self.proof_hashes = proof_hashes

    @property
    def dapp_key(self):
        """Gets the dapp_key of this RetrieveProofReceiptsRequest.  # noqa: E501

        The decentralized application access key  # noqa: E501

        :return: The dapp_key of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dapp_key

    @dapp_key.setter
    def dapp_key(self, dapp_key):
        """Sets the dapp_key of this RetrieveProofReceiptsRequest.

        The decentralized application access key  # noqa: E501

        :param dapp_key: The dapp_key of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: str
        """
        if dapp_key is None:
            raise ValueError("Invalid value for `dapp_key`, must not be `None`")  # noqa: E501

        self._dapp_key = dapp_key

    @property
    def protocol(self):
        """Gets the protocol of this RetrieveProofReceiptsRequest.  # noqa: E501

        The protocol name. default is 'HEP'.  # noqa: E501

        :return: The protocol of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this RetrieveProofReceiptsRequest.

        The protocol name. default is 'HEP'.  # noqa: E501

        :param protocol: The protocol of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def version(self):
        """Gets the version of this RetrieveProofReceiptsRequest.  # noqa: E501

        The protocol version such as '1.0'  # noqa: E501

        :return: The version of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RetrieveProofReceiptsRequest.

        The protocol version such as '1.0'  # noqa: E501

        :param version: The version of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def ts(self):
        """Gets the ts of this RetrieveProofReceiptsRequest.  # noqa: E501

        The current timestamp  # noqa: E501

        :return: The ts of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this RetrieveProofReceiptsRequest.

        The current timestamp  # noqa: E501

        :param ts: The ts of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: int
        """
        if ts is None:
            raise ValueError("Invalid value for `ts`, must not be `None`")  # noqa: E501

        self._ts = ts

    @property
    def nonce(self):
        """Gets the nonce of this RetrieveProofReceiptsRequest.  # noqa: E501

        The random string or auto-increment sequence  # noqa: E501

        :return: The nonce of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this RetrieveProofReceiptsRequest.

        The random string or auto-increment sequence  # noqa: E501

        :param nonce: The nonce of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: str
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def os(self):
        """Gets the os of this RetrieveProofReceiptsRequest.  # noqa: E501

        The operating system of client such as ios, android, dweb,etc.  # noqa: E501

        :return: The os of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this RetrieveProofReceiptsRequest.

        The operating system of client such as ios, android, dweb,etc.  # noqa: E501

        :param os: The os of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: str
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def language(self):
        """Gets the language of this RetrieveProofReceiptsRequest.  # noqa: E501

        The i18n language code such as zh, en, etc.  # noqa: E501

        :return: The language of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RetrieveProofReceiptsRequest.

        The i18n language code such as zh, en, etc.  # noqa: E501

        :param language: The language of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def dapp_signature_method(self):
        """Gets the dapp_signature_method of this RetrieveProofReceiptsRequest.  # noqa: E501

        The signature method used by dapp.  # noqa: E501

        :return: The dapp_signature_method of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dapp_signature_method

    @dapp_signature_method.setter
    def dapp_signature_method(self, dapp_signature_method):
        """Sets the dapp_signature_method of this RetrieveProofReceiptsRequest.

        The signature method used by dapp.  # noqa: E501

        :param dapp_signature_method: The dapp_signature_method of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: str
        """
        if dapp_signature_method is None:
            raise ValueError("Invalid value for `dapp_signature_method`, must not be `None`")  # noqa: E501

        self._dapp_signature_method = dapp_signature_method

    @property
    def dapp_signature(self):
        """Gets the dapp_signature of this RetrieveProofReceiptsRequest.  # noqa: E501

        The signature generated by dapp.  # noqa: E501

        :return: The dapp_signature of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dapp_signature

    @dapp_signature.setter
    def dapp_signature(self, dapp_signature):
        """Sets the dapp_signature of this RetrieveProofReceiptsRequest.

        The signature generated by dapp.  # noqa: E501

        :param dapp_signature: The dapp_signature of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: str
        """
        if dapp_signature is None:
            raise ValueError("Invalid value for `dapp_signature`, must not be `None`")  # noqa: E501

        self._dapp_signature = dapp_signature

    @property
    def proof_hashes(self):
        """Gets the proof_hashes of this RetrieveProofReceiptsRequest.  # noqa: E501

        The proof hashes  # noqa: E501

        :return: The proof_hashes of this RetrieveProofReceiptsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._proof_hashes

    @proof_hashes.setter
    def proof_hashes(self, proof_hashes):
        """Sets the proof_hashes of this RetrieveProofReceiptsRequest.

        The proof hashes  # noqa: E501

        :param proof_hashes: The proof_hashes of this RetrieveProofReceiptsRequest.  # noqa: E501
        :type: list[str]
        """
        if proof_hashes is None:
            raise ValueError("Invalid value for `proof_hashes`, must not be `None`")  # noqa: E501

        self._proof_hashes = proof_hashes

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
        if issubclass(RetrieveProofReceiptsRequest, dict):
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
        if not isinstance(other, RetrieveProofReceiptsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
