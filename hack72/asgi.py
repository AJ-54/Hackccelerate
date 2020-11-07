
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hack72.settings')

import django
django.setup()



from django.core.asgi import get_asgi_application
from channels.routing import get_default_application




from channels.auth import AuthMiddlewareStack
import chat.routing





application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})