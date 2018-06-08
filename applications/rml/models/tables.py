# from hw implementation
db.define_table('images',
                Field('created_on', 'datetime', default=request.now),
                Field('created_by', 'reference auth_user', default=auth.user_id),
                Field('image_url'),
                Field('image_price','float'),
                # Field('is_checked', 'boolean', default=False),
)


