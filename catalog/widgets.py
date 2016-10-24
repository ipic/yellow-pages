from django.conf import settings
from django.forms import widgets
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt


class GoogleMapsAddressWidget(widgets.TextInput):
    "a widget that will place a google map right after the #id_address field"

    class Media:
        css = {'all': (settings.STATIC_URL + 'css/google-maps-admin.css',)}
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js',
            'https://maps.google.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
            settings.STATIC_URL + 'js/google-maps-admin.js',
        )

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))
        html = u'<input%s /><div class="map_canvas_wrapper"><div id="map_canvas"></div></div>'
        return mark_safe(html % flatatt(final_attrs))
