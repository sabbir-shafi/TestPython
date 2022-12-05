import requests
import csv

HOST = "http://localhost:8080"

singlePersonInsert = HOST + "/calculator/insert"
multiplePersonInsert = HOST + "/calculator/insertMultiple"
uploadFromJSON = HOST + "/calculator/uploadLargeFileForInsertionToDatabase"
ClearDataBase = HOST + "/calculator/rakeDatabase"

taxRelief = HOST + "/calculator/taxRelief"
taxReliefSummary = HOST + "/calculator/taxReliefSummary"

birthday = ""
gender = ""
name = ""
natid = ""
salary = ""
tax = ""


def checkAssettion(response, compare):
    if response == compare:
        print("assertion passed")
    else:
        print("assertion failed")


def takeHeroInput():
    singleObj = {
        "birthday": "",
        "gender": "",
        "name": "",
        "natid": "",
        "salary": "",
        "tax": ""
    }

    birthday = input("insert birthday (in FORMAT DDMMYYYY)\n")
    gender = input("insert gender \n")
    name = input("insert name\n")
    natid = input("insert natid(numeric)\n")
    salary = input("insert salary (numeric)\n")
    tax = input("insert tax(numeric)\n")

    singleObj["birthday"] = birthday
    singleObj["gender"] = gender
    singleObj["name"] = name
    singleObj["natid"] = natid
    singleObj["salary"] = salary
    singleObj["tax"] = tax

    return singleObj


userSelection = int(input("Please select user role:\n1.Use as a Clerk\n2.Use as Bookkeeper\n3.Use as Governor\n"))

if userSelection == 1:
    inputSelection = int(
        input("Choose one from bellow:\n1.Insert single\n2.Insert Multiple\n3.Insert CSV file\n4.Clear data base\n"))

    if inputSelection == 1:
        jsonObj = takeHeroInput()
        response = requests.post(singlePersonInsert, json=jsonObj)
        checkAssettion(int(response.status_code),202)

    elif inputSelection == 2:
        count = int(input("How many inserts do you want?\n"))
        dic = []
        for i in range(count):
            jsonObj = takeHeroInput()
            dic.append(jsonObj)
        response = requests.post(multiplePersonInsert, json=dic)
        checkAssettion(int(response.status_code), 202)

    elif inputSelection == 3:
        headers = {'Content-Type': 'multipart/form-data', 'accept': '*/*'}
        with open('data.csv', 'r') as f:
            response = requests.post(uploadFromJSON, headers, files={'file': ('data.csv', f, 'text/csv')})
            checkAssettion(int(response.status_code), 200)
    elif inputSelection == 4:
        response = requests.post(ClearDataBase)
        checkAssettion(int(response.status_code), 200)

elif userSelection == 2:
    response = requests.get(taxRelief)
    print(response.content)
    checkAssettion(int(response.status_code), 200)

elif userSelection == 3:
    response = requests.get(taxReliefSummary)
    print(response.content)
    checkAssettion(int(response.status_code), 200)