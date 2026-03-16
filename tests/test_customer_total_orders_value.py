import pandas as pd

from mini_etl.db import get_db
from mini_etl.order_totals import customer_total_orders_value


def test_customer_total_orders_value(client):
    ...