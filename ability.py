import json,requests
def ability(name_pokemon):
    req=requests.get('http://pokeapi.co/api/v2/pokemon/'+name_pokemon)
    json_response=json.loads(req.text)
    result=[]
    for i in json_response['abilities']:
        result.append((i['ability']['name']))
    return result
