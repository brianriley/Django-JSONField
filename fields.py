from django.core import exceptions
from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import Field, TextField
try:
    import json
except ImportError:
    from django.utils import simplejson as json

class JSONField(TextField):
    description = _('JSON text')
    
    default_error_messages = {
        'invalid': _('Enter a valid JSON string.')
    }
    
    def __init__(self, verbose_name=None, name=None, schema_path=None, **kwargs):
        self.schema_path = schema_path
        Field.__init__(self, verbose_name, name, **kwargs)
    
    def get_internal_type(self):
        return 'JSONField'
    
    def to_python(self, value):
        try:
            return json.loads(value)
        except ValueError:
            raise exceptions.ValidationError(self.error_messages['invalid'])