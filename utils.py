from audioop import reverse
import jinja2
import json
import os
import pandas as pd
import requests
from slugify import slugify
from io import BytesIO


templateLoader = jinja2.FileSystemLoader(searchpath=".")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template('./templates/index.html')

GDRIVE_URL_FOTOS = "https://docs.google.com/spreadsheet/ccc?key=1aJz8-2rj-d2a62ciBH2j-ehzp4f0EgPF_Qg554W2IFA"

def gsheet_to_df():
    url = f"{GDRIVE_URL_FOTOS}&output=csv"
    r = requests.get(url)
    print(r.status_code)
    data = r.content
    df = pd.read_csv(BytesIO(data), on_bad_lines='skip')
    # df = pd.read_csv('./data_dump.csv')
    # print(df)
    return df

# df.to_csv('data_dump.csv', index=False)

def make_index_html(df):
    os.makedirs('./html', exist_ok=True)
    items = []
    rows = []     
    places = []  
    template = templateEnv.get_template('./templates/object.html')
    for gr, df in df.groupby('ordering'):
        object_id = slugify(gr)
        file_name = f"{object_id}.html"
        data_src = f"data/{object_id}.geojson"
        item = {
            "object_id": f"a{object_id.replace('-', '_')}",
            "url": file_name,
            "data_src": data_src, 
            "title": gr,
            "metadata": []
        }
        place = {}
        for i, row in df.iterrows():
            item['collection'] = row['collection']
            item['prev'] = slugify(row['previous']) + ".html"
            item['next'] = slugify(row['next']) + ".html"
            item['prevTitle'] = row['previous']
            item['nextTitle'] = row['next']
            item['prevGr'] = slugify(row['previousGr']) + ".html"
            item['nextGr'] = slugify(row['nextGr']) + ".html"
            item['prevTitleGr'] = row['previousGr']
            item['nextTitleGr'] = row['nextGr']
            item['titleOrig'] = row['titleDe']
            item['titleOrigGr'] = row['titleGr']
            station = {}
            placeKey = slugify(row['placeRegionDe'])
            place[placeKey] = {
                "titleDe": row['placeRegionDe'],
                "titleGr": row['placeRegionGr'],
                "coordinates": row['coordinates'],
                "countryDe": row['countryDe'],
                "countryGr": row['countryGr'],
                "countryHistoryDe": row['countryHistoryDe'],
                "countryHistoryGr": row['countryHistoryGr'],
                "geonamesPlace": row['placeGeonames'],
                "data_src": data_src,
                "object_id": f"a{object_id.replace('-', '_')}",
                "fileName": file_name,
                "photoTitleDe": row['titleDe'],
                "photoTitleGr": row['titleGr'],
            }            
            for x in row.keys():
                station[x] = row[x]
            station["fileName"] = file_name
            item['metadata'].append(station)
            rows.append(station)
        items.append(item)
        with open(f"./html/{file_name}", 'w') as f:
            f.write(template.render(**item))
        places.append(place)
    tmp_names = []
    tmp_places = []
    places_map = []
    for obj in places:    
        for x in obj.keys():
            if x not in tmp_names:
                tmp_names.append(x)
                tmp_places.append(obj[x])                
            else:
                places_map.append(obj[x])
    places = {
        "unique": [],
        "map": []
    }
    places['unique'].append(tmp_places)
    places['map'].append(places_map) 
    template = templateEnv.get_template('./templates/index.html')
    with open('./html/index.html', 'w') as f:
        f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/foto-detail.html')
    with open('./html/fotos-detail.html', 'w') as f:
        f.write(template.render({"objects": items}))
    # template = templateEnv.get_template('./templates/map.html')
    # with open('./html/map.html', 'w') as f:
    #     f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/table.html')
    with open('./html/table.html', 'w') as f:
        f.write(template.render({"objects": rows}))
    template = templateEnv.get_template('./templates/place-index.html')
    with open('./html/place-index.html', 'w') as f:
        f.write(template.render({"objects": items,"places": places}))
    template = templateEnv.get_template('./templates/about.html')
    with open('./html/about.html', 'w') as f:
        f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/team.html')
    with open('./html/team.html', 'w') as f:
        f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/journey.html')
    with open('./html/journey.html', 'w') as f:
        f.write(template.render({"objects": items}))
    # print(places)
    return items

