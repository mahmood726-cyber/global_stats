import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from pipelines.ingest_data import fetch_who_data, fetch_worldbank_data

def test_who_data():
    df = fetch_who_data()
    assert not df.empty
    assert 'iso3' in df.columns
    assert 'cvd_mortality_rate' in df.columns

def test_worldbank_data():
    df = fetch_worldbank_data()
    assert not df.empty
    assert 'gdp_per_capita' in df.columns
    assert 'health_exp_pct_gdp' in df.columns