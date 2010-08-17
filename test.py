"""
Mendeley Open API Example Client

Copyright (c) 2010, Mendeley Ltd. <copyright@mendeley.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

For details of the Mendeley Open API see http://dev.mendeley.com/

Example usage:

python test.py

"""

from pprint import pprint
from mendeley_client import MendeleyClient
import json
import os

mendeley = MendeleyClient('<insert_consumer_key_here>', '<insert_secret_key_here>')

try:
	mendeley.load_keys()
except IOError:
	mendeley.get_required_keys()
	mendeley.save_keys()

########## Public Methods Tests ##########

### Stats ###
print 'Authors stats'
response = mendeley.author_stats()
pprint(response)

print 'Papers stats'
response = mendeley.paper_stats()
pprint(response)

print 'Publication stats'
response = mendeley.publication_stats()
pprint(response)

print 'Tag stats'
response = mendeley.tag_stats('6')
pprint(response)

### Search ###

print 'Search for science'
response = mendeley.search('science', items=5)
pprint(response)

### Authored ###

print 'Authored by Ann Cowan'
response = mendeley.authored('Ann Cowan', items=5)
pprint(response)

### Tagged ###

print 'Tagged modularity'
response = mendeley.tagged('modularity', items=5)
pprint(response)

print 'Tagged test in discipline 6 (computer science)'
response = mendeley.tagged('test', cat=6)
pprint(response)

print 'Tagged modularity in subdiscipline Bioinformatics'
response = mendeley.tagged('modularity', subcat=455)
pprint(response)

### Categories and subcategories ###

print 'Categories'
response = mendeley.categories()
pprint(response)

print 'Subcategories'
response = mendeley.subcategories(3)
pprint(response)

#### Related ###

print 'Get related ones'
response = mendeley.related('91df2740-6d01-11df-a2b2-0026b95e3eb7')
pprint(response)

#DOI lookup

print 'DOI lookup'
response = mendeley.details('10.1145%2F1323688.1323690', type='doi')
pprint(response)

# Details

print 'Get details'
response = mendeley.details('2c8d9cb0-6d00-11df-a2b2-0026b95e3eb7')
pprint(response)

########## User Specific Tests ##########

### Library ###
print 'Library'
documents = mendeley.library()
pprint(documents)

### Collections ###

print 'Create new public collection called: "Create collection test"'
response = mendeley.create_collection(collection=json.dumps({'name': 'Collection test'}))
pprint(response)
collectionId = response['collection_id']

print 'Collections'
collections = mendeley.collections()
for collection in collections:
	print collection

### Shared Collections ###

print 'Create a new Share Collection"'
response = mendeley.create_sharedcollection(sharedcollection=json.dumps({'name': 'Shared collection to delete'}))
sharedcollectionid = response['shared_collection_id']
pprint(response)
pprint(sharedcollectionid)

'''print 'Shared Collections Members'
shared = mendeley.sharedcollections()
for share in shared:
	print share
	sharedId = share['id']
	members = mendeley.sharedcollection_members(sharedId)
	pprint(members)'''



### Documents ###
print 'Create new document on shared collection'
response = mendeley.create_document(document=json.dumps({'title': 'Document Title for SHARED COLLECTION', 'year': 2008, 'shared_collection_id': sharedcollectionid}))
pprint(response)
sharedDocumentId = response['document_id']

pprint(sharedcollectionid)
docs = mendeley.sharedcollection_documents(sharedcollectionid)
pprint(docs)

print 'Remove document from shared collection'
response = mendeley.delete_sharedcollection_document(sharedcollectionid, sharedDocumentId)
pprint(response)

docs = mendeley.sharedcollection_documents(sharedcollectionid)
pprint(docs)

print 'Remove shared collection'
response = mendeley.delete_sharedcollection(sharedcollectionid)
pprint(response)

print 'Shared Collections'
shared = mendeley.sharedcollections()
for share in shared:
	print share

print 'Create new document on library'
response = mendeley.create_document(document=json.dumps({'title': 'Document Title', 'year': 2010}))
pprint(response)
documentId = response['document_id']

print 'Add document to collection'
response = mendeley.add_document_to_collection(collectionId, documentId)
pprint(response)

print 'List all documents in collection'
docs_in_collection = mendeley.collection_documents(collectionId)
pprint(docs_in_collection)

print 'Remove document from collection'
response = mendeley.remove_document_from_collection(collectionId, documentId)
pprint(response)

docs_in_collection = mendeley.collection_documents(collectionId)
pprint(docs_in_collection)

print 'Remove collection'
response = mendeley.delete_collection(collectionId)
pprint(response)

### Documents ###

print 'Listing all documents in library'
response = mendeley.library()
pprint(response)
docs = response['document_ids']
print 'Details for all docs in the library'
for doc in docs:
	response = mendeley.document_details(doc)
	pprint(response)


print 'Create new document in library'
response = mendeley.create_document(document=json.dumps({'title': 'Document create test', 'year': 2010, 'Volume': 1, 'type': 'Journal Article', 'url': 'http://www.mendeley.com', 'tags':['test', 'journal']}))
pprint(response)
documentId = response['document_id']

response = mendeley.document_details(documentId)
pprint(response)

print 'Getting authored documents'
response = mendeley.documents_authored()
pprint(response)
for document in response['document_ids']:
	details = mendeley.document_details(document)
	pprint(details)

print 'Getting library'
response = mendeley.library(items=500)
pprint(response)

### MEMBERS ###

print 'Getting current user contacts'
response = mendeley.contacts()
pprint(response)
