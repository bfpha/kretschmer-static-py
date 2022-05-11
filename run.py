from re import M
from utils import (
    gsheet_to_df,
    make_index_html,
    make_geojsons,
    gsheet2_to_df,
    make_person_html,
    gsheet4_to_df,
    make_audio_html,
)

DF = gsheet_to_df()
make_index_html(DF)
make_geojsons(DF)
DF2 = gsheet2_to_df()
make_person_html(DF2)
DF3 = gsheet4_to_df()
make_audio_html(DF3)
make_geojsons(DF3)
