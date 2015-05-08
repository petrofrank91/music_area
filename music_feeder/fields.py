from __future__ import unicode_literals

from ipware.ip import get_ip


class CurrentUserIPDefault(object):
    def set_context(self, serializer_field):
        request = serializer_field.context['request']
        ip_address = get_ip(request)
        # assert ip_address, "We need user IP here"
        self.ip_address = ip_address

    def __call__(self):
        return self.ip_address
