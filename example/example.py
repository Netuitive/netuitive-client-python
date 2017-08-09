import netuitive
import time
import os

ApiClient = netuitive.Client(url=os.environ.get('API_URL'), api_key=os.environ.get('CUSTOM_API_KEY'))

MyElement = netuitive.Element()

MyElement.add_attribute('Language', 'Python')
MyElement.add_attribute('app_version', '7.0')

MyElement.add_relation('my_child_element')

MyElement.add_tag('Production', 'True')
MyElement.add_tag('app_tier', 'True')

timestamp = int(time.mktime(time.localtime()))
MyElement.add_sample('app.error', timestamp, 1, host='appserver01')
MyElement.add_sample('app.request', timestamp, 10, host='appserver01')

ApiClient.post(MyElement)

MyElement.clear_samples()

MyEvent = netuitive.Event('appserver01', 'INFO', 'test event','this is a test message', 'INFO')

ApiClient.post_event(MyEvent)

if ApiClient.time_insync():
    print('we have time sync with the server')
