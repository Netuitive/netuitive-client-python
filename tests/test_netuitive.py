#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_netuitive
----------------------------------

Tests for `netuitive` module.
"""

import unittest
import json
import time
import netuitive


class TestClientInit(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):

        # test custom endpoint url creation
        a = netuitive.Client('https://example.com/ingest', 'apikey')
        self.assertEqual(a.url, 'https://example.com/ingest')
        self.assertEqual(a.api_key, 'apikey')
        self.assertEqual(a.dataurl, 'https://example.com/ingest/apikey')
        self.assertEqual(
            a.eventurl, 'https://example.com/ingest/events/apikey')

        # test infrastructure endpoint url creation
        a = netuitive.Client(
            'https://example.com/ingest/infrastructure', 'apikey')
        self.assertEqual(a.url, 'https://example.com/ingest/infrastructure')
        self.assertEqual(a.api_key, 'apikey')
        self.assertEqual(
            a.dataurl, 'https://example.com/ingest/infrastructure/apikey')
        self.assertEqual(
            a.eventurl, 'https://example.com/ingest/events/infrastructure/apikey')

        # test negation of trailing / on the url
        a = netuitive.Client('https://example.com/ingest/', 'apikey')
        self.assertEqual(a.url, 'https://example.com/ingest')
        self.assertEqual(a.api_key, 'apikey')
        self.assertEqual(a.dataurl, 'https://example.com/ingest/apikey')
        self.assertEqual(
            a.eventurl, 'https://example.com/ingest/events/apikey')

    def tearDown(self):
        pass


class TestElementInit(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        a = netuitive.Element()
        b = netuitive.Element('NOT_SERVER')

        self.assertEqual(a.type, 'SERVER')
        self.assertEqual(b.type, 'NOT_SERVER')

    def tearDown(self):
        pass


class TestElementAttributes(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        a = netuitive.Element()
        a.add_attribute('Test', 'TestValue')
        self.assertEqual(a.attributes[0].name, 'Test')
        self.assertEqual(a.attributes[0].value, 'TestValue')

    def tearDown(self):
        pass


class TestElementTags(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        a = netuitive.Element()
        a.add_tag('Test', 'TestValue')

        self.assertEqual(a.tags[0].name, 'Test')
        self.assertEqual(a.tags[0].value, 'TestValue')

    def tearDown(self):
        pass


class TestElementSamples(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        a = netuitive.Element()
        a.add_sample(
            'metricId', 1434110794, 1, 'COUNTER', host='hostname')

        self.assertEqual(a.id, 'hostname')
        self.assertEqual(a.name, 'hostname')

        self.assertEqual(a.metrics[0].id, 'metricId')
        self.assertEqual(a.metrics[0].type, 'COUNTER')

        a.add_sample(
            'metricId', 1434110794, 1, 'COUNTER', host='hostname')

        # don't allow duplicate metrics
        self.assertEqual(len(a.metrics), 1)

        self.assertEqual(a.samples[0].metricId, 'metricId')
        self.assertEqual(a.samples[0].timestamp, 1434110794000)
        self.assertEqual(a.samples[0].val, 1)

        # test clear_samples
        self.assertEqual(len(a.metrics), 1)
        a.clear_samples()
        self.assertEqual(len(a.metrics), 0)
        self.assertEqual(len(a.samples), 0)

        # test sparseDataStrategy
        a.add_sample(
            'nonsparseDataStrategy', 1434110794, 1, 'COUNTER', host='hostname')
        a.add_sample(
            'sparseDataStrategy', 1434110794, 1, 'COUNTER', host='hostname', sparseDataStrategy='ReplaceWithZero')

        self.assertEqual(a.metrics[0].sparseDataStrategy, 'None')
        self.assertEqual(
            a.metrics[1].sparseDataStrategy, 'ReplaceWithZero')

        a.clear_samples()

        # test unit
        a.add_sample(
            'unit', 1434110794, 1, 'COUNTER', host='hostname', unit='Bytes')

        a.add_sample(
            'nonunit', 1434110794, 1, 'COUNTER', host='hostname')

        self.assertEqual(
            a.metrics[0].unit, 'Bytes')

        self.assertEqual(a.metrics[1].unit, '')

        # test post format for element

        ajson = json.dumps([a], default=lambda o: o.__dict__, sort_keys=True)
        j = '[{"attributes": [], "id": "hostname", "metrics": [{"id": "unit", "sparseDataStrategy": "None", "type": "COUNTER", "unit": "Bytes"}, {"id": "nonunit", "sparseDataStrategy": "None", "type": "COUNTER", "unit": ""}], "name": "hostname", "samples": [{"metricId": "unit", "timestamp": 1434110794000, "val": 1}, {"metricId": "nonunit", "timestamp": 1434110794000, "val": 1}], "tags": [], "type": "SERVER"}]'

        self.assertEqual(ajson, j)

    def tearDown(self):
        pass


class TestEvent(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        everything = netuitive.Event('elementId', 'INFO', 'title', 'message', 'INFO',
                                     [('name0', 'value0'), ('name1', 'value1')], 1434110794, 'source')

        notags = netuitive.Event(
            'elementId', 'INFO', 'title', 'message', 'INFO', timestamp=1434110794, source='source')

        minimum = netuitive.Event(
            'elementId', 'INFO', 'title', 'message', 'INFO')

        everythingjson = json.dumps(
            [everything], default=lambda o: o.__dict__, sort_keys=True)

        notagsjson = json.dumps(
            [notags], default=lambda o: o.__dict__, sort_keys=True)

        minimumjson = json.dumps(
            [minimum], default=lambda o: o.__dict__, sort_keys=True)

        # test event with all options

        self.assertEqual(everything.eventType, 'INFO')
        self.assertEqual(everything.title, 'title')
        self.assertEqual(everything.timestamp, 1434110794000)
        self.assertEqual(everything.tags[0].name, 'name0')
        self.assertEqual(everything.tags[0].value, 'value0')
        self.assertEqual(everything.tags[1].name, 'name1')
        self.assertEqual(everything.tags[1].value, 'value1')

        data = everything.data
        self.assertEqual(data.elementId, 'elementId')
        self.assertEqual(data.level, 'INFO')
        self.assertEqual(data.message, 'message')

        # test event without tags

        self.assertEqual(notags.eventType, 'INFO')
        self.assertEqual(notags.title, 'title')
        self.assertEqual(notags.timestamp, 1434110794000)
        self.assertEqual(hasattr(notags, 'tags'), False)

        data = notags.data
        self.assertEqual(data.elementId, 'elementId')
        self.assertEqual(data.level, 'INFO')
        self.assertEqual(data.message, 'message')

        # test event with minimum options

        shouldbetrue = False
        t = int(time.time()) * 1000

        # minimum.timstamp has to be within the 10 second
        if t - 10000 < int(minimum.timestamp):
            shouldbetrue = True

        self.assertTrue(shouldbetrue)
        self.assertEqual(minimum.title, 'title')
        self.assertEqual(minimum.eventType, 'INFO')

        data = minimum.data
        self.assertEqual(data.elementId, 'elementId')
        self.assertEqual(data.level, 'INFO')
        self.assertEqual(data.message, 'message')

        # test post format for event with all options

        j = '[{"data": {"elementId": "elementId", "level": "INFO", "message": "message"}, "eventType": "INFO", "source": "source", "tags": [{"name": "name0", "value": "value0"}, {"name": "name1", "value": "value1"}], "timestamp": 1434110794000, "title": "title"}]'

        self.assertEqual(everythingjson, j)

        # test post format for event without tags

        j = '[{"data": {"elementId": "elementId", "level": "INFO", "message": "message"}, "eventType": "INFO", "source": "source", "timestamp": 1434110794000, "title": "title"}]'

        self.assertEqual(notagsjson, j)

        # test post format for event with minimum options

        j = '[{"data": {"elementId": "elementId", "level": "INFO", "message": "message"}, "eventType": "INFO", "timestamp": ' + \
            str(minimum.timestamp) + ', "title": "title"}]'

        self.assertEqual(minimumjson, j)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
