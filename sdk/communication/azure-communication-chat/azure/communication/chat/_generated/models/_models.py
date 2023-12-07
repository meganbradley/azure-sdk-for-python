# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AddChatParticipantsRequest(msrest.serialization.Model):
    """Participants to be added to the thread.

    All required parameters must be populated in order to send to Azure.

    :param participants: Required. Participants to add to a chat thread.
    :type participants: list[~azure.communication.chat.models.ChatParticipant]
    """

    _validation = {
        'participants': {'required': True},
    }

    _attribute_map = {
        'participants': {'key': 'participants', 'type': '[ChatParticipant]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AddChatParticipantsRequest, self).__init__(**kwargs)
        self.participants = kwargs['participants']


class AddChatParticipantsResult(msrest.serialization.Model):
    """Result of the add chat participants operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar invalid_participants: The participants that failed to be added to the chat thread.
    :vartype invalid_participants: list[~azure.communication.chat.models.ChatError]
    """

    _validation = {
        'invalid_participants': {'readonly': True},
    }

    _attribute_map = {
        'invalid_participants': {'key': 'invalidParticipants', 'type': '[ChatError]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AddChatParticipantsResult, self).__init__(**kwargs)
        self.invalid_participants = None


class ChatError(msrest.serialization.Model):
    """The Communication Services error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error code.
    :type code: str
    :param message: Required. The error message.
    :type message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: Further details about specific errors that led to this error.
    :vartype details: list[~azure.communication.chat.models.ChatError]
    :ivar inner_error: The inner error if any.
    :vartype inner_error: ~azure.communication.chat.models.ChatError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ChatError]'},
        'inner_error': {'key': 'innererror', 'type': 'ChatError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatError, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = None
        self.details = None
        self.inner_error = None


class ChatMessage(msrest.serialization.Model):
    """Chat message.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The id of the chat message. This id is server generated.
    :type id: str
    :param type: Required. The chat message type. Possible values include: "text", "html",
     "topicUpdated", "participantAdded", "participantRemoved".
    :type type: str or ~azure.communication.chat.models.ChatMessageType
    :param sequence_id: Required. Sequence of the chat message in the conversation.
    :type sequence_id: str
    :param version: Required. Version of the chat message.
    :type version: str
    :param content: Content of a chat message.
    :type content: ~azure.communication.chat.models.ChatMessageContent
    :param sender_display_name: The display name of the chat message sender. This property is used
     to populate sender name for push notifications.
    :type sender_display_name: str
    :param created_on: Required. The timestamp when the chat message arrived at the server. The
     timestamp is in RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
    :type created_on: ~datetime.datetime
    :param sender_communication_identifier: Identifies a participant in Azure Communication
     services. A participant is, for example, a phone number or an Azure communication user. This
     model must be interpreted as a union: Apart from rawId, at most one further property may be
     set.
    :type sender_communication_identifier:
     ~azure.communication.chat.models.CommunicationIdentifierModel
    :param deleted_on: The timestamp (if applicable) when the message was deleted. The timestamp is
     in RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
    :type deleted_on: ~datetime.datetime
    :param edited_on: The last timestamp (if applicable) when the message was edited. The timestamp
     is in RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
    :type edited_on: ~datetime.datetime
    :param metadata: Message metadata.
    :type metadata: dict[str, str]
    """

    _validation = {
        'id': {'required': True},
        'type': {'required': True},
        'sequence_id': {'required': True},
        'version': {'required': True},
        'created_on': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'sequence_id': {'key': 'sequenceId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'content': {'key': 'content', 'type': 'ChatMessageContent'},
        'sender_display_name': {'key': 'senderDisplayName', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'sender_communication_identifier': {'key': 'senderCommunicationIdentifier', 'type': 'CommunicationIdentifierModel'},
        'deleted_on': {'key': 'deletedOn', 'type': 'iso-8601'},
        'edited_on': {'key': 'editedOn', 'type': 'iso-8601'},
        'metadata': {'key': 'metadata', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatMessage, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.type = kwargs['type']
        self.sequence_id = kwargs['sequence_id']
        self.version = kwargs['version']
        self.content = kwargs.get('content', None)
        self.sender_display_name = kwargs.get('sender_display_name', None)
        self.created_on = kwargs['created_on']
        self.sender_communication_identifier = kwargs.get('sender_communication_identifier', None)
        self.deleted_on = kwargs.get('deleted_on', None)
        self.edited_on = kwargs.get('edited_on', None)
        self.metadata = kwargs.get('metadata', None)


class ChatMessageContent(msrest.serialization.Model):
    """Content of a chat message.

    :param message: Chat message content for messages of types text or html.
    :type message: str
    :param topic: Chat message content for messages of type topicUpdated.
    :type topic: str
    :param participants: Chat message content for messages of types participantAdded or
     participantRemoved.
    :type participants: list[~azure.communication.chat.models.ChatParticipant]
    :param initiator_communication_identifier: Identifies a participant in Azure Communication
     services. A participant is, for example, a phone number or an Azure communication user. This
     model must be interpreted as a union: Apart from rawId, at most one further property may be
     set.
    :type initiator_communication_identifier:
     ~azure.communication.chat.models.CommunicationIdentifierModel
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'topic': {'key': 'topic', 'type': 'str'},
        'participants': {'key': 'participants', 'type': '[ChatParticipant]'},
        'initiator_communication_identifier': {'key': 'initiatorCommunicationIdentifier', 'type': 'CommunicationIdentifierModel'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatMessageContent, self).__init__(**kwargs)
        self.message = kwargs.get('message', None)
        self.topic = kwargs.get('topic', None)
        self.participants = kwargs.get('participants', None)
        self.initiator_communication_identifier = kwargs.get('initiator_communication_identifier', None)


class ChatMessageReadReceipt(msrest.serialization.Model):
    """A chat message read receipt indicates the time a chat message was read by a recipient.

    All required parameters must be populated in order to send to Azure.

    :param sender_communication_identifier: Required. Identifies a participant in Azure
     Communication services. A participant is, for example, a phone number or an Azure communication
     user. This model must be interpreted as a union: Apart from rawId, at most one further property
     may be set.
    :type sender_communication_identifier:
     ~azure.communication.chat.models.CommunicationIdentifierModel
    :param chat_message_id: Required. Id of the chat message that has been read. This id is
     generated by the server.
    :type chat_message_id: str
    :param read_on: Required. The time at which the message was read. The timestamp is in RFC3339
     format: ``yyyy-MM-ddTHH:mm:ssZ``.
    :type read_on: ~datetime.datetime
    """

    _validation = {
        'sender_communication_identifier': {'required': True},
        'chat_message_id': {'required': True},
        'read_on': {'required': True},
    }

    _attribute_map = {
        'sender_communication_identifier': {'key': 'senderCommunicationIdentifier', 'type': 'CommunicationIdentifierModel'},
        'chat_message_id': {'key': 'chatMessageId', 'type': 'str'},
        'read_on': {'key': 'readOn', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatMessageReadReceipt, self).__init__(**kwargs)
        self.sender_communication_identifier = kwargs['sender_communication_identifier']
        self.chat_message_id = kwargs['chat_message_id']
        self.read_on = kwargs['read_on']


class ChatMessageReadReceiptsCollection(msrest.serialization.Model):
    """A paged collection of chat message read receipts.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Collection of chat message read receipts.
    :type value: list[~azure.communication.chat.models.ChatMessageReadReceipt]
    :ivar next_link: If there are more chat message read receipts that can be retrieved, the next
     link will be populated.
    :vartype next_link: str
    """

    _validation = {
        'value': {'required': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ChatMessageReadReceipt]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatMessageReadReceiptsCollection, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = None


class ChatMessagesCollection(msrest.serialization.Model):
    """Collection of chat messages for a particular chat thread.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Collection of chat messages.
    :type value: list[~azure.communication.chat.models.ChatMessage]
    :ivar next_link: If there are more chat messages that can be retrieved, the next link will be
     populated.
    :vartype next_link: str
    """

    _validation = {
        'value': {'required': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ChatMessage]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatMessagesCollection, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = None


class ChatParticipant(msrest.serialization.Model):
    """A participant of the chat thread.

    All required parameters must be populated in order to send to Azure.

    :param communication_identifier: Required. Identifies a participant in Azure Communication
     services. A participant is, for example, a phone number or an Azure communication user. This
     model must be interpreted as a union: Apart from rawId, at most one further property may be
     set.
    :type communication_identifier: ~azure.communication.chat.models.CommunicationIdentifierModel
    :param display_name: Display name for the chat participant.
    :type display_name: str
    :param share_history_time: Time from which the chat history is shared with the participant. The
     timestamp is in RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
    :type share_history_time: ~datetime.datetime
    """

    _validation = {
        'communication_identifier': {'required': True},
    }

    _attribute_map = {
        'communication_identifier': {'key': 'communicationIdentifier', 'type': 'CommunicationIdentifierModel'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'share_history_time': {'key': 'shareHistoryTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatParticipant, self).__init__(**kwargs)
        self.communication_identifier = kwargs['communication_identifier']
        self.display_name = kwargs.get('display_name', None)
        self.share_history_time = kwargs.get('share_history_time', None)


class ChatParticipantsCollection(msrest.serialization.Model):
    """Collection of participants belong to a particular thread.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Chat participants.
    :type value: list[~azure.communication.chat.models.ChatParticipant]
    :ivar next_link: If there are more chat participants that can be retrieved, the next link will
     be populated.
    :vartype next_link: str
    """

    _validation = {
        'value': {'required': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ChatParticipant]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatParticipantsCollection, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = None


class ChatThreadItem(msrest.serialization.Model):
    """Summary information of a chat thread.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Chat thread id.
    :type id: str
    :param topic: Required. Chat thread topic.
    :type topic: str
    :param deleted_on: The timestamp when the chat thread was deleted. The timestamp is in RFC3339
     format: ``yyyy-MM-ddTHH:mm:ssZ``.
    :type deleted_on: ~datetime.datetime
    :ivar last_message_received_on: The timestamp when the last message arrived at the server. The
     timestamp is in RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
    :vartype last_message_received_on: ~datetime.datetime
    """

    _validation = {
        'id': {'required': True},
        'topic': {'required': True},
        'last_message_received_on': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'topic': {'key': 'topic', 'type': 'str'},
        'deleted_on': {'key': 'deletedOn', 'type': 'iso-8601'},
        'last_message_received_on': {'key': 'lastMessageReceivedOn', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatThreadItem, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.topic = kwargs['topic']
        self.deleted_on = kwargs.get('deleted_on', None)
        self.last_message_received_on = None


class ChatThreadProperties(msrest.serialization.Model):
    """Chat thread.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Chat thread id.
    :type id: str
    :param topic: Required. Chat thread topic.
    :type topic: str
    :param created_on: Required. The timestamp when the chat thread was created. The timestamp is
     in RFC3339 format: ``yyyy-MM-ddTHH:mm:ssZ``.
    :type created_on: ~datetime.datetime
    :param created_by_communication_identifier: Required. Identifies a participant in Azure
     Communication services. A participant is, for example, a phone number or an Azure communication
     user. This model must be interpreted as a union: Apart from rawId, at most one further property
     may be set.
    :type created_by_communication_identifier:
     ~azure.communication.chat.models.CommunicationIdentifierModel
    :param deleted_on: The timestamp when the chat thread was deleted. The timestamp is in RFC3339
     format: ``yyyy-MM-ddTHH:mm:ssZ``.
    :type deleted_on: ~datetime.datetime
    """

    _validation = {
        'id': {'required': True},
        'topic': {'required': True},
        'created_on': {'required': True},
        'created_by_communication_identifier': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'topic': {'key': 'topic', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'created_by_communication_identifier': {'key': 'createdByCommunicationIdentifier', 'type': 'CommunicationIdentifierModel'},
        'deleted_on': {'key': 'deletedOn', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatThreadProperties, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.topic = kwargs['topic']
        self.created_on = kwargs['created_on']
        self.created_by_communication_identifier = kwargs['created_by_communication_identifier']
        self.deleted_on = kwargs.get('deleted_on', None)


class ChatThreadsItemCollection(msrest.serialization.Model):
    """Collection of chat threads.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Collection of chat threads.
    :type value: list[~azure.communication.chat.models.ChatThreadItem]
    :ivar next_link: If there are more chat threads that can be retrieved, the next link will be
     populated.
    :vartype next_link: str
    """

    _validation = {
        'value': {'required': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ChatThreadItem]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChatThreadsItemCollection, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = None


class CommunicationErrorResponse(msrest.serialization.Model):
    """The Communication Services error.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. The Communication Services error.
    :type error: ~azure.communication.chat.models.ChatError
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ChatError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CommunicationErrorResponse, self).__init__(**kwargs)
        self.error = kwargs['error']


class CommunicationIdentifierModel(msrest.serialization.Model):
    """Identifies a participant in Azure Communication services. A participant is, for example, a phone number or an Azure communication user. This model must be interpreted as a union: Apart from rawId, at most one further property may be set.

    :param raw_id: Raw Id of the identifier. Optional in requests, required in responses.
    :type raw_id: str
    :param communication_user: The communication user.
    :type communication_user: ~azure.communication.chat.models.CommunicationUserIdentifierModel
    :param phone_number: The phone number.
    :type phone_number: ~azure.communication.chat.models.PhoneNumberIdentifierModel
    :param microsoft_teams_user: The Microsoft Teams user.
    :type microsoft_teams_user: ~azure.communication.chat.models.MicrosoftTeamsUserIdentifierModel
    """

    _attribute_map = {
        'raw_id': {'key': 'rawId', 'type': 'str'},
        'communication_user': {'key': 'communicationUser', 'type': 'CommunicationUserIdentifierModel'},
        'phone_number': {'key': 'phoneNumber', 'type': 'PhoneNumberIdentifierModel'},
        'microsoft_teams_user': {'key': 'microsoftTeamsUser', 'type': 'MicrosoftTeamsUserIdentifierModel'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CommunicationIdentifierModel, self).__init__(**kwargs)
        self.raw_id = kwargs.get('raw_id', None)
        self.communication_user = kwargs.get('communication_user', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.microsoft_teams_user = kwargs.get('microsoft_teams_user', None)


class CommunicationUserIdentifierModel(msrest.serialization.Model):
    """A user that got created with an Azure Communication Services resource.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The Id of the communication user.
    :type id: str
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CommunicationUserIdentifierModel, self).__init__(**kwargs)
        self.id = kwargs['id']


class CreateChatThreadRequest(msrest.serialization.Model):
    """Request payload for creating a chat thread.

    All required parameters must be populated in order to send to Azure.

    :param topic: Required. The chat thread topic.
    :type topic: str
    :param participants: Participants to be added to the chat thread.
    :type participants: list[~azure.communication.chat.models.ChatParticipant]
    """

    _validation = {
        'topic': {'required': True},
    }

    _attribute_map = {
        'topic': {'key': 'topic', 'type': 'str'},
        'participants': {'key': 'participants', 'type': '[ChatParticipant]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CreateChatThreadRequest, self).__init__(**kwargs)
        self.topic = kwargs['topic']
        self.participants = kwargs.get('participants', None)


class CreateChatThreadResult(msrest.serialization.Model):
    """Result of the create chat thread operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param chat_thread: Chat thread.
    :type chat_thread: ~azure.communication.chat.models.ChatThreadProperties
    :ivar invalid_participants: The participants that failed to be added to the chat thread.
    :vartype invalid_participants: list[~azure.communication.chat.models.ChatError]
    """

    _validation = {
        'invalid_participants': {'readonly': True},
    }

    _attribute_map = {
        'chat_thread': {'key': 'chatThread', 'type': 'ChatThreadProperties'},
        'invalid_participants': {'key': 'invalidParticipants', 'type': '[ChatError]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CreateChatThreadResult, self).__init__(**kwargs)
        self.chat_thread = kwargs.get('chat_thread', None)
        self.invalid_participants = None


class MicrosoftTeamsUserIdentifierModel(msrest.serialization.Model):
    """A Microsoft Teams user.

    All required parameters must be populated in order to send to Azure.

    :param user_id: Required. The Id of the Microsoft Teams user. If not anonymous, this is the AAD
     object Id of the user.
    :type user_id: str
    :param is_anonymous: True if the Microsoft Teams user is anonymous. By default false if
     missing.
    :type is_anonymous: bool
    :param cloud: The cloud that the Microsoft Teams user belongs to. By default 'public' if
     missing. Possible values include: "public", "dod", "gcch".
    :type cloud: str or ~azure.communication.chat.models.CommunicationCloudEnvironmentModel
    """

    _validation = {
        'user_id': {'required': True},
    }

    _attribute_map = {
        'user_id': {'key': 'userId', 'type': 'str'},
        'is_anonymous': {'key': 'isAnonymous', 'type': 'bool'},
        'cloud': {'key': 'cloud', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftTeamsUserIdentifierModel, self).__init__(**kwargs)
        self.user_id = kwargs['user_id']
        self.is_anonymous = kwargs.get('is_anonymous', None)
        self.cloud = kwargs.get('cloud', None)


class PhoneNumberIdentifierModel(msrest.serialization.Model):
    """A phone number.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. The phone number in E.164 format.
    :type value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PhoneNumberIdentifierModel, self).__init__(**kwargs)
        self.value = kwargs['value']


class SendChatMessageRequest(msrest.serialization.Model):
    """Details of the message to send.

    All required parameters must be populated in order to send to Azure.

    :param content: Required. Chat message content.
    :type content: str
    :param sender_display_name: The display name of the chat message sender. This property is used
     to populate sender name for push notifications.
    :type sender_display_name: str
    :param type: The chat message type. Possible values include: "text", "html", "topicUpdated",
     "participantAdded", "participantRemoved".
    :type type: str or ~azure.communication.chat.models.ChatMessageType
    :param metadata: Message metadata.
    :type metadata: dict[str, str]
    """

    _validation = {
        'content': {'required': True},
    }

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'sender_display_name': {'key': 'senderDisplayName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SendChatMessageRequest, self).__init__(**kwargs)
        self.content = kwargs['content']
        self.sender_display_name = kwargs.get('sender_display_name', None)
        self.type = kwargs.get('type', None)
        self.metadata = kwargs.get('metadata', None)


class SendChatMessageResult(msrest.serialization.Model):
    """Result of the send message operation.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A server-generated message id.
    :type id: str
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SendChatMessageResult, self).__init__(**kwargs)
        self.id = kwargs['id']


class SendReadReceiptRequest(msrest.serialization.Model):
    """Request payload for sending a read receipt.

    All required parameters must be populated in order to send to Azure.

    :param chat_message_id: Required. Id of the latest chat message read by the user.
    :type chat_message_id: str
    """

    _validation = {
        'chat_message_id': {'required': True},
    }

    _attribute_map = {
        'chat_message_id': {'key': 'chatMessageId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SendReadReceiptRequest, self).__init__(**kwargs)
        self.chat_message_id = kwargs['chat_message_id']


class SendTypingNotificationRequest(msrest.serialization.Model):
    """Request payload for typing notifications.

    :param sender_display_name: The display name of the typing notification sender. This property
     is used to populate sender name for push notifications.
    :type sender_display_name: str
    """

    _attribute_map = {
        'sender_display_name': {'key': 'senderDisplayName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SendTypingNotificationRequest, self).__init__(**kwargs)
        self.sender_display_name = kwargs.get('sender_display_name', None)


class UpdateChatMessageRequest(msrest.serialization.Model):
    """Request payload for updating a chat message.

    :param content: Chat message content.
    :type content: str
    :param metadata: Message metadata.
    :type metadata: dict[str, str]
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UpdateChatMessageRequest, self).__init__(**kwargs)
        self.content = kwargs.get('content', None)
        self.metadata = kwargs.get('metadata', None)


class UpdateChatThreadRequest(msrest.serialization.Model):
    """Request payload for updating a chat thread.

    :param topic: Chat thread topic.
    :type topic: str
    """

    _attribute_map = {
        'topic': {'key': 'topic', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UpdateChatThreadRequest, self).__init__(**kwargs)
        self.topic = kwargs.get('topic', None)