#! /bin/bash

type turnstile_data_master_with_weather.csv | python riders_per_station_mapper.py  | sort | python riders_per_station_reducer.py > result.txt

