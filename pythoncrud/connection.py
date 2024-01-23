from django.http import HttpResponse
from pymongo import MongoClient
from django.conf import settings

def get_mongo_client():
    return MongoClient(
        host='mongodb://localhost:27017/'
    )

def example_view(request):
    client = get_mongo_client()
    
    # Check if the client is not None before using it
    if client is not None:
        db = client['yourmongodbname']
        collection = db['your_collection']

        # Perform MongoDB operations
        result = collection.find_one({'field': 'value'})

        # Close the PyMongo client when done
        client.close()

        return HttpResponse(f'MongoDB result: {result}')
    else:
        # Handle the case where the client is None
        return HttpResponse('Failed to connect to MongoDB')

