import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()
from atlas.src.atlas.data_service import YahooDataExtractor,import_data_from_csv


if __name__ == '__main__':
    import_data_from_csv(r'/Users/krzysztofbienias/Documents/Trade_Data_fixed_rules.csv')
    yahoo_extractor=YahooDataExtractor(tickers="PLNEUR=X",start_period='2025-01-20',end_period='2025-01-20')
    resu=yahoo_extractor.extract_data()
    print("THE END")
