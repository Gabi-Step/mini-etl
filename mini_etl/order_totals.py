from datetime import datetime

import pandas as pd


def customer_total_orders_value(conn) -> None:
    """Get all active customers and their total order value.
    Store results in a csv file.
    conn: database connection.
    """
    df = pd.read_sql_query('''
        SELECT o.customer_id, c.first_name, c.last_name, o.quantity, o.price
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        WHERE c.status = "active"
    ''', conn)

    df['order_value'] = df['quantity'] * df['price']

    totals = df.groupby(['customer_id', 'first_name', 'last_name'])['order_value'].sum().reset_index()
    totals['full_name'] = totals['first_name'] + ' ' + totals['last_name']

    final = totals[['full_name', 'order_value']].rename(columns={'order_value': 'total'})
    final.to_csv(f'.customer_total_orders_value-{datetime.now()}.csv', index=False)