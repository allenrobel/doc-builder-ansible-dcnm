# dcnm_image_upload

???+ "Details"

    - short_description
        - DCNM Ansible Module for managing images.
    - version_added
        - 3.5.0
    - description
        - DCNM Ansible Module for the following image management operations Upload, Delete, and Display NXOS images from the controller
    - author
        - Mallik Mudigonda(@mmudigon)


## options

???+ "Details"


### state

???+ "Details"

    - description
        - The required state of the configuration after module completion.
    - type
        - str
    - choices
        - merged
        - overridden
        - deleted
        - query
    - default
        - merged

### files

???+ "Details"

    - description
        - A dictionary of images and other related information that is required to download the same.
    - type
        - list
    - elements
        - dict
    - default
        - []

#### path

???+ "Details"

    - description
        - Full path to the image that is being uploaded to the controller. For deleting an image the exact image name must be provided.
    - type
        - str
    - required
        - True

#### source

???+ "Details"

    - description
        - Protocol to be used to download the image from the controller.
    - type
        - str
    - choices
        - scp
        - sftp
        - local
    - default
        - local

#### remote_server

???+ "Details"

    - description
        - IP address of the server hosting the image. This parameter is required only if source is 'scp' or 'sftp'.
    - type
        - str
    - required
        - True

#### user_name

???+ "Details"

    - description
        - User name to be used to log into the image hosting server. This parameter is required only if source is 'scp' or 'sftp'.
    - type
        - str
    - required
        - True

#### password

???+ "Details"

    - description
        - Password to be used to log into the image hosting server. This parameter is required only if source is 'scp' or 'sftp'.
    - type
        - str
    - required
        - True
