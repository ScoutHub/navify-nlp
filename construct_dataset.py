import pandas as pd
from langdetect import detect
import json
import random
from unidecode import unidecode
import re

def load_json_data(path: str) -> list[str]:
    with open(path, 'r') as file:
        data = json.load(file)
    city_data = [item['label'] for item in data["cities"]]
    return city_data

def generate_trip_phrase(villes):
    ville_depart = random.choice(villes).lower()
    ville_arrivee = random.choice(villes).lower()

    while ville_arrivee == ville_depart:
        ville_arrivee = random.choice(villes).lower()
    phrases = [
        f"Je veux aller de {ville_depart} à {ville_arrivee}.",
        f"Je suis à {ville_depart} et j'aimerais aller à {ville_arrivee}.",
        f"Je suis à {ville_depart} et j'aimerais me rendre à {ville_arrivee}.",
        f"J'aimerais me rendre à {ville_arrivee} depuis {ville_depart}.",
        f"Je veux aller à {ville_arrivee} depuis {ville_depart}.",
        f"Je suis à {ville_arrivee} et je veux aller à {ville_depart}.",
        f"Je voudrais aller à {ville_depart} depuis {ville_arrivee}.",
        f"Comment me rendre à {ville_arrivee} depuis {ville_depart} ?",
        f"Y a-t-il des trains de {ville_depart} à {ville_arrivee} ?",
        f"Je prévois de voyager de {ville_depart} à {ville_arrivee} demain.",
        f"J'aimerai aller à {ville_arrivee} depuis {ville_depart}.",
        f"Je veux voyager à {ville_arrivee} de {ville_depart}.",
        f"Quel est le trajet de {ville_depart} à {ville_arrivee} ?",
        f"Voyage de {ville_depart} jusqu'à {ville_arrivee}.",
        f"Je veux me déplacer de {ville_depart} à {ville_arrivee}.",
        f"Je pars de {ville_depart} en direction de {ville_arrivee}.",
        f"Je veux partir de {ville_depart} en direction de {ville_arrivee}.",
        f"Comment rejoindre {ville_arrivee} à partir de {ville_depart} ?",
        f"Comment partir de {ville_depart} à {ville_arrivee} ?",
        f"Comment partir depuis {ville_depart} à {ville_arrivee} ?",
        f"Je planifie un voyage entre {ville_depart} et {ville_arrivee}.",
        f"Je veux un train entre {ville_depart} et {ville_arrivee}.",
        f"Je suis à {ville_arrivee} et je retourne à {ville_depart} demain.",
        f"Je veux faire un trajet de {ville_depart} à {ville_arrivee}.",
    ]
    phrase = random.choice(phrases).lower()
    phrase = unidecode(phrase)
    phrase = re.sub(r'[^\w\s]', '', phrase)
    return phrase, ville_depart, ville_arrivee

