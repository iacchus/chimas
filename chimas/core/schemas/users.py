from sqlalchemy import func

users_schema = {
    'datasource': {

        'projection': {
            'created': 1,
            'deleted': 1,
            'email': 1,
            'etag': 1,
            'id': 1,
            'login': 1,
            'password': 1,
            'updated': 1
        },

        'source': 'Users'
    },

    'item_lookup': True,
    'item_lookup_field': 'id',
    'item_methods': ['GET', 'DELETE'],
    'item_url': 'regex("[0-9]+")',
    'resource_methods': ['GET', 'POST'],
    'schema': {
        'created': {
            'default': func.now,
            'nullable': True,
            'required': False,
            'type': 'datetime',
            'unique': False
        },
        'deleted': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'email': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'etag': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'id': {
            'nullable': True,
            'required': False,
            'type': 'integer',
            'unique': True
        },
        'login': {
            'required': False,
            'type': 'string',
            'unique': True
        },
        'password': {
            'nullable': True,
            'required': False,
            'type': 'string',
            'unique': False
        },
        'updated': {
            'default': func.now,
            'nullable': True,
            'required': False,
            'type': 'datetime',
            'unique': False
        }
    } # END OF 'schema'
} # END OF 'users_schema' dict
