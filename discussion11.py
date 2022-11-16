import unittest
import sqlite3
import json
import os
# starter code

# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


# Creates list of species ID's and numbers
def create_species_table(cur, conn):

    species = ["Rabbit",
    "Dog",
    "Cat",
    "Boa Constrictor",
    "Chinchilla",
    "Hamster",
    "Cobra",
    "Parrot",
    "Shark",
    "Goldfish",
    "Gerbil",
    "Llama",
    "Hare"
    ]

    cur.execute("DROP TABLE IF EXISTS Species")
    cur.execute("CREATE TABLE Species (id INTEGER PRIMARY KEY, title TEXT)")
    for i in range(len(species)):
        cur.execute("INSERT INTO Species (id,title) VALUES (?,?)",(i,species[i]))
    conn.commit()

# TASK 1
# CREATE TABLE FOR PATIENTS IN DATABASE
def create_patients_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Patients")
    cur.execute("CREATE TABLE Patients (pet_id INTEGER, name STRING, species_id NUMBER, age INTEGER, cuteness INTEGER, aggressiveness NUMBER)")
    


# ADD FLUFFLE TO THE TABLE
def add_fluffle(cur, conn):
    cur.execute("INSERT INTO Patients (pet_id,name,species_id,age,cuteness,aggressiveness) VALUES (?,?,?,?,?,?)",(0,"Fluffle",0,3,90,100))
    conn.commit()
    

# TASK 2
# CODE TO ADD JSON TO THE TABLE
# ASSUME TABLE ALREADY EXISTS
def add_pets_from_json(filename, cur, conn):
    
    # WE GAVE YOU THIS TO READ IN DATA
    f = open(filename)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)

    # THE REST IS UP TO YOU
    
    for i in range(len(json_data)):
        if json_data[i]["species"] == "Rabbit":
            json_data[i]["species"] = 0
        elif json_data[i]["species"] == "Dog":
            json_data[i]["species"] = 1
        elif json_data[i]["species"] == "Cat":
            json_data[i]["species"] = 2
        elif json_data[i]["species"] == "Boa Constrictor":
            json_data[i]["species"] = 3
        elif json_data[i]["species"] == "Chinchilla":
            json_data[i]["species"] = 4
        elif json_data[i]["species"] == "Hamster":
            json_data[i]["species"] = 5
        elif json_data[i]["species"] == "Cobra":
            json_data[i]["species"] = 6
        elif json_data[i]["species"] == "Parrot":
            json_data[i]["species"] = 7
        elif json_data[i]["species"] == "Shark":
            json_data[i]["species"] = 8
        elif json_data[i]["species"] == "Goldfish":
            json_data[i]["species"] = 9
        elif json_data[i]["species"] == "Gerbil":
            json_data[i]["species"] = 10
        elif json_data[i]["species"] == "Llama":
            json_data[i]["species"] = 11
        elif json_data[i]["species"] == "Hare":
            json_data[i]["species"] = 12

        cur.execute("INSERT INTO Patients (pet_id,name,species_id,age,cuteness,aggressiveness) VALUES (?,?,?,?,?,?)",(i+1,json_data[i]["name"],json_data[i]["species"],json_data[i]["age"],json_data[i]["cuteness"],json_data[i]["aggressiveness"]))
    conn.commit()




# TASK 3
# CODE TO OUTPUT NON-AGGRESSIVE PETS
def non_aggressive_pets(aggressiveness, cur, conn):
    cur.execute("SELECT name FROM Patients WHERE aggressiveness<="+ str(aggressiveness))
    conn.commit()
    result = cur.fetchall()
    return result






def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('animal_hospital.db')
    create_species_table(cur, conn)

    create_patients_table(cur, conn)
    add_fluffle(cur, conn)
    add_pets_from_json('pets.json', cur, conn)
    ls = (non_aggressive_pets(10, cur, conn))
    print(ls)
    
    
if __name__ == "__main__":
    main()

