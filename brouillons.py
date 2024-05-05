import pandas as pd

# Charger les bases de données
dataset = pd.read_csv('dataset_m.csv', delimiter=',', quotechar='"')
datasetsupplement = pd.read_csv('dataset_supplement.csv', delimiter=',', quotechar='"')

# Fonction pour extraire les modalités d'un attribut complexe
def extraire_modalites(row, variable, attribut):
    elements = eval(row[variable])
    modalites = set()
    for element in elements:
        if attribut in element:
            modalites.add(element[attribut])
    return len(modalites)  # Retourne le nombre de modalités

# Liste des variables complexes à traiter et des attributs à considérer
attributs_actors = ['gender']
attributs_production_crew = ['department', 'gender']

# Ajouter une colonne avec le nombre de modalités par attribut
for attribut in attributs_production_crew:
    datasetsupplement['Nb_modalite_production_crew_' + attribut] = datasetsupplement.apply(lambda x: extraire_modalites(x, 'production_crew', attribut), axis=1)

for attribut in attributs_actors:
    datasetsupplement['Nb_modalite_actors_' + attribut] = datasetsupplement.apply(lambda x: extraire_modalites(x, 'actors', attribut), axis=1)

# Sauvegarder la nouvelle base de données
datasetsupplement.to_csv('datasetsupplement_new.csv', index=False)
