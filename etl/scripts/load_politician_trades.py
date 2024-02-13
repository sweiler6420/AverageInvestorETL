from schemas.politician_trades import *
from pydantic import ValidationError
from utils import utils
import requests
import sys

def get_asset(record):
    asset_input = {
        "asset_id": record['_assetId'],
        "asset_type": record['asset']['assetType'],
        "asset_ticker": record['asset']['assetTicker'],
        "instrument": record['asset']['instrument']
    }

    try:
        asset_obj = Asset(**asset_input)

        print(asset_obj.asset_id)
        print(asset_obj.asset_ticker)
        
    except ValidationError as e:
        print(e)

def get_issuer(record):
    issuer_input = {
        "issuer_id": record['_issuerId'],
        "state_id": record['issuer']['_stateId'],
        "country": record['issuer']['country'],
        "issuer_name": record['issuer']['issuerName'],
        "issuer_ticker": record['issuer']['issuerTicker'],
        "sector": record['issuer']['sector'],
    }

    try:
        issuer_obj = Issuer(**issuer_input)

        print(issuer_obj.issuer_id)
        print(issuer_obj.issuer_ticker)
        
    except ValidationError as e:
        print(e)
    

def get_politician(record):
    politician_input = {
        "politician_id": record['_politicianId'],
        "state": record['politician']['_stateId'],
        "chamber": record['politician']['chamber'],
        "dob": record['politician']['dob'],
        "first_name": record['politician']['firstName'],
        "gender": record['politician']['gender'],
        "last_name": record['politician']['lastName'],
        "party": record['politician']['party']
    }

    try:
        politician_obj = Politician(**politician_input)

        print(politician_obj.politician_id)
        print(politician_obj.state)
        
    except ValidationError as e:
        print(e)


def get_trades(record):
    trade_input = {
        "trade_id": record['_txId'],
        "politician_id": record['_politicianId'],
        "asset_id": record['_assetId'],
        "issuer_id": record['_issuerId'],
        "published_date": record['pubDate'],
        "filing_date":  record['filingDate'],
        "transaction_date": record['txDate'],
        "direction":  record['txType'],
        "has_capital_gains":  record['hasCapitalGains'],
        "owner":  record['owner'],
        "chamber": record['chamber'],
        "price":  record['price'],
        "size":  record['size'],
        "size_range_high":  record['sizeRangeHigh'],
        "size_range_low": record['sizeRangeLow'],
        "value": record['value'],
        "filing_id": record['filingId'],
        "filing_url":  record['filingURL'],
        "reporting_gap":  record['reportingGap'],
        "comment":  record['comment']
    }

    try:
        trade_obj = PoliticianTrades(**trade_input)

        print(trade_obj.politician_id)
        print(trade_obj.owner)
        
    except ValidationError as e:
        print(e)
    

def get_page():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Origin': 'https://www.capitoltrades.com',
        'Referer': 'https://www.capitoltrades.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    session = requests.Session()

    url = "https://bff.capitoltrades.com/trades"

    first_page = session.get(url, headers=headers).json()
    yield first_page


def process_records():

    for page in get_page():
        for record in page['data']:
            get_politician(record)
            get_trades(record)
            get_issuer(record)
            get_asset(record)


def main(args: None):

    config = utils.getConfigVars()

    process_records()

if __name__ == "__main__":

    args = sys.argv[1:]
    main(args=args)