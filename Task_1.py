import requests

def get_hero_intelligence(hero_name, hero_list):
    response = requests.get(f'https://www.superheroapi.com/api.php/1565665036954012/search/{hero_name}')
    intelligence = response.json()['results'][0]['powerstats']['intelligence']
    hero_list.append([hero_name, int(intelligence)])

def by_int(item):
    return item[1]

hero_list = []

get_hero_intelligence('Hulk', hero_list)
get_hero_intelligence('Thanos', hero_list)
get_hero_intelligence('Captain America', hero_list)

most_intelligent_hero = max(hero_list, key=by_int)
print(f'Самый умный герой: {most_intelligent_hero[0]}. Его интеллект равен {most_intelligent_hero[1]}')