import os
import sys

import pandas as pd

from areainfo import boroughs, borough
from resources.file_paths import data_save_path_prefix

__search_root_path = data_save_path_prefix + "/{region}"
__file_name = "/housing_data.csv"


def search(
        search_borough: borough,
        postcode: str = None,
        address: str = None,
        min_bedrooms: int = 0,
        max_bedrooms: int = 10,
        price_min: float = 0,
        price_max: float = sys.float_info.max
):
    results = pd.DataFrame()
    search_root_path = __search_root_path.format(region=search_borough.name)
    for date_path in os.scandir(search_root_path):
        for bedroom_path in os.scandir(date_path):
            if min_bedrooms <= int(bedroom_path.name) <= max_bedrooms:
                data = pd.read_csv(bedroom_path.path + __file_name)
                data = data.loc[data["price"].between(price_min, price_max)]
                if address is not None:
                    data = data.loc[data["address"].str.contains(address)]
                if postcode is not None:
                    data = data.loc[data["postcode"].sts.contains(postcode)]
                if data.size > 0:
                    results = results.append(data)
    return results


if __name__ == "__main__":
    res = search(
        search_borough=boroughs.HARINGEY,
        address='Elder Avenue',
        min_bedrooms=2,
        max_bedrooms=2,
        price_min=450_000,
        price_max=600_000
    )
    print(res.to_markdown())
