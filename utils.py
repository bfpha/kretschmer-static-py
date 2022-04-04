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

GDRIVE_URL = "https://docs.google.com/spreadsheet/ccc?key=1CZdnY39HSsE0C9eSMdvuCoRxJhSxnwlcUxr80qv96uY"

def gsheet_to_df():
    url = f"{GDRIVE_URL}&output=csv"
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
        for i, row in df.iterrows():
            item['prev'] = slugify(row[1]) + ".html"
            item['next'] = slugify(row[2]) + ".html"
            item['prevTitle'] = row[1]
            item['nextTitle'] = row[2]
            item['collection'] = row[3]
            item['titleOrig'] = row[8]
            station = {}
            for x in row.keys():
                station[x] = row[x]
            station["fileName"] = file_name
            item['metadata'].append(station)
            rows.append(station)
        items.append(item)
        with open(f"./html/{file_name}", 'w') as f:
            f.write(template.render(**item))
    template = templateEnv.get_template('./templates/index.html')
    with open('./html/index.html', 'w') as f:
        f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/map.html')
    with open('./html/map.html', 'w') as f:
        f.write(template.render({"objects": items}))
    template = templateEnv.get_template('./templates/table.html')
    with open('./html/table.html', 'w') as f:
        f.write(template.render({"objects": rows}))
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
                    "title": f"{gr}"
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
                    "title": row['placeRegionDe']
                }
            }
            item["features"].append(feature_point)

        item["features"].append(feature_line)
        with open(f'./html/data/{file_name}', 'w', encoding='utf-8') as f:
            json.dump(item, f, ensure_ascii=False, indent=4)
        items.append(item)
    return items

GDRIVE_URL2 = "https://docs.google.com/spreadsheet/ccc?key=1O_BGOyzf1d-1qJGwPrIr1EHTxP3ThpTWxUVnkH5l_NQ"

def gsheet2_to_df():
    url = f"{GDRIVE_URL2}&output=csv"
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
