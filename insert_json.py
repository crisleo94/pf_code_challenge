import json

import psycopg2
from psycopg2.extras import Json

conn = psycopg2.connect(
    host='localhost',
    port='5454',
    database='sprockets',
    user='postgres',
    password='postgres'
)

cur = conn.cursor()

def insert_factory_data():
    with open('seed_factory_data.json') as f:
        factories = json.load(f).get('factories')

    for factory in factories:
        chart_data = json.dumps(factory.get('factory').get('chart_data'))
        print(chart_data)
        cur.execute(
            'INSERT INTO factory (chart_data) VALUES (%s)',
            [chart_data]
        )

    conn.commit()
    cur.close()
    conn.close()

def insert_sprockets():
    with open('seed_sprocket_types.json') as f:
        sprockets_data = json.load(f).get('sprockets')

    for sp in sprockets_data:
        cur.execute(
            'INSERT INTO sprocket (teeth, pitch_diameter, outside_diameter, pitch) VALUES (%s, %s, %s, %s)',
            (sp.get('teeth'),sp.get('pitch_diameter'),sp.get('outside_diameter'),sp.get('pitch'))
        )

    conn.commit()
    cur.close()
    conn.close()

# insert_sprockets()
insert_factory_data()
