
def test_get_customer(client):
    response = client.get('/customers/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['first_name'] == 'John'
    assert data['last_name'] == 'Doe'
    assert len(data['orders']) == 2
    assert data['orders'][0]['product_name'] == 'Yorkshire pudding'


def test_get_customer_not_found(client):
    response = client.get('/customers/999')
    assert response.status_code == 404
    assert response.get_json()['error'] == 'Customer not found'


def test_get_customer_no_orders(client):
    response = client.get('/customers/4')
    assert response.status_code == 200
    assert response.get_json()['orders'] == []