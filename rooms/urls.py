from rest_framework.routers import DefaultRouter
from . import viewsets
from django.urls import path
from . import views

router = DefaultRouter()
router.register("room", viewsets.RoomViewset, basename="room")

app_name = "rooms"

urlpatterns = router.urls
# [
#     # path("list", views.ListRoomsView.as_view()),
#     # path("<int:pk>/", views.SeeRoomView.as_view()),
# ]
