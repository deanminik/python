import json
import urllib.request

req = urllib.request.Request("https://globalmentoring.com.mx/api/clima.json", headers={"User-Agent": "Chrome"})
res = urllib.request.urlopen(req)

print(res.code)
print(res)
"""
200
<http.client.HTTPResponse object at 0x7f9c788596d0>
"""

body_response = res.read()
print(body_response)
"""
b'{"clima":[{"principal":"Con nubes","descripcion":"Pocas nubes"}],"principal":{"temp":18,"sensacion":16,"temp_min":11,"temp_max":23},"id":2345612}'
"""
json_response = json.loads(body_response.decode('utf-8'))
print(json_response)

"""
{'clima': [{'principal': 'Con nubes', 'descripcion': 'Pocas nubes'}], 'principal': {'temp': 18, 'sensacion': 16, 'temp_min': 11, 'temp_max': 23}, 'id': 2345612}
"""

# access to the description
#pocas nubes
descrip = json_response.get('clima')
print(descrip)
"""
[{'principal': 'Con nubes', 'descripcion': 'Pocas nubes'}]
"""
descrip = json_response.get('clima')[0]
print(descrip)
""" we are inside of the list
{'principal': 'Con nubes', 'descripcion': 'Pocas nubes'}
"""
descrip = json_response.get('clima')[0].get('descripcion')
print(descrip)
"""
Pocas nubes
"""

# show the temperture min and max
tem_min = json_response.get('principal').get('temp_min')
print(tem_min)
"""
11
"""

tem_max = json_response.get('principal').get('temp_max')
print(tem_max)
"""
23
"""