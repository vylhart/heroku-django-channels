
import os,django
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter
from chat.routing import websocket_urlpatterns
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainapp.settings")
django.setup()

application = ProtocolTypeRouter({
    "http":      AsgiHandler(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
