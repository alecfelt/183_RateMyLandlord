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
db.define_table('product',
    Field('product_name'),
    Field('quantity', 'integer'),
    Field('price', 'float'),
    Field('image', 'upload'),
    Field('description', 'text'),
)
db.product.id.readable = db.product.id.writable = False

db.define_table('customer_order',
    Field('order_date', default=datetime.datetime.utcnow()),
    Field('customer_info', 'blob'),
    Field('transaction_token', 'blob'),
    Field('cart', 'blob'),
)

# Let's define a secret key for stripe transactions.
from gluon.utils import web2py_uuid
if session.hmac_key is None:
    session.hmac_key = web2py_uuid()


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

# from hw implementation
db.define_table('images',
                Field('created_on', 'datetime', default=request.now),
                Field('created_by', 'reference auth_user', default=auth.user_id),
                Field('image_url'),
                Field('image_price','float'),
                # Field('is_checked', 'boolean', default=False),
)

