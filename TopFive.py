import pandas as pd 
import TrefleQuery as TrefleQuery
import asyncio 
from datetime import datetime

def TopFive(borough):
    filename = "london_street_trees_gla_20180214.csv"
    TQ = TrefleQuery.TrefleQuery()
    df = pd.read_csv(filename)
    df['borough'] = df['borough'].apply(lambda x: x.strip())
    top_five = df[df['borough']==borough].groupby('species_name').count().sort_values('gla_id',ascending=False)['gla_id'][0:5]
    lambeth_species = [(item[0],item[1]) for item in zip(top_five.keys(), top_five.values)]
    lambeth_species = [(species[0].replace(' species',''), species[1]) for species in lambeth_species]
    lambeth_species = [{
                            'latin': species[0],
                            'name' : TQ.species_search(species[0]).name,
                            'count': species[1]
                       } 
                        for species in lambeth_species]
    return lambeth_species

def GetBoroughList():
    filename = "london_street_trees_gla_20180214.csv"
    df = pd.read_csv(filename)
    df['borough'] = df['borough'].apply(lambda x: x.strip())
    return list(df['borough'].unique())