# Here go your api methods.
def get_user_email():
    return auth.user.email if auth.user is not None else None

def get_memos():
    memos = []
    are_publics=0
    are_privates=0
    # Create a bunch of data
    db_rows = db().select(db.memo.ALL)
    for i, r in enumerate(db_rows):
        if r.user_email == get_user_email():
            are_privates+=1
        elif r.is_public:
            are_publics+=1
        temp_memo = dict(
            id = r.id,
            title=r.title,
            body=r.body,
            user_email=r.user_email,
            is_being_edited = False,
            is_public = r.is_public,
        )
        memos.insert(0, temp_memo)
    return response.json(dict(memos=memos, are_publics=are_publics, are_privates=are_privates))

def get_my_email():
    current_user = auth.user.email if auth.user is not None else None
    logged_in = True if auth.user is not None else False
    return response.json(dict(current_user=current_user, logged_in=logged_in))

@auth.requires_signature()
def add_memo():
    memo_id = db.memo.insert(
        title=request.vars.title,
        body=request.vars.body,
    )
    memo = db.memo(memo_id)
    memo['is_being_edited'] = False
    return response.json(dict(memo=memo))

@auth.requires_signature()
def del_memo():
    db(db.memo.id == request.vars.memo_id).delete()
    return "ok"

@auth.requires_signature()
def edit_memo():
    db(db.memo.id == request.vars.memo_id).update(
        body=request.vars.body,
        title=request.vars.title
    )
    return "ok"

@auth.requires_signature()
def toggle_publicity():
    db(db.memo.id == request.vars.memo_id).update(is_public=request.vars.is_public)
    return "ok"
