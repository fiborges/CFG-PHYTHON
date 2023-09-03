import requests
import json
import csv

# Fazer uma solicitação à API para obter dados de personagens
url = 'https://hp-api.onrender.com/api/characters'
response = requests.get(url)
characters = json.loads(response.text)

# Nome do arquivo CSV para salvar os dados
csv_file = 'harry_potter_characters.csv'

character_ranking = {
    'Harry Potter': 9,
    'Hermione Granger': 9,
    'Ron Weasley': 9,
    'Draco Malfoy': 8,
    'Minerva McGonagall': 10,
    'Cedric Diggory': 8,
    'Cho Chang': 7,
    'Severus Snape': 9,
    'Rubeus Hagrid': 7,
    'Neville Longbottom': 8,
    'Luna Lovegood': 7,
    'Ginny Weasley': 8,
    'Sirius Black': 9,
    'Remus Lupin': 9,
    'Arthur Weasley': 7,
    'Bellatrix Lestrange': 9,
    'Lord Voldemort': 12,
    'Horace Slughorn': 8,
    'Dolores Umbridge': 7,
    'Lucius Malfoy': 8,
    'Vincent Crabbe': 6,
    'Gregory Goyle': 6,
    'Lily Potter': 8,
    'James Potter': 8,
    'Albus Dumbledore': 12,
    'Newt Scamander': 8,
    'Molly Weasley': 8,
    'Percy Weasley': 7,
    'Fred Weasley': 7,
    'George Weasley': 7,
    'Lee Jordan': 7,
    'Bill Weasley': 8,
    'Charlie Weasley': 8,
    'Fat Friar': 6,
    'Hannah Abbott': 7,
    'Susan Bones': 7,
    'Terry Boot': 6,
    'Mandy Brocklehurst': 6,
    'Lavender Brown': 6,
    'Millicent Bulstrode': 6,
    'Justin Finch-Fletchley': 7,
    'Seamus Finnegan': 7,
    'Theodore Nott': 6,
    'Pansy Parkinson': 6,
    'Parvati Patil': 6,
    'Padma Patil': 6,
    'Lisa Turpin': 6,
    'Blaise Zabini': 6,
    'Nearly Headless Nick': 7,
    'Bloody Baron': 7,
    'Pomona Sprout': 7,
    'Filius Flitwick': 6,
    'Angelina Johnson': 6,
    'Marcus Flint': 6,
    'Alicia Spinnet': 6,
    'Katie Bell': 6,
    'Adrian Pucey': 6,
    'Miles Bletchley': 6,
    'Terrence Higgs': 6,
    'Celestina Warbeck': 7,
    'Colin Creevey': 6,
    'Moaning Myrtle': 7,
    'Milicent Bullstroude': 6,
    'Ernie Macmillan': 7,
    'Penelope Clearwater': 6,
    'Peter Pettigrew': 6,
    'Cassius Warrington': 6,
    'Graham Montague': 6,
    'Peregrine Derrick': 6,
    'Lucian Bole': 6,
    'Walden Macnair': 6,
    'Stewart Ackerley': 6,
    'Malcolm Baddock': 6,
    'Eleanor Branstone': 7,
    'Owen Cauldwell': 7,
    'Laura Madley': 7,
    'Natalie McDonald': 6,
    'Graham Pritchard': 6,
    'Orla Quirke': 6,
    'Kevin Whitby': 7,
    'Eloise Midgen': 7,
    'Fawcett': 6,
    'Summers': 7,
    'Stebbins': 6,
    'Evan Rosier': 6,
    'Wilkes': 6,
    'Avery': 6,
    'Mulciber': 6,
    'Nymphadora Tonks': 7,
    'Alphard Black': 6,
    'Regulus Black': 6,
    'Phineas Nigelus Black': 6,
    'Araminta Meliflua Black': 6,
    'Andromeda Tonks': 7,
    'Rodolphus Lestrange': 6,
    'Rabastan Lestrange': 6,
    'Aberforth Dumbledore': 7,
    'Anthony Goldstein': 6,
    'Euan Abercrombie': 7,
    'Rose Zeller': 7,
    'Kenneth Towler': 6,
    'Vicky Frobisher': 6,
    'Geoffrey Hooper': 6,
    'Michael Corner': 6,
    'Zacharias Smith': 6,
    'Andrew Kirke': 6,
    'Jack Sloper': 6,
    'Summerby': 7,
    'Marietta Edgecombe': 6,
    'Bradley': 6,
    'Roger Davies': 6,
    'Eddie Carmichael': 6,
    'Daphne Greengrass': 6,
    'Romilda Vane': 6,
    'Cormac McLaggen': 6,
    'Marcus Belby': 6,
    'Demelza Robins': 6,
    'Jimmy Peakes': 6,
    'Ritchie Coote': 6,
    'Leanne': 6,
    'Vaisey': 6,
    'Harper': 6,
    'Urquhart': 6,
    'Cadwallader': 6,
    'Amycus Carrow': 6,
    'Alecto Carrow': 6,
    'Xenophilius Lovegood': 6,
    'Scabior': 6,
    'Ted Lupin': 6,
    'Lily Potter': 8,
    'James Potter': 8,
    'Albus Severus Potter': 6,
    'Rose Weasley': 6,
    'Scorpius Malfoy': 6
}

