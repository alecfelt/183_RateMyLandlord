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

    # print("searching for " + search_name)

    landlords = []

    for row in db(db.landlords.first_name).select(orderby=db.landlords.last_name):
        if match_names(search_name, row.first_name, row.last_name):
            temp_landlord = dict(
                id=row.id,
                first_name=row.first_name,
                last_name=row.last_name,
                property_ids=row.property_ids,
                review_ids=row.review_ids,
                tag_ids=row.tag_ids,
                avg_l_rating = row.average_l_rating,
                avg_p_rating = row.average_p_rating
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
    str = request.vars.search_str if request.vars.search_str else ''
    matched_properties = []
    all_landlords = []

    # Populate all landlords
    for row in db().select(orderby=db.landlords.last_name):
        temp_landlord = dict(
            id=row.id,
            first_name=row.first_name,
            last_name=row.last_name,
            property_ids=row.property_ids,
            review_ids=row.review_ids,
            tag_ids=row.tag_ids,
            avg_l_rating = row.average_l_rating,
            avg_p_rating = row.average_p_rating
        )
        all_landlords.append(temp_landlord)

    for row in db().select(db.properties.id, db.properties.address, db.properties.landlord_ids, db.properties.tag_ids, orderby=db.properties.address):
        if match_address(str, row.address):

            ass_landlords = []

            # FIND THE LANDLORD
            for l_id in row.landlord_ids:
                for landlord in all_landlords:
                    if l_id == landlord["id"]:
                        ass_landlords.append(landlord)

            temp_property = dict(
                id=row.id,
                address=row.address,
                landlord_ids=row.landlord_ids,
                landlords=ass_landlords
            )
            matched_properties.append(temp_property)
    return response.json(dict(
        properties=matched_properties
    ))


# Get all landlords
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
                tag_ids      = row.tag_ids,
                avg_l_rating = row.average_l_rating,
                avg_p_rating = row.average_p_rating
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
    logger.info(request.vars)
    if request.vars.first_name and request.vars.last_name:
        (first_name, last_name) = format_name(request.vars.first_name, request.vars.last_name)
    else:
        # print ("In add_landlord(): Name can't be null")
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

# Private method, not an actual route
def add_property():
    return response.json(dict(
        msg='add_property'
    ))

#
def get_landlord(landlord_id=None):
    logger.info('request.vars')
    logger.info(request.vars)
    if request.vars.landlord_id:
        q = (db.landlords.id == request.vars.landlord_id)
    elif landlord_id:
        q = (db.landlords.id == landlord_id)
    else:
        # print("In get_landlord(): landlord_id cannot be NULL")
        return "nok"

    r = db(q).select().first()
    return dict(
        id           = r.id,
        first_name   = r.first_name,
        last_name    = r.last_name,
        property_ids = r.property_ids,
        review_ids   = r.review_ids,
        tag_ids      = r.tag_ids,
        avg_l_rating = r.average_l_rating,
        avg_p_rating = r.average_p_rating
    )


# private method to get average landlord rating and average property rating
def get_averages(landlord_id):
    l_rating_sum = 0
    p_rating_sum = 0
    review_count = 0

    q = (db.reviews.landlord_id == landlord_id)
    for r in db(q).select():
        # book keeping for averages/ids
        if r.landlord_rating:
            l_rating_sum += r.landlord_rating
        if r.property_rating:
            p_rating_sum += r.property_rating
        review_count += 1

    if review_count != 0:
        avg_l_rating = round((l_rating_sum * 1.0)/review_count, 1)
        avg_p_rating = round ((p_rating_sum * 1.0)/review_count, 1)
    else:
        avg_l_rating = 0
        avg_p_rating = 0

    # l_avg = db.reviews.landlord_rating.avg()
    # p_avg = db.reviews.property_rating.avg()
    #
    # r = db(q).select(l_avg, p_avg).first()
    # avg_l_rating = r[l_avg]
    # avg_p_rating = r[p_avg]
    #
    # print r[l_avg]
    # print("\n\naverage_l_rating: ", avg_l_rating)
    # print("average_p_rating: ", avg_p_rating)

    return (avg_l_rating, avg_p_rating)

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
        # print "[Error] get_reviews(): landlord_id cannot be Null"
        # raise HTTP(500)
        return "nok"
        # landlord_id = 10

    reviews = []
    # l_rating_sum = 0
    # p_rating_sum = 0
    # review_count = 0

    q_review = (db.reviews.landlord_id == landlord_id)
    for row in db(q_review).select(orderby=~db.reviews.updated_on):
        # book keeping for averages/ids
        # if landlord_rating:
        #     l_rating_sum += row.landlord_rating
        # if row.property_rating:
        #     p_rating_sum += row.property_rating
        # review_count += 1

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

    # if review_count != 0:
    #     ave_l_rating = round((l_rating_sum * 1.0)/review_count, 1)
    #     ave_p_rating = round ((p_rating_sum * 1.0)/review_count, 1)
    # else:
    #     ave_l_rating = 0
    #     ave_p_rating = 0

    # Get a list of property_ids owned by the landlord
    q_landlord = (db.landlords.id == landlord_id)
    row = db(q_landlord).select(db.landlords.property_ids).first()
    property_ids = row.property_ids

    # Get a list of addresses from list of property_ids
    properties = json.loads(get_properties(property_ids))["properties"]
    # addresses = [ p["address"].encode('ascii','ignore') for p in properties ]
    addresses = [ (str(p["address"])).encode('ascii','ignore') for p in properties ]
    # logger.info(type(addresses[0]))
    # print addresses

    landlord = get_landlord(landlord_id)

    return response.json(dict(
        reviews=reviews,
        landlord=landlord,
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
        property_tag_ids = review['property_tag_ids'],
        comments = review['comments']
    )

    return review_id

# Private method to update a landlord's review_ids, property_ids,
# and tag_ids. Called right after a review has been inserted into db
def update_landlord(landlord_id, landlord_obj):
    q = (db.landlords.id == landlord_id)
    r = db(q).select().first()
    first_name = r.first_name
    last_name = r.last_name

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
        tag_ids = tag_ids.union( set(landlord_obj['tag_ids']) )
        tag_ids = list(tag_ids)
    else:
        tag_ids = landlord_obj['tag_ids']

    r.tag_ids = tag_ids

    # Update landlord's avrage landlord rating and average property rating
    (avg_l_rating, avg_p_rating) = get_averages(landlord_id)
    r.average_l_rating = avg_l_rating
    r.average_p_rating = avg_p_rating

    r.update_record()

    # return dict(
    #     id           = landlord_id,
    #     first_name   = first_name,
    #     last_name    = last_name,
    #     property_ids = property_ids,
    #     review_ids   = review_ids,
    #     tag_ids      = tag_ids
    # )

def test_route():
    landlord_id = 2
    q = (db.landlords.id == landlord_id)
    r = db(q).select().first()
    (avg_l_rating, avg_p_rating) = get_averages(landlord_id)
    r.average_l_rating = avg_l_rating
    r.average_p_rating = avg_p_rating
    r.update_record()

def add_review():
    logger.info(request.vars.landlord_tag_ids)
    logger.info(request.vars.property_tag_ids)
    for var in request.vars:
        logger.info(var)
        logger.info(type(var))
    if request.vars.landlord_id:
        landlord_id = request.vars.landlord_id
    else:
        # print("In add_review(): landlord_id should never be null")
        return "nok"

    address_obj = dict(
        street  = request.vars.street,
        city    = request.vars.city,
        state   = request.vars.state,
        zipcode = request.vars.zip
    )
    # logger.info(address_obj)
    address = format_address(address_obj)
    logger.info(address)

    # Check if property already exists
    # If exists, get property_id and add landlord_id to list landlord_ids
    property_id = address_exists(address)
    logger.info(property_id)
    if property_id:
        logger.info('property already exists')
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
        property_id = str(db.properties.insert(
            address = address,
            landlord_ids = [landlord_id]))


    # convert tags to ints
    landlord_tags = request.vars.landlord_tag_ids.replace('[', '').replace(']', '').replace('"', '').replace('\\', '').split(',')
    property_tags = request.vars.property_tag_ids.replace('[', '').replace(']', '').replace('"', '').replace('\\', '').split(',')
    logger.info("landlord_tags")
    logger.info(landlord_tags)
    logger.info("property_tags")
    logger.info(property_tags)
    if '' in landlord_tags:
        landlord_tag_ids = []
    else:
        landlord_tag_ids = [int(l) for l in landlord_tags]

    if '' in property_tags:
        property_tag_ids = []
    else:
        property_tag_ids = [int(p) for p in property_tags]

    # convert yes and no to True and False
    rent_with_landlord_again = rent_with_property_again = True
    if request.vars.rent_with_landlord_again == 'no':
        rent_with_landlord_again = False
    if request.vars.rent_with_property_again == 'no':
        rent_with_property_again = False

    # Insert review
    review_obj = dict(
        landlord_id = landlord_id,
        property_id = property_id,
        landlord_rating = request.vars.landlord_rating,
        property_rating = request.vars.property_rating,
        rent_with_landlord_again = rent_with_landlord_again,
        rent_with_property_again = rent_with_property_again,
        landlord_tag_ids = landlord_tag_ids,
        property_tag_ids = property_tag_ids,
        comments = request.vars.comments
    )
    logger.info(review_obj)

    review_id = int(insert_into_reviews(review_obj))

    # Insert landlord landlords
    landlord_obj = dict(
        property_id  = property_id,
        review_id    = review_id,
        tag_ids      = landlord_tag_ids
    )
    logger.info(landlord_obj)
    logger.info(landlord_id)
    landlord_obj = update_landlord(landlord_id, landlord_obj)

    return "ok"

# redirect to about page's html template
def about():
    return dict()
# redirect to contact page's html template
def contact():
    return dict()
