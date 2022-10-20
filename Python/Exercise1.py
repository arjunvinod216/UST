# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:55:35 2022

@author: arjun
"""

from pymongo import MongoClient
import pandas as pd
import json
import numpy as np

def mongoimport(csv_path):
    hr_df = pd.read_csv(csv_path)
    payload = json.loads(hr_df.to_json(orient = 'records'))
    
    collection.delete_many({})
    
    collection.insert_many(payload)
    
    
if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    
    db = client['HRdatabase1']
    
    collection = db['EmpCollection']
    
    mongoimport('C:/Users/arjun/Downloads/HR-Employee-Attrition.csv')

    # 1
    allDocuments = collection.aggregate([
        {'$group':{'_id' : '$Department', 'total_counts':{'$count':{}}}},
        {'$sort' : {'total_counts':-1}},
        ])
    
    for item in allDocuments:
        print(item)
        
    # 2. 
    print("Top hired employee is from which education fields: ")
    allDocuments = collection.aggregate([
        {'$group':{'_id' : '$EducationField', 'total_counts':{'$count':{}}}},
        {'$sort' : {'total_counts':-1}},
        {'$limit':1}
        ])
    
    for item in allDocuments:
        print(item)
        
    # 3. 
    min_maxsalary = collection.aggregate([
        {'$group' : {'_id' : 'null', 'max salary':{ '$max' : '$MonthlyIncome'}, 
                     'min salary' : {'$min':'$MonthlyIncome'}}}, {'$project' : {'_id' : 0}}])
        
   
    
    # 4. 
    print('Find the AVG Monthly Income of overall employee : ')
    avgincome = collection.aggregate([
        {'$group' : {'_id' : 'null', 'avg salary':{ '$avg' : '$MonthlyIncome'}}}, 
                    {'$project' : {'_id' : 0}}])
    
    for item in avgincome:
        item['avg salary'] = np.round(item['avg salary'], 2) 
        print(item)
        
    # 5. 
    print('Find the AVG PercentSalaryHike of employee : ')
    avgincome = collection.aggregate([
        {'$group' : {'_id' : 'null', 'avgsalary_hike':{ '$avg' : '$PercentSalaryHike'}}}, 
                    {'$project' : {'_id' : 0}}])
    
    for item in avgincome:
        item['avgsalary_hike'] = np.round(item['avgsalary_hike'], 2) 
        print(item)
    
    # 6. 
    avg_attrition = collection.aggregate([
                    {'$match' : {'Attrition':"Yes"}},
                    {'$group' : {'_id' : 'null', 'avgsalary_hike':{ '$avg' : '$PercentSalaryHike'}}}, 
                    {'$project' : {'_id' : 0}}])
    
    for item in avg_attrition:
        item['avgsalary_hike'] = np.round(item['avgsalary_hike'], 2) 
        print(item)
    
    # 7. 
    print('Highest attrition is in which department : ')
    Dept_attrition = collection.aggregate([
        {'$match' : {'Attrition':"Yes"}},
        {'$group':{'_id' : '$Department', 'total_counts':{'$count':{}}}},
        {'$sort' : {'total_counts':-1}},
        ])
    
    for item in Dept_attrition:
        print(item)
        
