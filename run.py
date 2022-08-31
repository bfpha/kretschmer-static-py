from re import M
from utils import (
    gsheet_to_df,
    make_index_html,
    make_geojsons,
    make_person_html,
    make_audio_html,
)

IMAGES = "1aJz8-2rj-d2a62ciBH2j-ehzp4f0EgPF_Qg554W2IFA"
DF = gsheet_to_df(IMAGES)
PERSONS = "1frs9RF7kqAmbl3W1PWPRJyq1iGBxHIQikrNr9yXkkyQ"
DF2 = gsheet_to_df(PERSONS)
AUDIO = "16HRSdXvbUiTrQaxWoDjXiY3KfOFKUGwCoWE4S9TgcmU"
DF3 = gsheet_to_df(AUDIO)
make_index_html(DF)
make_geojsons(DF)
make_person_html(DF2)
make_audio_html(DF3)
make_geojsons(DF3)
