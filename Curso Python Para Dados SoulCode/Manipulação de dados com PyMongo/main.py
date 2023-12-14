from pymongo import collection


def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://brunnomanducarfe:9gwEIK6UiJycfsO9@mydatabase.pfsyul3.mongodb.net/"

    client = MongoClient(CONNECTION_STRING)

    print("Conectado com sucesso!")

    return client['sample_airbnb']


get_database()
