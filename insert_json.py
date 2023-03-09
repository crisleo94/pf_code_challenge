import json

factories = []

with open('seed_sprocket_types.json') as f:
    factories = json.load(f).get('sprockets')

with open('seed_factory_data.json') as f:
    productivity = json.load(f).get('factories')

for factory in factories:
    for prod in productivity:
      res = {
          'teeth': factory.get('teeth'),
          'pitch_diameter': factory.get('pitch_diameter'),
          'outside_diameter': factory.get('outside_diameter'),
          'pitch': factory.get('pitch'),
          'actual': 0,
          'goal': 0,
          'time': 0
      }

      time = prod.get('factory').get('chart_data').get('time')
      actual_prod = prod.get('factory').get('chart_data').get('sprocket_production_actual')
      expected_prod = prod.get('factory').get('chart_data').get('sprocket_production_goal')

      for i in range(len(time)):
          actual = actual_prod[i]
          goal = expected_prod[i]
          current_time = time[i]

          res['actual'] = actual
          res['goal'] = goal
          res['time'] = current_time

      print(res)
        
