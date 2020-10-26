from rightmove.scraper import RightmoveData

__base_url = "https://www.rightmove.co.uk/property-for-sale/find.html?" \
             "searchType=SALE" \
             "&locationIdentifier=REGION%{regionCode}" \
             "&insId=1" \
             "&radius=0.0" \
             "&minPrice={minPrice}" \
             "&maxPrice={maxPrice}" \
             "&minBedrooms={minBedrooms}" \
             "&maxBedrooms={maxBedrooms}" \
             "&displayPropertyType=" \
             "&maxDaysSinceAdded={maxDaysSinceAdded}" \
             "&includeSSTC=true" \
             "&_includeSSTC=on" \
             "&sortByPriceDescending=" \
             "&primaryDisplayPropertyType=" \
             "&secondaryDisplayPropertyType=" \
             "&oldDisplayPropertyType=" \
             "&oldPrimaryDisplayPropertyType=" \
             "&newHome=" \
             "&auction=false"


def scrape(region, min_bedrooms=None, max_bedrooms=None, days_added=None):
    url = __rightmove_url(
        region_code=region,
        min_bedrooms=min_bedrooms,
        max_bedrooms=max_bedrooms,
        max_days_since_added=days_added
    )
    rm = RightmoveData(url)
    return rm.get_results


def __rightmove_url(
        region_code: str,
        min_price: int = None,
        max_price: int = None,
        min_bedrooms: int = None,
        max_bedrooms: int = None,
        max_days_since_added: int = None
):
    return __base_url.format(
        regionCode=region_code,
        minPrice=__xstr(min_price),
        maxPrice=__xstr(max_price),
        minBedrooms=__xstr(min_bedrooms),
        maxBedrooms=__xstr(max_bedrooms),
        maxDaysSinceAdded=__xstr(max_days_since_added)
    )


def __xstr(s):
    if s is None:
        return ''
    return str(s)
