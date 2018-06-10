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
#         data = [{name: "", }, {}, {}]
def search_landlords():
    return response.json(dict(
        msg='search_landlords'
    ))


# input: search_str
# output: list of property obj
#         data = [{address: "", }, {}, {}]
def search_properties():
    return response.json(dict(
        msg='search_properties'
    ))

# input: list of landlord ids
# output: list of landlord objs
#         data = [{name: "", }, {}, {}]
def get_landlords():
    return response.json(dict(
        msg='get_landlords'
    ))

# input: name, website, address
# output: name, website, address
def add_landlord():
    return response.json(dict(
        msg='add_landlord'
    ))

# input: list of property ids
# output: list of property obj
#         data = [{address: "", }, {}, {}]
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
#         data = [{landlord_id: "", }, {}, {}]
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
