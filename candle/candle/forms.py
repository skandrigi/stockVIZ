from django import forms

DURATION_CHOICES = [
    ('1d', '1 Day'),
    ('5d', '5 Days'),
    ('1mo', '1 Month'),
    ('3mo', '3 Months'),
    ('6mo', '6 Months'),
    ('ytd', 'Year-To-Date'),
    ('1y', '1 Year'),
    ('2y', '2 Years'),
    ('5y', '5 Years'),
    ('10y', '10 Years'),
]

class tickerForm(forms.Form):
    post = forms.CharField(label="Enter Stock Ticker", max_length=5)
    duration = forms.ChoiceField(label="Select Duration", choices=DURATION_CHOICES)