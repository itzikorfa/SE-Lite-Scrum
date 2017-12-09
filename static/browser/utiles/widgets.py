from django.forms.widgets import NumberInput

class RangeInput(NumberInput):
    input_type = 'range'
#
# widgets = {'sprint_duration': RangeInput(
#             attrs={'max': 30, 'min' : 7}
#         )}