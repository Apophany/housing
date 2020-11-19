import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import ticker

from areainfo import boroughs
from areainfo.borough import Borough
from resources.file_paths import data_save_path_prefix

__file_name = "/housing_data.csv"
__search_root_path = data_save_path_prefix + "/{region}"
__search_path = data_save_path_prefix + "/{region}/{date}/{num_bedrooms}" + __file_name


def get_data(borough: Borough, num_bedrooms: int):
    results = pd.DataFrame(columns=['date', 'avg_price', 'count'])
    root = __search_root_path.format(region=borough.name)
    for date_entry in os.scandir(root):
        data_path = __search_path.format(region=borough.name, date=date_entry.name, num_bedrooms=num_bedrooms)
        if os.path.isfile(data_path):
            data = pd.read_csv(data_path)
            results.loc[len(results)] = [date_entry.name, data['price'].mean(), len(data)]

    return results


def plot(loc: Borough, bedrooms: int):
    results = get_data(loc, bedrooms)
    results = results.tail(110)

    x_axis_data = results.index
    y_axis_data = results['avg_price']

    poly_coefficients = np.polyfit(x_axis_data, y_axis_data, 3)
    trend_function = np.poly1d(poly_coefficients)

    fig, ax = plt.subplots()
    ax.set_title(loc.name + ' ' + str(bedrooms) + ' Bedrooms')

    ax2 = ax.twinx()
    ax2.set_ylabel('Daily Listed Volume', rotation=90, labelpad=15, fontdict={'fontsize': 16})
    ax2.bar(x_axis_data, results['count'], width=0.3, color='gray', alpha=0.3)

    ax.set_ylabel('Average Daily Price', rotation=90, labelpad=15, fontdict={'fontsize': 16})
    ax.set_xticks(x_axis_data)
    ax.set_xticklabels(results['date'], rotation=90)
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    ax.plot(x_axis_data, y_axis_data, color='blue')
    ax.plot(x_axis_data, trend_function(x_axis_data), color='orange')
    plt.show()


if __name__ == "__main__":
    plot(loc=boroughs.HACKNEY, bedrooms=2)
