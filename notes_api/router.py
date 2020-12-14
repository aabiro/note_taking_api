from notes_api.veiwsets import NoteViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('note', NoteViewset)

# API mapped to viewsets - localhost:p/api/note/6
# GET, PUT, UPDATE, DELETE
# List, retrieve