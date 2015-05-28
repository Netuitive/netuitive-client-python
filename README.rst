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


## Usage

```
    import netuitive

    # Setup the Client
    ApiClient = netuitive.Client('<my_api_url>', '<my_api_key>')

    # setup the Element
    MyElement = netuitive.Element()

    # Add an Attribute
    MyElement.add_attribute('Language', 'Python')

    # Add a Tag
    MyElement.add_tag(('Production', 'True')

    # Add a Metric Sample
    MyElement.add_sample('cpu.idle', 1432832135, 1, host='my_hostname')

    # Send the Samples
    ApiClient.post(MyElement)

    # Remove the samples already sent
    MyElement.clear_samples()
```

## Copyright and License

Copyright 2015 Netuitive, Inc. under [the Apache 2.0 license](LICENSE).