def make_geojsons(df):
    items = []
    for gr, df in df.groupby('ordering'):
        os.makedirs('./html/data', exist_ok=True)
        file_name = f"{(slugify(gr))}.geojson"
        item = {
            "type": "FeatureCollection",
            "features": []
        }
        feature_line = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": []
            },
            "properties": {
                    "link": slugify(gr),
                }
        }
        for i, row in df.iterrows():
            coords = list(reversed([float(x) for x in row['coordinates'].replace(' ', '').split(',')]))
            feature_line['geometry']['coordinates'].append(coords)
            feature_point = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": coords
                },
                "properties": {
                    "title": row['placeRegionDe'],
                    "link": slugify(gr),
                    "titleGr": row['placeRegionGr'],
                    "linkTitleDe": row['titleDe'],
                    "linkTitleGr": row['titleGr'],
                }
            }
            item["features"].append(feature_point)
        item["features"].append(feature_line)
        with open(f'./html/data/{file_name}', 'w', encoding='utf-8') as f:
            json.dump(item, f, ensure_ascii=False, indent=4)
        items.append(item)
    return items

GDRIVE_URL_PERSON = "https://docs.google.com/spreadsheet/ccc?key=1frs9RF7kqAmbl3W1PWPRJyq1iGBxHIQikrNr9yXkkyQ"

def gsheet2_to_df():
    url = f"{GDRIVE_URL_PERSON}&output=csv"
    r = requests.get(url)
    print(r.status_code)
    data = r.content
    df = pd.read_csv(BytesIO(data), on_bad_lines='skip')
    # df = pd.read_csv('./data_dump.csv')
    # print(df)
    return df

def make_person_html(df):
    os.makedirs('./html', exist_ok=True)
    items = []
    rows = []       
    template = templateEnv.get_template('./templates/persons.html')
    for gr, df in df.groupby('id'):
        object_id = slugify(gr)
        file_name = f"{object_id}.html"
        item = {
            "object_id": f"{object_id.replace('-', '_')}",
            "url": file_name,
            "title": gr,
            "metadata": []
        }
        for i, row in df.iterrows():
            station = {}
            for x in row.keys():
                station[x] = row[x]
            item['metadata'].append(station)
            rows.append(station)
        items.append(item)
        with open(f"./html/{file_name}", 'w') as f:
            f.write(template.render(**item))
    template = templateEnv.get_template('./templates/person-index.html')
    with open('./html/person-index.html', 'w') as f:
        f.write(template.render({"objects": items}))
    return items


GDRIVE_URL_AUDIO = "https://docs.google.com/spreadsheet/ccc?key=16HRSdXvbUiTrQaxWoDjXiY3KfOFKUGwCoWE4S9TgcmU"

def gsheet4_to_df():
    url = f"{GDRIVE_URL_AUDIO}&output=csv"
    r = requests.get(url)
    print(r.status_code)
    data = r.content
    df = pd.read_csv(BytesIO(data), on_bad_lines='skip')
    # df = pd.read_csv('./data_dump.csv')
    # print(df)
    return df

def make_audio_html(df):
    os.makedirs('./html', exist_ok=True)
    items = []
    rows = []       
    template = templateEnv.get_template('./templates/object_audio.html')
    for gr, df in df.groupby('ordering'):
        object_id = slugify(gr)
        file_name = f"{object_id}.html"
        data_src = f"data/{object_id}.geojson"
        item = {
            "object_id": f"a{object_id.replace('-', '_')}",
            "url": file_name,
            "data_src": data_src, 
            "title": gr,
            "metadata": []
        }
        for i, row in df.iterrows():
            item['prev'] = slugify(row['previous']) + ".html"
            item['next'] = slugify(row['next']) + ".html"
            item['prevTitle'] = row['previous']
            item['nextTitle'] = row['next']
            item['prevGr'] = slugify(row['previousGr']) + ".html"
            item['nextGr'] = slugify(row['nextGr']) + ".html"
            item['prevTitleGr'] = row['previousGr']
            item['nextTitleGr'] = row['nextGr']
            item['titleOrig'] = row['titleDe']
            item['titleOrigGr'] = row['titleGr']
            station = {}
            for x in row.keys():
                station[x] = row[x]
            item['metadata'].append(station)
            rows.append(station)
        items.append(item)
        with open(f"./html/{file_name}", 'w') as f:
            f.write(template.render(**item))
    template = templateEnv.get_template('./templates/tonaufnahmen-detail.html')
    with open('./html/tonaufnahmen-detail.html', 'w') as f:
        f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/table_audio.html')
    with open('./html/table_audio.html', 'w') as f:
        f.write(template.render({"objects": rows}))
    return items

