from cornicesqla import crud, DBView
from cornice import Service
from pyramid.view import view_config

from myblog.models import BlogEntry, BlogUser, DBSession
import json


#
# CRUD
#

@crud(mapping=BlogEntry, path='/blog/{id}', collection_path='/blog',
      session=DBSession)
class BlogView(DBView):
    pass


@crud(mapping=BlogUser, path='/users/{id}', collection_path='/users',
      session=DBSession)
class BlogUser(DBView):
    pass


#
# JS UI
#
@view_config(route_name='jsui', renderer='myblog:templates/home.mako')
def home(request):
    return {'title': 'Welcome to My Blog'}
