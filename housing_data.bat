set SCRIPT_LOCATION=%1
set LOG_LOCATION=%2

call %CONDA_HOME%/scripts/activate.bat housing

python.exe %SCRIPT_LOCATION%/housing_scraper_app.py --logConfigFile %SCRIPT_LOCATION%/logging.conf --logFilePath %LOG_LOCATION%
