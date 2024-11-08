# dcnm_rest

???+ "Details"

    - short_description
        - Send REST API requests to DCNM controller.
    - version_added
        - 0.9.0
    - description
        - "Send REST API requests to DCNM controller."
    - author
        - Mike Wiebe (@mikewiebe)


## options

???+ "Details"


### method

???+ "Details"

    - description
        - 'REST API Method'
    - required
        - True
    - type
        - str
    - choices
        - GET
        - POST
        - PUT
        - DELETE

### path

???+ "Details"

    - description
        - 'REST API Path Endpoint'
    - required
        - True
    - type
        - str

### data

???+ "Details"

    - description
        - 'Additional data in JSON or TEXT to include with the REST API call'
    - aliases
        - json_data
    - required
        - False
    - type
        - raw
