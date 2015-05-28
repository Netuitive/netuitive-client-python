========
Usage
========

To use Netuitive Python Client in a project::

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

