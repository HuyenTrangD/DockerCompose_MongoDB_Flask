"""
Exemple de commnunication avec une base mongo DB
Lexique:
* Base de données <=> database
* Table <=> collection
* row <=> document
"""
# import de mes librairies
from pymongo import MongoClient

# info de ma db
host = 'localhost'
port = 27017

# création du client de connexion
client = MongoClient(host=host, port=port)

# récupération de ma db
mabdd = client.demo

print(type(mabdd))
print(mabdd)

# récupération d"une collection
col = mabdd.users

print("ma collection_type :\n",type(col))
print("ma collection :\n", col)

# ajout des datas dans ma bdd => format JSON
new_data = {
    'titre':'Docteur',
    'superpouvoir':'chiant',
    'pointure': 42
}
# insertion de mon document en json
reponse_new_id = col.insert_one(new_data)
# récupération de l'id à partir de l'objet ID
new_id = str(reponse_new_id.inserted_id)
# attribution de son id à la nouvelle data enregistrée
new_data["_id"] = new_id
print("enregistrement du user : \n", new_data)

# récupération de tous les users de ma collection
mes_users = col.find()
print("ensemble de mes users :\n", list(mes_users))