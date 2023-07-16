from django.shortcuts import render
from candle.forms import tickerForm
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
import yfinance as yf
import pandas as pd
from datetime import date, timedelta
import matplotlib as mpl
from matplotlib import pyplot as plt

mpl.use('Agg')

import os
from django.conf import settings

@csrf_protect
@ensure_csrf_cookie
def home(request):
    context = {}
    context['form'] = tickerForm()
    return render(request, 'base.html', context)

@csrf_protect
@ensure_csrf_cookie
def custom_post(request):
    if request.method == 'POST':
        form = tickerForm(request.POST)
        if form.is_valid():
            post_data = form.cleaned_data['post']
            time = form.cleaned_data['duration']
            result = grap(post_data, time)
            args = {'form': form, 'text': post_data, 'result': result}
            return render(request, 'result.html', args)
        else:
            return render(request, 'base.html', {'form': form})
    else:
        form = tickerForm()
    
    return render(request, 'base.html', {'form': form})

def grap(data, time):
    gData = yf.download(data, period=time)
    plt.figure(figsize=(20, 6))
    plt.plot(gData.index, gData['Adj Close'])
    plt.title(f"Stock Price for {data} ({time})")
    plt.xlabel('Date')
    plt.ylabel('Stock Price (Adj Close)')
    
    img_path = os.path.join(settings.MEDIA_ROOT, 'stock_plot.png')
    plt.savefig(img_path)
    plt.close()

    img_url = os.path.join(settings.MEDIA_URL, 'stock_plot.png')

    return img_url