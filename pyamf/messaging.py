# -*- encoding: utf8 -*-
#
# Copyright (c) 2007 The PyAMF Project. All rights reserved.
# 
# Arnar Birgisson
# Thijs Triemstra
# Nick Joyce
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Flex Messaging Implementation.

@see: U{http://osflash.org/documentation/amf3#remoteobject}

@author: U{Arnar Birgisson<mailto:arnarbi@gmail.com>}
@author: U{Thijs Triemstra<mailto:info@collab.nl>}
@author: U{Nick Joyce<mailto:nick@boxdesign.co.uk>}

@since: 0.1.0
"""

import pyamf

class AbstractMessage(object):
    """
    Abstract base class for all Flex messages. Messages have two customizable sections;
    headers and data. The headers property provides access to specialized meta information
    for a specific message instance. The data property contains the instance specific data
    that needs to be delivered and processed by the decoder.
    """
    #: Specific data that needs to be delivered to the remote destination.
    data = None
    #: The clientId indicates which client sent the message. 
    clientId = None
    #: The message destination.
    destination = None
    #: Message headers
    headers = []
    #: Unique message ID
    messageId = None
    #: Indicates how long the message should be considered valid and deliverable.
    timeToLive = None
    #: Time stamp for the message.
    timestamp = None
    
    def __repr__(self):
        m = '<%s ' % self.__class__.__name__

        for k, v in self.__dict__.iteritems():
            m += ' %s=%s' % (k, v)

        return m + " />"

class AsyncMessage(AbstractMessage):
    """
    Base class for all asynchronous Flex messages.
    """
    #: Correlation id of the message.
    correlationId = None

class AcknowledgeMessage(AsyncMessage):
    """
    Acknowledges the receipt of a message that was sent previously. Every message sent
    within the messaging system must receive an acknowledgement.
    """
    pass

class CommandMessage(AsyncMessage):
    """
    Provides a mechanism for sending commands related to publish/subscribe messaging,
    ping, and cluster operations.

    @see: U{http://livedocs.adobe.com/flex/201/langref/mx/messaging/messages/CommandMessage.html}
    """
    #: Operation/command.
    operation = None
    #: Remote destination belonging to a specific service, based upon whether this
    #: message type matches the message type the service handles.
    messageRefType = None

class ErrorMessage(AbstractMessage):
    """
    Flex error message to be returned to the client.
    """
    #: Extended data that the remote destination has chosen to associate with 
    #: this error to facilitate custom error processing on the client. 
    extendedData = {}
    #: Fault code for the error. 
    faultCode = None
    #: Detailed description of what caused the error. 
    faultDetail = None
    #: A simple description of the error. 
    faultString = None
    #: Should a traceback exist for the error, this property contains the
    #: message.
    rootCause = {}

class RemotingMessage(AbstractMessage):
    """
    Used to send RPC requests to a remote endpoint.

    @see: {http://livedocs.adobe.com/flex/201/langref/mx/messaging/messages/RemotingMessage.html}
    """
    #: Name of the remote method/operation that should be called.
    operation = None
    #: Name of the service to be called
    #: including package name.
    #: This property is provided for backwards compatibility.
    source = None

pyamf.register_class(RemotingMessage, 'flex.messaging.messages.RemotingMessage')
pyamf.register_class(ErrorMessage, 'flex.messaging.messages.ErrorMessage')
pyamf.register_class(CommandMessage, 'flex.messaging.messages.CommandMessage')
pyamf.register_class(AcknowledgeMessage, 'flex.messaging.messages.AcknowledgeMessage')