from task_geo.data_sources.noaa.api_connector import noaa_api_connector
from task_geo.data_sources.noaa.api_formatter import noaa_api_formatter


def noaa_api(countries, start_date, end_date):
    raw = noaa_api_connector(countries, start_date, end_date)
    return noaa_api_formatter(raw)
