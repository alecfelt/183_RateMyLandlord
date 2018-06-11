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

# Boolean function that determines whether name in search string
# matches with first, last name stored in the database
def match_names(search_name, first_name, last_name):
    search_name = search_name.strip().lower()
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    if (search_name in first_name) or (search_name in last_name) or (first_name in search_name) or (last_name in search_name):
        return True
    else:
        return False

    # ---- Use matching percentage but doesn't work as well  ---- #

    # matched_chars = set(name1).intersection(name2)
    # # num_matched_chars = len(set(name1).intersection(name2))
    # num_matched_chars = len(matched_chars)
    # # matching_percent = (matched_chars * 1.0) / len(name1)
    # matching_percent = (num_matched_chars * 1.0) / len(name1)
    #
    # print 'matched_chars: ', matched_chars
    # print 'matching_percent: ', matching_percent
    #
    # if matching_percent == 1:
    #     return True
    # else:
    #     return False
    # return True if

# Goes through table landlords and returns a list of landlord objects with name that contains the substring passed in
# input: search_str
# output: list of landlord obj
#         data = { landlords: [{name: "", }, {}, {}] }
def search_landlords():
    # if request.vars.search_str:
    #     name = request.vars.search_str
    # else:
    #     name = ""

    search_name = request.vars.search_str if request.vars.search_str else ''

    print("searching for " + search_name)

    landlords = []

    for row in db(db.landlords.first_name).select(orderby=db.landlords.last_name):
        if match_names(search_name, row.first_name, row.last_name):
            temp_landlord = dict(
                id=row.id,
                first_name=row.first_name,
                last_name=row.last_name,
                property_ids=row.property_ids,
                review_ids=row.review_ids,
                tag_ids=row.tag_ids
            )
            landlords.append(temp_landlord)

    return response.json(dict(
        landlords=landlords
    ))

    # Old way. Change it back it anyone prefers this one
    # str = request.vars.search_str if request.vars.search_str else ''
    # print("searching for " + str)

    # for row in db(db.landlords.first_name).select(orderby=db.landlords.last_name):
    # for row in db().select(orderby=db.landlords.last_name):
    #     if str.lower() in row.first_name.lower():
    #         temp_landlord = dict(
    #             id=row.id,
    #             first_name=row.first_name,
    #             last_name=row.last_name,
    #             property_ids=row.property_ids,
    #             review_ids=row.review_ids,
    #             tag_ids=row.tag_ids
    #         )
    #         landlords.append(temp_landlord)
    #         continue
    #     if str.lower() in row.last_name.lower():
    #         temp_landlord = dict(
    #             id=row.id,
    #             first_name=row.first_name,
    #             last_name=row.last_name,
    #             property_ids=row.property_ids,
    #             review_ids=row.review_ids,
    #             tag_ids=row.tag_ids
    #         )
    #         landlords.append(temp_landlord)
    #
    # return response.json(dict(
    #     landlords=landlords
    # ))


# Boolean function that determines whether address in search string
# matches with some address stored in the database
def match_address(search_address, db_address):
    search_address = search_address.strip().upper()
    # print 'search_address: ', search_address
    # print 'db_address: ', db_address
    if search_address in db_address:
        # print 'search_address in db_address'
        return True
    else:
        # print 'search_address not in db_address'
        return False

# Goes through table properties and returns a list of property objects with address that contains the substring passed in
# input: search_str
# output: list of property obj
#         data = { properties: [{id: 1, address: "", landlord_ids: []}, {}, {}] }
def search_properties():
    address = request.vars.search_str if request.vars.search_str else ''
    properties = []

    for row in db().select(db.properties.id, db.properties.address, db.properties.landlord_ids, db.properties.tag_ids, orderby=db.properties.address):
        # if address in row.address:
        if match_address(address, row.address):
            propertie = dict(
                id=row.id,
                address=row.address,
                landlord_ids=row.landlord_ids
            )
            properties.append(propertie)

    print properties

    return response.json(dict(
        properties=properties
    ))