def generate_incomplete_phrase(villes):
    ville_depart = random.choice(villes).lower()
    ville_arrivee = random.choice(villes).lower()

    while ville_arrivee == ville_depart:
        ville_arrivee = random.choice(villes).lower()
    phrases = [
        f"Quel temps fait-il à {ville_depart} ?",
        f"Je suis à {ville_depart}, quel temps fait-il à {ville_arrivee} ?",
        f"Il pleut à {ville_depart} en ce moment",
        f"Je suis à {ville_arrivee} et j'aimerais faire du shopping à {ville_arrivee}",
        f"{ville_arrivee} est une très belle ville",
        f"La culture de {ville_arrivee} est meilleure que celle de {ville_depart}",
        f"Je préfère {ville_arrivee} à {ville_depart}",
        f"Je me suis amusé à {ville_arrivee}, mais je préfère {ville_depart}",
        f"Je ne pourrais pas vivre dans une ville comme {ville_depart}",
        f"Je ne pourrais pas vivre dans une ville comme {ville_depart}, je préfère {ville_arrivee}",
        f"La gastronomie de {ville_arrivee} est superbe",
        f"Il fait chaud à {ville_depart}, mais froid à {ville_arrivee}",
        f"Je rêve de visiter {ville_arrivee} un jour",
        f"Les habitants de {ville_depart} sont très accueillants",
        f"Les paysages autour de {ville_arrivee} sont incroyables",
        f"{ville_depart} est connue pour son architecture unique",
        f"Les musées de {ville_arrivee} sont incontournables",
        f"Le marché de {ville_depart} est très animé le week-end",
        f"La vie nocturne de {ville_arrivee} est impressionnante",
        f"Je me demande si la plage de {ville_arrivee} est belle",
        f"Le coût de la vie à {ville_depart} est plus élevé qu'à {ville_arrivee}",
        f"J'ai entendu dire que {ville_arrivee} organise un grand festival chaque année",
        f"Les rues de {ville_depart} sont toujours pleines de vie",
        f"{ville_arrivee} est célèbre pour sa cuisine locale",
        f"Je me souviens d'un excellent restaurant à {ville_depart}",
        f"Les parcs à {ville_arrivee} sont parfaits pour une promenade",
        f"{ville_depart} a une riche histoire à découvrir",
        f"Le climat à {ville_arrivee} est plus agréable qu'à {ville_depart}",
        f"J'aimerais goûter aux spécialités culinaires de {ville_arrivee}",
        f"Les gens de {ville_depart} sont très chaleureux",
        f"{ville_arrivee} est une destination touristique populaire",
        f"J'aimerais en savoir plus sur la culture locale de {ville_arrivee}",
        f"Les festivals à {ville_depart} sont toujours incroyables",
        f"Je trouve l'architecture de {ville_arrivee} fascinante",
        f"{ville_depart} est connue pour sa scène musicale vibrante",
        f"Je pense que les transports publics à {ville_arrivee} sont très efficaces",
        f"Les couchers de soleil à {ville_depart} sont magnifiques",
        f"Je ne sais pas si {ville_arrivee} est plus chère que {ville_depart}",
        f"Les rues pavées de {ville_arrivee} sont charmantes",
        f"J'adore les petites boutiques à {ville_depart}",
        f"Les plages à {ville_arrivee} sont incroyables en été",
        f"{ville_depart} est parfaite pour un week-end tranquille",
        f"Le centre-ville de {ville_arrivee} est très animé",
        f"{ville_arrivee} a une ambiance très cosmopolite",
        f"Je voudrais voir les monuments historiques de {ville_depart}",
        f"La scène artistique de {ville_arrivee} est impressionnante",
        f"Les cafés à {ville_depart} sont toujours très accueillants",
        f"Je ne savais pas que {ville_arrivee} avait tant d'attractions",
        f"Les traditions de {ville_depart} sont fascinantes",
        f"{ville_arrivee} est célèbre pour son carnaval annuel",
        f"Je préfère {ville_arrivee} à {ville_depart}",
        f"{ville_arrivee} et {ville_depart} sont de belles villes.",
        f"Je me suis amusé à {ville_arrivee}, mais je préfère {ville_depart}",
        f"Je ne pourrais pas vivre dans une ville comme {ville_depart}",
        f"Je ne pourrais pas vivre dans une ville comme {ville_depart}, je préfère {ville_arrivee}",
        f"La gastronomie de {ville_arrivee} est superbe",
        f"Il fait chaud à {ville_depart}, mais froid à {ville_arrivee}",
        f"Les rues de {ville_depart} sont magnifiques, mais celles de {ville_arrivee} sont plus modernes",
        f"J'ai quitté {ville_depart} pour visiter {ville_arrivee} aujourd'hui",
        f"Je trouve les habitants de {ville_depart} plus accueillants que ceux de {ville_arrivee}",
        f"Les paysages autour de {ville_arrivee} sont plus variés qu'à {ville_depart}",
        f"Je suis à {ville_arrivee}, mais je pense souvent à {ville_depart}",
        f"{ville_depart} est plus calme que {ville_arrivee}",
        f"J'aimerais combiner le charme de {ville_depart} et l'énergie de {ville_arrivee}",
        f"Je vais faire mes courses à {ville_arrivee}, mais je préfère le marché de {ville_depart}",
        f"{ville_arrivee} est plus animée que {ville_depart}",
        f"Je pense que {ville_depart} est plus propice à une vie tranquille que {ville_arrivee}",
        f"La vie à {ville_depart} est très différente de celle à {ville_arrivee}",
        f"Les spécialités culinaires de {ville_arrivee} surpassent celles de {ville_depart}",
        f"Les habitants de {ville_depart} sont plus chaleureux que ceux de {ville_arrivee}",
        f"J'aime visiter {ville_arrivee}, mais je préfère rentrer à {ville_depart}",
        f"Les musées de {ville_depart} sont tout aussi fascinants que ceux de {ville_arrivee}",
        f"Je trouve l'architecture de {ville_depart} plus authentique que celle de {ville_arrivee}",
        f"Le climat à {ville_arrivee} est très différent de celui à {ville_depart}",
        f"Je préfère la plage de {ville_arrivee} à celle de {ville_depart}",
        f"Je suis à {ville_arrivee} pour le week-end, mais j'habite à {ville_depart}",
        f"Je rêve de combiner la tranquillité de {ville_depart} et l'effervescence de {ville_arrivee}",
        f"Le coût de la vie à {ville_depart} est plus abordable qu'à {ville_arrivee}",
        f"Je me suis bien amusé à {ville_arrivee}, mais rien ne vaut {ville_depart}",
        f"J'ai découvert que les traditions de {ville_depart} sont différentes de celles de {ville_arrivee}",
        f"Les marchés de {ville_arrivee} sont plus diversifiés que ceux de {ville_depart}",
        f"{ville_depart} est connue pour ses festivals, mais {ville_arrivee} est célèbre pour son carnaval",
        f"Je suis parti de {ville_depart} pour voir les attractions touristiques de {ville_arrivee}",
        f"Les transports publics à {ville_arrivee} sont plus efficaces qu'à {ville_depart}",
        f"Les rues de {ville_depart} sont moins bondées que celles de {ville_arrivee}",
        f"J'ai adoré visiter {ville_arrivee}, mais ma ville préférée reste {ville_depart}",
        f"Les couchers de soleil à {ville_depart} sont différents de ceux à {ville_arrivee}",
        f"Les deux villes, {ville_depart} et {ville_arrivee}, ont leur charme unique",
        f"Je voudrais revenir à {ville_depart} après mon séjour à {ville_arrivee}",
        f"{ville_depart} est une ville historique, tandis que {ville_arrivee} est plus moderne",
        f"J'ai quitté {ville_depart} pour explorer les attractions de {ville_arrivee}",
        f"Je préfère le style de vie de {ville_arrivee} à celui de {ville_depart}",
        f"Les événements culturels à {ville_arrivee} sont très différents de ceux à {ville_depart}",
        f"Je trouve la vie nocturne de {ville_arrivee} plus intéressante que celle de {ville_depart}",
        f"Je suis venu de {ville_depart} pour profiter de l'atmosphère animée de {ville_arrivee}"
    ]

    phrase = random.choice(phrases).lower()
    phrase = unidecode(phrase)
    phrase = re.sub(r'[^\w\s]', '', phrase)
    return phrase,  ville_depart, ville_arrivee


