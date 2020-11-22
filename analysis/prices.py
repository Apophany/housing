import os
from datetime import datetime

import matplotlib.pyplot as mplt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from matplotlib import ticker

from areainfo import boroughs
from areainfo.borough import Borough
from resources.file_paths import data_save_path_prefix

__file_name = "/housing_data.csv"
__search_root_path = data_save_path_prefix + "/{region}"
__search_path = data_save_path_prefix + "/{region}/{date}/{num_bedrooms}" + __file_name


class Frequency:
    DAILY = 'Daily'
    MONTHLY = 'Monthly'


def get_data(borough: Borough, num_bedrooms: int):
    results = pd.DataFrame(columns=['date', 'price'])
    root = __search_root_path.format(region=borough.name)
    for date_entry in os.scandir(root):
        data_path = __search_path.format(region=borough.name, date=date_entry.name, num_bedrooms=num_bedrooms)
        if os.path.isfile(data_path):
            data = pd.read_csv(data_path)
            data['date'] = datetime.strptime(date_entry.name, '%Y-%m-%d')
            results = results.append(data[['date', 'price']], ignore_index=True)

    return results.set_index('date')


def plot(loc: Borough, bedrooms: int, groupby=Frequency.MONTHLY, start_date=datetime(2015, 1, 1)):
    results = get_data(loc, bedrooms)
    results = results[results.index > start_date]
    results.dropna(inplace=True)

    freq = 'M' if groupby == Frequency.MONTHLY else 'D'
    grouped_data = results.groupby(pd.Grouper(freq=freq), dropna=True)
    grouped_prices = grouped_data.mean().dropna()
    grouped_volume = grouped_data.count().loc[grouped_data.count()['price'] > 0]

    x_axis_data = grouped_prices.index
    y_axis_data = grouped_prices['price']

    poly_coefficients = np.polyfit(mdates.date2num(x_axis_data), y_axis_data, 3)
    trend_function = np.poly1d(poly_coefficients)

    fig, ax = mplt.subplots()
    ax.set_title(loc.name + ' ' + str(bedrooms) + ' Bedrooms')

    title = 'Monthly' if groupby == Frequency.MONTHLY else 'Daily'

    ax2 = ax.twinx()
    ax2.set_ylabel(title + ' Listed Volume', rotation=90, labelpad=15, fontdict={'fontsize': 16})
    ax2.bar(x_axis_data, grouped_volume['price'], width=0.3, color='gray', alpha=0.3)

    ax.set_ylabel('Average ' + title + ' Price', rotation=90, labelpad=15, fontdict={'fontsize': 16})
    ax.set_xticks(x_axis_data)
    ax.set_xticklabels(grouped_prices.index, rotation=90)
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.get_xaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: mdates.num2date(x).strftime('%d-%m-%Y')))

    ax.plot(x_axis_data, y_axis_data, color='blue')
    ax.plot(x_axis_data, trend_function(mdates.date2num(x_axis_data)), color='orange')
    mplt.show()


if __name__ == "__main__":
    plot(loc=boroughs.WALTHAM_FOREST, bedrooms=2, start_date=datetime(2020, 1, 1))
