# serviexpress/widgets.py
from django.forms.widgets import TimeInput

class formato_hora(TimeInput):
    input_type = 'time'
    format = '%I:%M %p'