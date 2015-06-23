===============================
Netuitive Python Client
===============================

Features
--------

* Create a Netuitive Element with the following data:
    * Element Name
    * Attributes
    * Tags
    * Metric Samples


Usage
-----

* Setup the Client
    ``ApiClient = netuitive.Client(api_key='<my_api_key>')``


* Setup the Element
    ``MyElement = netuitive.Element()``

* Add an Attribute
    ``MyElement.add_attribute('Language', 'Python')``

* Add a Tag
    ``MyElement.add_tag(('Production', 'True')``

* Add a Metric Sample
    ``MyElement.add_sample('cpu.idle', 1432832135, 1, host='my_hostname')``

* Add a Metric Sample with a Sparse Data Strategy
    ``MyElement.add_sample('app.zero', 1432832135, 1, host='my_hostname', sparseDataStrategy='ReplaceWithZero')``

* Add a Metric Sample with unit type
    ``MyElement.add_sample('app.requests', 1432832135, 1, host='my_hostname', unit='requests/s')``


* Send the Samples
    ``ApiClient.post(MyElement)``

* Remove the samples already sent
    ``MyElement.clear_samples()``

Example
-------
::

    import netuitive

    ApiClient = netuitive.Client(apikey='aaaa9956110211e594444697f922ec7b')

    MyElement = netuitive.Element()

    MyElement.add_attribute('Language', 'Python')
    MyElement.add_attribute('app_version', '7.0')

    MyElement.add_tag(('Production', 'True')
    MyElement.add_tag(('app_tier', 'True')

    MyElement.add_sample('app.error', 1432832135, 1, host='appserver01')
    MyElement.add_sample('app.request', 1432832135, 10, host='appserver01')

    ApiClient.post(MyElement)

    MyElement.clear_samples()


Copyright and License
---------------------

Copyright 2015 Netuitive, Inc. under [the Apache 2.0 license](LICENSE).
