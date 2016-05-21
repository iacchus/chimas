from sqlalchemy import func

boards_schema = {
    'datasource': {
        'projection': {
            'created': 1,
            'deleted': 1,
            'description': 1,
            'etag': 1,
            'id': 1,
            'title': 1,
            'updated': 1
        },
        'source': 'Boards'
    },
    'item_lookup': True,
    'item_lookup_field': 'id',
    'item_url': 'regex("[0-9]+")',
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
        'description': {
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
            'required': False,
            'type': 'integer',
            'unique': True
        },
        'title': {
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
    } # 'schema key'
} # dict
