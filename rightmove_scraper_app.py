import os
from argparse import ArgumentParser
from datetime import date
from pandas import DataFrame
from areainfo.borough import Borough
from areainfo.boroughs import get_boroughs
from resources.file_paths import data_save_path_prefix
from rightmove import rightmove_api

__save_path_template = data_save_path_prefix + "/{region}/{date}/{numBedrooms}"
__file_name = "housing_data.csv"
__max_bedrooms = 10


def save_results(curr_date: str, borough_name: str, num_bedrooms: int, result: DataFrame, dry_run: bool):
    if not is_int(num_bedrooms):
        return

    save_path = __save_path_template.format(
        date=curr_date,
        region=borough_name,
        numBedrooms=int(num_bedrooms)
    )
    print("Saving rightmove data for: {}".format(save_path))

    if dry_run:
        return

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    result.to_csv(os.path.join(save_path, __file_name))


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def save_all_days_data(borough: Borough, dry_run: bool):
    """
    Scrape rightmove for borough data with properties added any time. Since this
    will return a large amount of properties for each borough, we additionally
    partition the scraping queries by the number of bedrooms
    """

    for num_bedrooms in range(0, __max_bedrooms + 1):
        print("Scraping rightmove for borough: {}, bedrooms = {}, days = {}".format(borough.name, num_bedrooms, "ALL"))

        results = rightmove_api.get(borough.rightmove_code, min_bedrooms=num_bedrooms, max_bedrooms=num_bedrooms)
        added_dates = results.date_added.unique()

        for curr_date in added_dates:
            results_for_date = results.loc[results["date_added"] == curr_date]
            save_results(curr_date, borough.name, num_bedrooms, results_for_date, dry_run)


def save_last_day_of_data(curr_date: str, borough: Borough, dry_run: bool):
    """
    Scrape rightmove for borough data with properties added in the last 24 hours
    """

    print("Scraping rightmove for borough: {}, days: {}".format(borough.name, 1))

    results = rightmove_api.get(borough.rightmove_code, days_added=1)
    bedrooms_available = results.number_bedrooms.unique()

    for bedrooms in bedrooms_available:
        results_for_num_bedrooms = results.loc[results["number_bedrooms"] == bedrooms]
        save_results(curr_date, borough.name, bedrooms, results_for_num_bedrooms, dry_run)


def run_main(args):
    backfill = args.backfill
    borough_name = args.borough
    excluded_borough = args.excludeBorough
    dry_run = args.dryRun

    today = date.today().strftime("%Y-%m-%d")
    for borough in get_boroughs():
        if (borough_name and not borough_name == borough.name) or excluded_borough == borough.name:
            continue
        if backfill:
            save_all_days_data(borough, dry_run)
        else:
            save_last_day_of_data(today, borough, dry_run)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--backfill", help="Backfill all rightmove data", action="store_true")
    parser.add_argument("--borough", help="Borough to run data collection for", type=str)
    parser.add_argument("--excludeBorough", help="Exclude the borough from the results", type=str)
    parser.add_argument("--dryRun", help="Don't save the data to file", action="store_true")
    parsed_args = parser.parse_args()

    run_main(parsed_args)
