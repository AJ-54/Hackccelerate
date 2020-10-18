from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
#import Notifications.routing
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': 
        URLRouter(
            chat.routing.websocket_urlpatterns
 #           +Notifications.routing.websocket_urlpatterns
        
    ),
})
