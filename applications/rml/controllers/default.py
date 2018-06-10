# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

import datetime

# ---- example index page ----
def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki()

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

### Our endpoints ###
#####################
### Our endpoints ###
#####################
### Our endpoints ###
#####################
### Our endpoints ###


# input: search_str
# output: list of landlord obj
#         data = { landlords: [{name: "", }, {}, {}] }
def search_landlords():
    if request.vars.search_str:
        name = request.vars.search_str
    else:
        name = ""

    landlords = []

    for row in db().select(db.landlords.id, db.landlords.name, orderby=db.landlords.name):
        if name in row.name:
            landlord = dict(
                id=row.id,
                name=row.name
            )
        landlords.append(landlord)

    return response.json(dict(
        landlords=landlords
    ))

# input: search_str
# output: list of property obj
#         data = { properties: [{id: 1, address: "", landlord_ids: []}, {}, {}] }
def search_properties():
    if request.vars.search_str:
        address = request.vars.search_str
    else:
        address = ""

    properties = []

    for row in db().select(db.properties.id, db.properties.address, db.properties.landlord_ids, orderby=db.properties.address):
        if address in row.address:
            propertie = dict(
                id=row.id,
                address=row.address,
                landlord_ids=row.landlord_ids
            )
        properties.append(propertie)

    return response.json(dict(
        properties=properties
    ))

# input: list of landlord ids
# output: list of landlord objs
#         data = { landlords: [{name: "", }, {}, {}] }
def get_landlords():
    if request.vars.landlord_ids:
        landlord_ids = request.vars.landlord_ids;
    else:
        landlord_ids = []

    landlords = []

    for row in db().select(db.landlords.id, db.landlords.name, orderby=db.landlords.name):
        if row.id in landlord_ids:
            landlord = dict(
                id=row.id,
                name=row.name
            )
        landlords.append(landlord)

    return response.json(dict(
        landlords=landlords
    ))

# input: name, website, address
# output: data = {name: "name", website: "website url", address: "address"}
def add_landlord():
    return response.json(dict(
        msg='add_landlord'
    ))

# input: list of property ids
# output: list of property obj
#         data = { properties: [{address: "", }, {}, {}] }
def get_properties():
    return response.json(dict(
        msg='get_properties'
    ))

# private method, not an actual route
def add_property():
    return response.json(dict(
        msg='add_property'
    ))

# input: landlord_id
# output: list of review objs
#         data = { reviews: [{landlord_id: "", }, {}, {}] }
def get_reviews():
    return response.json(dict(
        msg='get_reviews'
    ))

# input: landlord_id, address,
# landlord_rating
# property_rating
# rent_with_landlord_again
# rent_with_property_again
# landlord_tag_ids
# property_tag_ids
# comments
# output: "ok"
def add_review():
    return response.json(dict(
        msg='add_review'
    ))