# creating rdf ttl files

def make_rdf_ttl(df):
    os.makedirs('./rdf', exist_ok=True)
    items = []
    rows = []     
    template = templateEnv.get_template('./templates/katalog_fotos.ttl')
    for gr, df in df.groupby('ordering'):
        object_id = slugify(gr)
        file_name = f"{object_id}.xml"
        item = {
            "object_id": f"a{object_id.replace('-', '_')}",
            "url": file_name,
            "title": gr,
            "metadata": []
        }
        for i, row in df.iterrows():
            station = {}         
            for x in row.keys():
                station[x] = row[x]
            item['metadata'].append(station)
            rows.append(station)
        items.append(item)
    with open('./rdf/katalog_fotos.ttl', 'w') as f:
        f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/katalog_journal.ttl')
    with open('./rdf/katalog_journal.ttl', 'w') as f:
        f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/katalog_place.ttl')
    with open('./rdf/katalog_place.ttl', 'w') as f:
        f.write(template.render({"objects": items}))
    return items

GDRIVE_URL_TONAUFNAHMEN = "https://docs.google.com/spreadsheet/ccc?key=16HRSdXvbUiTrQaxWoDjXiY3KfOFKUGwCoWE4S9TgcmU"

def gsheet3_to_df():
    url = f"{GDRIVE_URL_TONAUFNAHMEN}&output=csv"
    r = requests.get(url)
    print(r.status_code)
    data = r.content
    df = pd.read_csv(BytesIO(data), on_bad_lines='skip')
    # df = pd.read_csv('./data_dump.csv')
    # print(df)
    return df

def make_rdf_tonaufnahmen_ttl(df):
    os.makedirs('./rdf', exist_ok=True)
    items = []
    rows = []     
    template = templateEnv.get_template('./templates/katalog_tonaufnahmen.ttl')
    for gr, df in df.groupby('ordering'):
        object_id = slugify(gr)
        file_name = f"{object_id}.xml"
        item = {
            "object_id": f"a{object_id.replace('-', '_')}",
            "url": file_name,
            "title": gr,
            "metadata": []
        }
        for i, row in df.iterrows():
            station = {}         
            for x in row.keys():
                station[x] = row[x]
            item['metadata'].append(station)
            rows.append(station)
        items.append(item)
    with open('./rdf/katalog_tonaufnahmen.ttl', 'w') as f:
        f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/katalog_journal.ttl')
    with open('./rdf/katalog_journal2.ttl', 'w') as f:
        f.write(template.render({"objects": items}))
    return items

def make_rdf_person_ttl(df):
    os.makedirs('./rdf', exist_ok=True)
    items = []
    rows = []     
    template = templateEnv.get_template('./templates/katalog_person.ttl')
    for gr, df in df.groupby('id'):
        object_id = slugify(gr)
        file_name = f"{object_id}.xml"
        item = {
            "object_id": f"a{object_id.replace('-', '_')}",
            "url": file_name,
            "title": gr,
            "metadata": []
        }
        for i, row in df.iterrows():
            station = {}         
            for x in row.keys():
                station[x] = row[x]
            item['metadata'].append(station)
            rows.append(station)
        items.append(item)
    with open('./rdf/katalog_person.ttl', 'w') as f:
        f.write(template.render({"objects": items}))
    return items
