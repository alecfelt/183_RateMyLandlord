# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime


# Product table.
# from cart
db.define_table('landlords',
    Field('first_name', type='string'),
    Field('last_name', type='string'),
    Field('average_l_rating', type='double'),
    Field('average_p_rating', type='double'),
    Field('property_ids', type='list:integer'),
    Field('review_ids', type='list:integer'),
    Field('tag_ids', type='list:integer'),
    Field('updated_on', 'datetime', update=request.now, redefine=True)
)

db.define_table('properties',
    Field('address', type='string'),
    Field('landlord_ids', type='list:integer'),
    Field('tag_ids', type='list:integer'),
    Field('updated_on', 'datetime', update=request.now, redefine=True)
)

db.define_table('reviews',
    Field('landlord_id', type='integer'),
    Field('property_id', type='integer'),
    Field('landlord_rating', type='integer'),
    Field('property_rating', type='integer'),
    Field('rent_with_landlord_again', type='boolean'),
    Field('rent_with_property_again', type='boolean'),
    Field('landlord_tag_ids', type='list:integer'),
    Field('property_tag_ids', type='list:integer'),
    Field('comments', type='text'),
    Field('updated_on', 'datetime', update=request.now, redefine=True)
)

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

import json

def nicefy(b):
    if b is None:
        return 'None'
    obj = json.loads(b)
    s = json.dumps(obj, indent=2)
    return s

def get_user_email():
    return auth.user.email if auth.user else None