# Escrever os dados em um arquivo CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escrever o cabeçalho do arquivo CSV
    writer.writerow(['Name', 'Species', 'House', 'Power'])

    # Escrever os dados de cada personagem no arquivo CSV
    for character in characters:
        name = character.get('name', '')
        species = character.get('species', '')
        house = character.get('house', '')
        power = character_ranking.get(name, '')  # Obtém a classificação do dicionário de classificação

        # Verificar se há uma casa associada (não vazia)
        if house:
            writer.writerow([name, species, house, power])

print(f'Dados dos personagens salvos em {csv_file}')


url = 'https://hp-api.onrender.com/api/spells'
response = requests.get(url)
spells = json.loads(response.text)

# Nome do arquivo CSV para salvar os dados dos feitiços
csv_file = 'harry_potter_spells.csv'

# Definir um dicionário de classificação de feitiços (você pode personalizar isso)
spell_ranking = {
    'Aberto': 2,
    'Accio': 3,
    'Aguamenti': 2,
    'Alohomora': 4,
    'Anapneo': 2,
    'Aparecium': 1,
    'Apparate': 4,
    'Ascendio': 3,
    'Avada Kedavra': 10,
    'Avis': 2,
    'Bat': 1,
    'Bombardo': 4,
    'Brackium Emendo': 2,
    'Capacious Extremis': 5,
    'Confundo': 3,
    'Conjunctivitis Curse': 4,
    'Crinus Muto': 2,
    'Crucio': 9,
    'Diffindo': 3,
    'Disillusionment Charm': 4,
    'Disapparate': 5,
    'Engorgio': 3,
    'Episkey': 2,
    'Expecto patronum': 7,
    'Erecto': 3,
    'Evanesco': 2,
    'Expelliarmus': 6,
    'Ferula': 3,
    'Fidelius Charm': 7,
    'Fiendfyre Curse': 9,
    'Finite Incantatem': 4,
    'Furnunculus Curse': 2,
    'Geminio': 3,
    'Glisseo': 2,
    'Homenum Revelio': 4,
    'Homonculus Charm': 5,
    'Immobulus': 3,
    'Impedimenta': 3,
    'Incarcerous': 4,
    'Imperio': 8,
    'Impervius': 3,
    'Incendio': 4,
    'Langlock': 2,
    'Legilimens': 6,
    'Levicorpus': 3,
    'Locomotor Mortis': 3,
    'Lumos': 2,
    'Morsmordre': 7,
    'Mucus Ad Nauseam': 2,
    'Muffliato': 3,
    'Nox': 2,
    'Obliviate': 5,
    'Obscuro': 3,
    'Oculus Reparo': 3,
    'Oppugno': 3,
    'Petrificus Totalus': 4,
    'Periculum': 3,
    'Piertotum Locomotor': 5,
    'Protean Charm': 4,
    'Protego': 6,
    'Reducto': 4,
    'Reducio': 3,
    'Renneverate': 3,
    'Reparifors': 4,
    'Reparo': 3,
    'Rictusempra': 3,
    'Riddikulus': 5,
    'Scourgify': 3,
    'Sectumsempra': 7,
    'Serpensortia': 4,
    'Silencio': 3,
    'Sonorus': 3,
    'Spongify': 2,
    'Stupefy': 6,
    'Tarantallegra': 4,
    'Unbreakable Vow': 8,
    'Wingardium Leviosa': 4,
}


# Escrever os dados em um arquivo CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escrever o cabeçalho do arquivo CSV
    writer.writerow(['Name', 'Description', 'Rank'])

    # Escrever os dados de cada feitiço no arquivo CSV
    for spell in spells:
        name = spell.get('name', '')
        description = spell.get('description', '')
        rank = spell_ranking.get(name, '')  # Obtém a classificação do dicionário de classificação
        writer.writerow([name, description, rank])

print(f'Dados dos feitiços salvos em {csv_file}')