import json
from app.core.scrap import get_blogs, write_data_to_json
from app.utils.constants import DATES, JSONFILE

def main():
    base_url = 'https://eastcroydoncool.co.uk/'
    data = get_blogs(base_url,DATES)
    write_data_to_json(data, JSONFILE)

if __name__ == "__main__":
    main()