'''

Inspired in part by http://code.alcidesfonseca.com/docs/rdflib/graph_merging.html

'''

import sys
from rdflib.graph import Graph

def main(argv):
#     inputFileName1 = '/home/mikel/UPV-EHU/Eclipse_Workspace/MergeRDFGraphs-Galaxy/data/vc-db-3.rdf'
#     inputFileName2 = '/home/mikel/UPV-EHU/Eclipse_Workspace/MergeRDFGraphs-Galaxy/data/vc-db-4.rdf'
    
    store = Graph()
    for inputFileName in argv:
        store.parse(inputFileName)
    print store.serialize()

if __name__ == "__main__":
    main(sys.argv[1:])
