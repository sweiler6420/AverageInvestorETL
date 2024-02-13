from pydantic import BaseModel, EmailStr, Field, conint
from datetime import datetime, date, time
from typing import Optional
from uuid import UUID

class Politician(BaseModel):
    politician_id: str = Field(..., max_length=50)
    state: str = Field(..., max_length=5)
    chamber: Optional[str] = Field(None, max_length=50)
    dob: Optional[date] = Field(None)
    first_name: str = Field(..., max_length=80)
    last_name: str = Field(..., max_length=80)
    gender: Optional[str] = Field(None, max_length=25)
    party: str = Field(..., max_length=50)

    # class Config:
    #     orm_mode = True

class Asset(BaseModel):
    asset_id: conint(gt=10000000) = Field(...)
    asset_type: str =  Field(None, max_length=50)
    asset_ticker: str = Field(None)
    instrument: str = Field(None)


class Issuer(BaseModel):
    issuer_id: conint(gt=10000) = Field(...)
    state_id: str = Field(None)
    country: str = Field(None)
    issuer_name: str = Field(None, max_length=100)
    issuer_ticker: str = Field(None, max_length=35)
    sector: str = Field(None, max_length=100)


class PoliticianTrades(BaseModel):
    trade_id: conint(gt=1000000000) = Field(...)
    politician_id: str = Field(..., max_length=50)
    asset_id: conint(gt=10000000) = Field(...)
    issuer_id: conint(gt=10000) = Field(...)
    published_date: datetime = Field(...)
    filing_date: date = Field(...)
    transaction_date: date = Field(...)
    direction: str = Field(..., max_length=10)
    has_capital_gains: bool = Field(default=False)
    owner: str = Field(..., max_length=30)
    chamber: str = Field(..., max_length=30)
    price: float = Field(None)
    size: int = Field(None)
    size_range_high: int = Field(None)
    size_range_low: int = Field(None)
    value: int = Field(None)
    filing_id: conint(gt=10000000)
    filing_url: str = Field(..., max_length=255)
    reporting_gap: int = Field(...)
    comment: str = Field(None, max_length=200)
