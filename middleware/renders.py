# core/renderers.py

from rest_framework.renderers import BrowsableAPIRenderer

class LocalBrowsableAPIRenderer(BrowsableAPIRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        request = renderer_context.get('request')
        ip = request.META.get('REMOTE_ADDR')

        # Solo permite la API web si la IP es local
        if ip not in ('127.0.0.1', '::1', '10.100.39.23','172.21.250.10'):
            return 'Consulte por Postman o thunderclient xd'# No muestra el navegador DRF
        return super().render(data, accepted_media_type, renderer_context)