def generate_trip_phrase_with_intermediate(villes):
    ville_depart = random.choice(villes).lower()
    ville_arrivee = random.choice(villes).lower()
    
    while ville_arrivee == ville_depart:
        ville_arrivee = random.choice(villes).lower()

    nb_detour = random.randint(1, 5)
    villes_detour = []

    for _ in range(nb_detour):
        random_detour = random.choice(villes)
        while(random == ville_arrivee or random == ville_depart):
            random_detour = random.choice(villes)
        villes_detour.append(random_detour.lower())

    phrases = [
        f"Je veux aller de {ville_depart} à {ville_arrivee} en passant par #.",
        f"Je suis à {ville_depart} et j'aimerais aller à {ville_arrivee} en passant par #.",
        f"Je suis à {ville_depart} et j'aimerais me rendre à {ville_arrivee} en passant par #.",
        f"Comment me rendre à {ville_arrivee} depuis {ville_depart} en passant par #?",
        f"Y a-t-il des trains de {ville_depart} à {ville_arrivee} en passant par # ?",
        f"Je prévois de voyager de {ville_depart} à {ville_arrivee} en coupant par #",
        f"J'aimerai aller à {ville_arrivee} depuis {ville_depart} en passant par #",
        f"Je veux voyager à {ville_arrivee} de {ville_depart} en faisant un détour par #",
        f"Je veux aller à {ville_arrivee} depuis {ville_depart} en passant par #.",
        f"Je suis à {ville_arrivee} et je veux aller à {ville_depart} en passant par #.",
        f"En passant par #, je veux aller de {ville_depart} à {ville_arrivee}.",
        f"En passant par #, comment me rendre à {ville_arrivee} depuis {ville_depart} ?",
        f"En passant par #, y a-t-il des trains de {ville_depart} à {ville_arrivee} ?",
        f"En passant par #, je prévois de voyager de {ville_depart} à {ville_arrivee}.",
        f"En passant par #, j'aimerai aller à {ville_arrivee} depuis {ville_depart}.",
        f"En faisant un détour par #, je veux voyager à {ville_arrivee} de {ville_depart}.",
        f"En passant par #, je veux aller à {ville_arrivee} depuis {ville_depart}.",
    ]
    
    random_phrase = random.choice(phrases)

    last_index = random_phrase.find("#")
    begin = random_phrase[:last_index]
    end = random_phrase[last_index:].replace("#", "")

    for i in range(len(villes_detour)):
        if(i == len(villes_detour) - 1):
            begin += f'{villes_detour[i]}'
        elif(i == len(villes_detour) - 2):
            begin += f'{villes_detour[i]} et '
        else:
            begin += f'{villes_detour[i]}, '

    detours = ','.join(villes_detour)

    random_phrase = (begin + end).lower()
    random_phrase = unidecode(random_phrase)
    random_phrase = re.sub(r'[^\w\s]', '', random_phrase)
    return random_phrase, ville_depart, ville_arrivee, detours

def generate_ds(file_path: str, villes, n: int, with_detour = False):
    print(f'[INFO]: Generating dataset...')
    data = []

    for _ in range(n):
        phrase, origine, destination = generate_trip_phrase(villes)
        data.append((phrase, origine, destination, None, 1))
    
    if with_detour:
        for _ in range(n // 2):
            phrase, origine, destination, detours = generate_trip_phrase_with_intermediate(villes)
            data.append((phrase, origine, destination, detours, 1))
    
    else:
        for _ in range(n):
            phrase, origine, destination = generate_incomplete_phrase(villes)
            data.append((phrase, origine, destination, None, 0))

    df = pd.DataFrame(data, columns=['text', 'origin', 'destination', 'detours', "is_trip"])
    df.to_csv(f'datasets/{file_path}', ";")
    print(f'[SUCCESS]: Dataset generated in path datasets/{file_path}')

if __name__ == "__main__":
    villes = load_json_data("assets/cities.json")

    generate_ds('bert_ds.csv', villes, 3000)
    generate_ds('bert_ds_val.csv', villes, 5)
    generate_ds(file_path='spacy_ds.csv', villes=villes, n=5000, with_detour=True)
