from re import M
from utils import (
    gsheet_to_df,
    make_rdf_ttl,
    gsheet2_to_df,
    make_rdf_tonaufnahmen_ttl,
    gsheet3_to_df,
    make_rdf_person_ttl,
)

DF = gsheet_to_df()
make_rdf_ttl(DF)
DF2 = gsheet2_to_df()
make_rdf_person_ttl(DF2)
DF3 = gsheet3_to_df()
make_rdf_tonaufnahmen_ttl(DF3)
