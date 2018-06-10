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

# Goes through table landlords and returns a list of landlord objects with name that contains the substring passed in
# input: search_str
# output: list of landlord obj
#         data = { landlords: [{name: "", }, {}, {}] }
def search_landlords():
    # if request.vars.search_str:
    #     name = request.vars.search_str
    # else:
    #     name = ""

    name = request.vars.search_str if request.vars.search_str else ''

    landlords = []

    for row in db().select(orderby=db.landlords.name):
        if name in row.name:
            landlord = dict(
                id=row.id,
                name=row.name,
                property_ids=row.property_ids,
                review_ids=row.review_ids,
                tag_ids=row.tag_ids
            )
        landlords.append(landlord)

    return response.json(dict(
        landlords=landlords
    ))

# input: search_str
# output: list of property obj
#         data = { properties: [{id: 1, address: "", landlord_ids: []}, {}, {}] }
def search_properties():
    # if request.vars.search_str:
    #     address = request.vars.search_str
    # else:
    #     address = ""

    address = request.vars.search_str if request.vars.search_str else ''
    properties = []

    for row in db().select(db.properties.id, db.properties.address, db.properties.landlord_ids, db.properties.tag_ids, orderby=db.properties.address):
        if address in row.address:
            propertie = dict(
                id=row.id,
                address=row.address,
                landlord_ids=row.landlord_ids,
                tag_ids=row.tag_ids
            )
        properties.append(propertie)

    return response.json(dict(
        properties=properties
    ))

# input: list of landlord ids
# output: list of landlord objs
#         data = { landlords: [{name: "", }, {}, {}] }
def get_landlords():
    # if request.vars.landlord_ids:
    #     landlord_ids = request.vars.landlord_ids;
    # else:
    #     landlord_ids = []

    landlord_ids = request.vars.landlord_ids if request.vars.landlord_ids else []

    landlords = []

    for row in db().select(orderby=db.landlords.name):
        if row.id in landlord_ids:
            landlord = dict(
                id=row.id,
                name=row.name,
                property_ids=row.property_ids,
                review_ids=row.review_ids,
                tag_ids=row.tag_ids
            )
        landlords.append(landlord)

    return response.json(dict(
        landlords=landlords
    ))

# Strip leading and trailing whitespaces and capitalize the address
def format_address_elem(address_elem, isState=False):
    address_elem = address_elem.strip().upper()

    return address_elem

# Takes an address dictionary and returns a formatted string
def format_address(address):
    city = format_address_elem( address["city"] )
    state = format_address_elem( address["state"] )
    zipcode = format_address_elem( address["zipcode"] )

    street = ""
    for e in address["street"].split():
        street = street + " " + format_address_elem(e)
    street = street.strip()

    full_address = street + ", " + city + ', ' + state + ' ' + zipcode

    return full_address


# Add a landlord into table landlords
# input: name, website, address, where address = {street: "", city: "", state: "", zipcode: ""}
# output: data = {name: "name", website: "website url", address: "address", property_id: 1}
def add_landlord():
    # Return an error if landlord name is null
    if request.vars.name:
        name = request.vars.name
    else:
        print "[Error] add_landlord(): landlord name cannot be null"
        raise HTTP(500)
        # name = "John Cena"

    if request.vars.address:
        address = format_address(request.vars.address)
    else:
        print "[Error] add_landlord(): property address cannot be null"
        raise HTTP(500)
        # addy = {'street': "417 high steet", 'city': " santa  cruz", 'state': 'CA ', 'zipcode': ' 95060'}
        # address = format_address(addy)


    website = request.vars.website

    # Check if property already exists
    # If exists, get the property id
    # Otherwise insert to db and get property id
    q = (db.properties.address == address)
    r = db(q).select(db.properties.id).first()
    if r:
        # print "property found"
        property_id = r.id
    else:
        property_id = db.properties.insert(
            address = address
        )
        # print "property_id: ", property_id

    # Insert landlord landlords
    landlord_id = db.landlords.insert(
        name = name,
        property_id = property_id
    )
    # print "landlord id: ", landlord_id

    # Insert/append landlord_id into table properties for the property
    q = (db.properties.id == property_id)
    r = db(q).select().first()
    if r.landlord_ids:
        landlord_ids = set(r.landlord_ids)
        landlord_ids.add(landlord_id)
        landlord_ids = list(landlord_ids)
    else:
        landlord_ids = [landlord_id]

    r.update_record(landlord_ids=landlord_ids)

    # Returns the landlord info.
    return response.json(dict(
        id = landlord_id,
        address = address,
        website = website,
        property_id = property_id
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
