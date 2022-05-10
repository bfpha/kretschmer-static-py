from re import M
from utils import (
    gsheet_to_df,
    make_rdf_ttl,
    gsheet2_to_df,
    make_rdf_tonaufnahmen_ttl,
    gsheet3_to_df,
    make_rdf_person_ttl,
)
from rdflib import Graph

DF = gsheet_to_df()
make_rdf_ttl(DF)
DF2 = gsheet2_to_df()
make_rdf_person_ttl(DF2)
DF3 = gsheet3_to_df()
make_rdf_tonaufnahmen_ttl(DF3)
g = Graph()
# g.parse('rdf/rdf_constants_deleted.ttl', format='ttl')
# g.parse('rdf/katalog_place.ttl', format='ttl')
# g.parse('rdf/katalog_person.ttl', format='ttl')
g.parse('rdf/katalog_journal.ttl', format='ttl')
g.parse('rdf/katalog_journal2.ttl', format='ttl')
g.parse('rdf/katalog_fotos.ttl', format='ttl')
g.serialize(destination="rdf/objects_kretschmer_all.ttl", format='ttl')
