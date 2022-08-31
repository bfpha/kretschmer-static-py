from re import M
from utils import (
    gsheet_to_df,
    make_rdf_ttl,
    make_rdf_tonaufnahmen_ttl,
    make_rdf_person_ttl,
)
from rdflib import Graph

IMAGES = "1aJz8-2rj-d2a62ciBH2j-ehzp4f0EgPF_Qg554W2IFA"
PERSONS = "1frs9RF7kqAmbl3W1PWPRJyq1iGBxHIQikrNr9yXkkyQ"
AUDIO = "16HRSdXvbUiTrQaxWoDjXiY3KfOFKUGwCoWE4S9TgcmU"
DF = gsheet_to_df(IMAGES)
make_rdf_ttl(DF)
DF2 = gsheet_to_df(PERSONS)
make_rdf_person_ttl(DF2)
DF3 = gsheet_to_df(AUDIO)
make_rdf_tonaufnahmen_ttl(DF3)
g = Graph()
# g.parse('rdf/rdf_constants_deleted.ttl', format='ttl')
# g.parse('rdf/katalog_place.ttl', format='ttl')
# g.parse('rdf/katalog_person.ttl', format='ttl')
# g.parse('rdf/katalog_journal.ttl', format='ttl')
# g.parse('rdf/katalog_journal2.ttl', format='ttl')
# g.parse('rdf/katalog_fotos.ttl', format='ttl')
g.parse('rdf/missingDesc.ttl', format='ttl')
# g.parse('rdf/katalog_tonaufnahmen.ttl', format='ttl')
g.serialize(destination="rdf/objects_kretschmer_all.ttl", format='ttl')
