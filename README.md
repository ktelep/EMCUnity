EMCUnity
=======================

EMCUnity provides a Python interface to the EMC Unity RESTful API

## Description

This module has been developed to provide a pythonic interface for interacting with EMC's Unity line of mid-range storage arrays.  This module supports both Physical arrays (such as the 300/400/500/600 hybrid and all flash models) along with the UnityVSA.  

Although this module provides a layer of abstraction between the REST API and the developer, it is recommended that you review the following documents as a reference, particularly when referencing object names, fields that are available, and the use of filters when querying the array.

[Unity Family Unisphere Management REST API Reference Guide](https://support.emc.com/docu69899_Unity_Family_Unisphere_Management_REST_API_Reference_Guide.zip?language=en_US)

[Unity Family Unisphere Management REST API Programmers' Guide](https://support.emc.com/docu69331_Unity-Family-Unisphere-Management-REST-API-Programmer's-Guide.pdf?language=en_US)

As of today the module is fully functional for retrieving information from the array along with performing manual POST and DELETE requests.   Work is continuing to create helper functions to simplify common tasks.

## Installation

*Prerequisites*

1.  Python 2.7 (Python 3 support is coming)
2.  Requests module

## Sample usage

Creating a LUN

    # Connect to the array
    unity = Unity('unity.ktelep.local','admin','TooManySecrets')

    # Gather a list of pools, we need the pool ID for LUN creation
    pools = unity.pool()
    first_pool = pools[0].id

    # Create a lun with a new Unitylun object
    new_lun = Unitylun(name="TestLUN",pool=first_pool,sizeTotal=50000000,
                 description="Test Description")

    # Pass it to create_lun
    response = unity.create_lun_from_obj(new_lun)
    print response

    # Create a new lun with parameters
    response = unity.create_lun("TestLUN2", first_pool, 50000000, "Test Desc")
    print response


Any object defined in the API Reference Guide is accessible as a function, for example gathering license keys shown below.  This pattern is available for any referenced object.


    # Connect to the array
    unity = Unity('unity.ktelep.local','admin','TooManySecrets')

    unity.license()   # Returns all licenses as Unitylicense objects
    unity.license(item_id='QUALITY_OF_SERVICE')  # Returns the QOS License
    unity.license(item_filter='id LK "UNISPHERE%"') # Returns Licenses starting with "UNISPHERE"
    unity.license(item_name='FAST_VP') # Returns license named FAST_VP


You can also make direct calls (GET,POST,DELETE) to the REST API

    # Request for DAE instances, returns response object  
    response = unity.get('/types/dae/instances')
    json_data = response.json()

    # Create a LUN manually (Size is in bytes)
    payload = {'name': "NewLUN"
               'lunParameters':{'pool':{'id':'pool_1'},
                                        'size': 50000000}}

    response = self.post('/types/storageResource/action/createLun',payload)

    new_id = response.json()['content']['storageResource']['id']

    # Delete a LUN manually
    response = self.delete('/instances/storageResource/%s' % new_id)  


Licensing
---------
This software is provided under the MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Status API Training Shop Blog About Pricing


Support
-------
Please file bugs and issues at the Github issues page.
