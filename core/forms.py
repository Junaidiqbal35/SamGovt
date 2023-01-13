import datetime

from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class SamGovtForm(forms.Form):
    OPTIONS = (
        ("u", "Justification (J & A)"),
        ("p", "Pre solicitation"),
        ("a", "Award Notice"),
        ("r", " Sources Sought"),
        ("s", " Special Notice"),
        ("o", " Solicitation"),
        ("g", " Sale of Surplus Property"),
        ("k", " Combined Synopsis / Solicitation"),
        ("i", " Intent to  Bundle Requirements(DoD - Funded)")
    )

    ptype = forms.ChoiceField(choices=OPTIONS)
    naicsCode = forms.CharField(max_length=255)
    postedDate = forms.DateField(widget=DateInput(format='%d/%m%Y'))
    postedto = forms.DateField(widget=DateInput(format='%d/%m%Y'))
