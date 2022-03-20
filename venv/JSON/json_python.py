# Read a json file
# JSON -> Javascript Object Notation
import json
import urllib.request
"""
note: if we do not add a fake user agent will get an error 
https://gitlab.com/gitlab-org/gitlab/-/issues/219669
 Dalton Durst @UniversalSuperBox
It appears that this is a CloudFlare error, it is set up to block the urllib user agent.
When attempting the urlopen() call normally
CloudFlare is the only plausible source of this error I could find: https://support.cloudflare.com/hc/en-us/articles/360029779472-Troubleshooting-Cloudflare-1XXX-errors#error1010
The default urllib User-Agent is Python-urllib/3.6 (Replacing 3.6 with whichever Python version is appropriate)
"""
req = urllib.request.Request("https://globalmentoring.com.mx/api/personas.json", headers={"User-Agent": "Chrome"})
res = urllib.request.urlopen(req)
print(res.code)
print(res)
"""
200
<http.client.HTTPResponse object at 0x7fcdbbea7d30>
"""
body_response = res.read()
print(body_response)
"""
b'{"personas":[{"nombre": "Juan Perez", "edad": "28"},{"nombre": "Karla Gomez", "edad": "32"},{"nombre": 
"Carlos Lara", "edad": "35"},{"nombre": "Mar\xc3\xada Esparza", "edad": "22"},{"nombre": 
"Pedro Santos", "edad": "40"}], "total": 5, "mensaje": "exitoso"}'

"""

# that was information the type binary this the reason of b at the beginning
# we need transform this data to JSON correctly
json_response = json.loads(body_response.decode('utf-8'))
print(json_response)
"""
{'personas': [{'nombre': 'Juan Perez', 'edad': '28'}, {'nombre': 'Karla Gomez', 'edad': '32'}, {'nombre': 
'Carlos Lara', 'edad': '35'}, {'nombre': 'María Esparza', 'edad': '22'}, {'nombre':
 'Pedro Santos', 'edad': '40'}], 'total': 5, 'mensaje': 'exitoso'}
"""

# print the name of the person
# convert json to list and dictionaries
for person in json_response['personas']:
    print(f'Person: {person["nombre"]} {person["edad"]}')

"""
Person: Juan Perez 28
Person: Karla Gomez 32
Person: Carlos Lara 35
Person: María Esparza 22
Person: Pedro Santos 40
"""

# access to independent variables
print(f'Total of persons: {json_response["total"]}')
"""
Total of persons: 5
"""

# access to message
print(f'Total of persons: {json_response["mensaje"]}')
"""
Total of persons: exitoso
"""