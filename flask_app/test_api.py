from app import flask_app

client = flask_app.test_client()

def test_test():
    response = client.get("/")
    assert response.json['result'] == 'ok'

def test_predict():

    response = client.post("/predict",
                           data={
                               'General government revenue | Percent of GDP': '0',
                               'General government total expenditure | National currency | Billions': '0',
                               'Gross national savings | Percent of GDP': '0',
                               'Total investment | Percent of GDP': '0',
                               'Unemployment rate | Percent of total labor force': '0'
                           })

    assert response.status_code == 200

    assert response.json['results'] == ['Versicolor']