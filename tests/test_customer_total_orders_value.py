import pandas as pd

from mini_etl.db import get_db
from mini_etl.order_totals import customer_total_orders_value


def test_customer_total_orders_value(client):
    # TODO: potentially customer_total_orders_value needs a refactor to be more testable
    # This test was not as easy as it should've been
    ...