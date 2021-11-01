from pymongo import MongoClient

def fetch_from_db(keyword):
    client = MongoClient('mongodb://localhost:27017/paper_db')
    db=client.paper_db
    papers_collec=db['papers'].find({'$text':{'$search':keyword}})# , 'rank':{'$ne':'NA'}})
    paper_lst=list(papers_collec)
    if len(paper_lst) == 0:
        #If there is no data with that keyword,
        #fetch data from different api's and insert data after preprocessing
        #Display the processed data
        print("Empty")
    else:
        for doc in paper_lst:
            print(doc)

fetch_from_db("vision machine")