# input: list of landlord ids
# output: list of landlord objs
#         data = { landlords: [{name: "", }, {}, {}] }
def get_landlords():
    landlords = []
    for row in db().select(orderby=db.landlords.last_name):
        if row.first_name is not None:
            landlord = dict(
                id           = row.id,
                first_name   = row.first_name,
                last_name    = row.last_name,
                property_ids = row.property_ids,
                review_ids   = row.review_ids,
                tag_ids      = row.tag_ids
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
    state = format_address_elem( address["state"] )
    zipcode = format_address_elem( address["zipcode"] )

    street = ""
    for s in address["street"].split():
        street = street + " " + format_address_elem(s)
    street = street.strip()

    city = ""
    for c in address["city"].split():
        city = city + " " + format_address_elem(c)
    city = city.strip()

    full_address = street + ", " + city + ', ' + state + ' ' + zipcode

    return full_address

# Private method to format name
def format_name(first_name, last_name):
    first_name = first_name.strip().lower().capitalize()
    last_name = last_name.strip().lower().capitalize()

    return (first_name, last_name)

# Private method to check if landlord exists
# If landlord exists, returns a landlord object
# landlord name needs to be formatted
def landlord_exists(first_name, last_name):
    q = ((db.landlords.first_name == first_name) & (db.landlords.last_name == last_name))
    r = db(q).select().first()
    if r:
        return dict(
            id           = r.id,
            first_name   = r.first_name,
            last_name    = r.last_name,
            property_ids = r.property_ids,
            review_ids   = r.review_ids,
            tag_ids      = r.tag_ids
        )
    else:
        return None

# Add a landlord into table landlords
# If landlord already exists, add_landlord() will return the existing
# landlord as a landlord object
# input: name, website
# output: data = {name: "name", website: "website url", property_ids: [4, 5]}
def add_landlord():
    # Return an error if landlord name is null
    if request.vars.first_name and request.vars.last_name:
        (first_name, last_name) = format_name(request.vars.first_name, request.vars.last_name)
    else:
        print ("In add_landlord(): Name can't be null")
        return("nok")

    website = request.vars.website
    address = 'Slack me if this is used -Ben'

    # If landlord exists, return it.
    landlord = landlord_exists(first_name, last_name)
    if landlord:
        landlord['address'] = address
        landlord['website'] = website
        # return response.json(dict(
        #     id = landlord['id'],
        #     landlord = landlord
        # ))
    # If not insert it
    else:
        # Insert landlord landlords
        landlord_id = db.landlords.insert(
            first_name = first_name,
            last_name  = last_name
        )

        landlord = dict(
            id = landlord_id,
            first_name=first_name,
            last_name=last_name,
            property_ids  = [],
            review_ids   = [],
            tag_ids      = [],
            address = address,
            website = website,
        )

    # Returns the landlord info.
    return response.json(dict(
        id = landlord['id'],
        landlord = landlord
    ))

# Get a list of properties based on list of property ids pssed in
# input: list of property ids
# output: list of property obj
#         data = { properties: [{address: "", }, {}, {}] }
def get_properties(inputIds=None):
    if inputIds:
        ids = inputIds
    else:
        ids = request.vars.property_ids if request.vars.property_ids else []

    properties = []

    for row in db().select(orderby=db.properties.address):
        if row.id in ids:
            propertie = dict(
                id=row.id,
                address=row.address,
                landlord_ids=row.landlord_ids
            )
            properties.append(propertie)

    return response.json(dict(
        properties=properties
    ))

# private method, not an actual route
def add_property():
    return response.json(dict(
        msg='add_property'
    ))

# Get all the reviews of a landlord based on landlord_id
# Also returns average landlord rating, average property rating,
# and list of addresses the landlord owns
# input: landlord_id
# output: list of review objs
#         data = { ave_l_rating: 3.4, ave_p_rating: 5.2, addresses: [list of property addresses the landlord owns], reviews: [{landlord_id: "", }, {}, {}] }
def get_reviews():
    if request.vars.landlord_id:
        landlord_id = request.vars.landlord_id;
    else:
        print "[Error] get_reviews(): landlord_id cannot be Null"
        raise HTTP(500)
        # landlord_id = 10

    reviews = []
    l_rating_sum = 0
    p_rating_sum = 0
    review_count = 0

    q_review = (db.reviews.landlord_id == landlord_id)
    for row in db(q_review).select(orderby=~db.reviews.updated_on):
        # book keeping for averages/ids
        if landlord_rating:
            l_rating_sum += row.landlord_rating
        if row.property_rating:
            p_rating_sum += row.property_rating
        review_count += 1

        review = dict(
            id=row.id,
            landlord_id=row.landlord_id,
            property_id=row.property_id,
            landlord_rating=row.landlord_rating,
            property_rating=row.property_rating,
            rent_with_landlord_again=row.rent_with_landlord_again,
            rent_with_property_again=row.rent_with_property_again,
            landlord_tag_ids=row.landlord_tag_ids,
            property_tag_ids=row.property_tag_ids,
            comments=row.comments
        )
        reviews.append(review)

    if review_count != 0:
        ave_l_rating = round((l_rating_sum * 1.0)/review_count, 1)
        ave_p_rating = round ((p_rating_sum * 1.0)/review_count, 1)
    else:
        ave_l_rating = 0
        ave_p_rating = 0

    # Get a list of property_ids owned by the landlord
    q_landlord = (db.landlords.id == landlord_id)
    row = db(q_landlord).select(db.landlords.property_ids).first()
    property_ids = row.property_ids

    # Get a list of addresses from list of property_ids
    properties = json.loads(get_properties(property_ids))["properties"]
    addresses = [ p["address"].encode('ascii','ignore') for p in properties ]
    # print addresses

    return response.json(dict(
        reviews=reviews,
        ave_l_rating=ave_l_rating,
        ave_p_rating=ave_p_rating,
        addresses=addresses
    ))

# Boolean method that checks if address exists
# Doesn't actually return property object
def address_exists(address_str):
    q = (db.properties.address == address_str)
    r = db(q).select(db.properties.id).first()
    if r:
        return r.id
    else:
        return None

# Private method to insert into table reviews when given a review
def insert_into_reviews(review):
    review_id = db.reviews.insert(
        landlord_id = review['landlord_id'],
        property_id = review['property_id'],
        landlord_rating = review['landlord_rating'],
        property_rating = review['property_rating'],
        rent_with_landlord_again = review['rent_with_landlord_again'],
        rent_with_property_again = review['rent_with_property_again'],
        landlord_tag_ids = review['landlord_tag_ids'],
        property_tag_ids = review['landlord_tag_ids'],
        comments = review['comments']
    )

    return review_id

# Private method to update a landlord's review_ids, property_ids,
# and tag_ids. Called right after a review has been inserted into db
def update_landlord(landlord_id, landlord_obj):
    q = (db.landlords.id == landlord_id)
    r = db(q).select().first()
    # Update property_ids
    if r.property_ids:
        property_ids = set(r.property_ids)
        property_ids.add( landlord_obj['property_id'] )
        property_ids = list(property_ids)
    else:
        property_ids = [ landlord_obj['property_id'] ]

    r.property_ids = property_ids

    # Update review_ids
    if r.review_ids:
        review_ids = set(r.review_ids)
        review_ids.add( landlord_obj['review_id'] )
        review_ids = list(review_ids)
    else:
        review_ids = [ landlord_obj['review_id'] ]

    r.review_ids = review_ids

    # Update tag_ids
    if r.tag_ids:
        tag_ids = set(r.tag_ids)
        tag_ids = tag_ids.union( set(landlord_obj['tag_id']) )
        tag_ids = list(tag_ids)
    else:
        tag_ids = landlord_obj['tag_ids']

    r.tag_ids = tag_ids

    r.update_record()

# input:
# landlord_id
# street: null, -
# city: null, -
# state: null, -
# zip: null, -
# landlord_rating: 1,
# property_rating: 1,
# rent_with_landlord_again: null,
# rent_with_property_again: null,
# landlord_tag_ids: [],
# property_tag_ids: [],
# comments: null
# output: "ok"
def add_review():
    if request.vars.landlord_id:
        landlord_id = request.vars.landlord_id
    else:
        print "In add_review(): landlord_id should never be 0"
        return "nok"

    address_obj = dict(
        street  = request.vars.street,
        city    = request.vars.city,
        state   = request.vars.state,
        zipcode = request.vars.zip
    )
    address = format_address(address_obj)

    # Check if property already exists
    # If exists, get property_id and add landlord_id to list landlord_ids
    property_id = address_exists(address)
    if property_id:
        q = (db.properties.id == property_id)
        r = db(q).select().first()
        if r.landlord_ids: # if landlord_ids is not NULL
            landlord_ids = set(r.landlord_ids)
            landlord_ids.add(landlord_id)
            landlord_ids = list(landlord_ids)
        else: # if landlord_ids is NULL
            landlord_ids = [landlord_id]
        r.update_record(landlord_ids=landlord_ids)
    # If property doesn't exist yet
    # Insert property to db and get property id
    else:
        property_id = db.properties.insert(
            address = address,
            landlord_ids = [landlord_id])

    # Insert review
    review_obj = dict(
        landlord_id = landlord_id,
        property_id = property_id,
        landlord_rating = request.vars.landlord_rating,
        property_rating = request.vars.property_rating,
        rent_with_landlord_again = request.vars.rent_with_landlord_again,
        rent_with_property_again = request.vars.rent_with_property_again,
        landlord_tag_ids = request.vars.landlord_tag_ids,
        property_tag_ids = request.vars.landlord_tag_ids,
        comments = request.vars.comments
    )

    review_id = insert_into_reviews(review_obj)

    # Insert landlord landlords
    landlord_obj = dict(
        property_id = property_id,
        review_id   = review_id,
        tag_ids     = request.vars.landlord_tag_ids
    )
    update_landlord(landlord_id, landlord_obj)

    return "ok"

# redirect to about page's html template
def about():
    return dict()
# redirect to contact page's html template
def contact():
    return dict()
