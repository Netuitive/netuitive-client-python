import time
from .tag import Tag


class Event(object):

    """An Event

    Args:
        elementId (string): <element FQN>
        eventType (string): type of the event
        title (string): title of the event
        message (string): the event message
        level (string): one of [INFO, WARNING, CRITICAL]
        tags (list of lists):  tags for this event
        timestamp (epoch) : The timestamp of the event
        source (string): the source of the event
    """

    def __init__(self, elementId, eventType, title, message, level, tags=None, timestamp=None, source=None):

        self.eventType = eventType.upper()
        self.title = title

        if source is not None:
            self.source = source

        if tags is not None:
            self.tags = []
            for t in tags:
                self.tags.append(Tag(t[0], t[1]))

        if timestamp is None:
            self.timestamp = int(time.time()) * 1000
        else:
            self.timestamp = timestamp * 1000

        if self.eventType == 'INFO' and message is not None and level is not None:
            self.data = EventType(elementId, 'INFO', message, level)


class EventType(object):

    """An Event

    Args:
        eventType (string): type of the event
        elementId (string): <element FQN>
        level (string): one of [INFO, WARNING, CRITICAL]
        message (string): the message
    """

    def __init__(self, elementId, eventType, message=None, level=None):
        self.elementId = elementId

        if eventType.upper() == 'INFO' and message is not None and level is not None:
            self.level = level
            self.message = message
