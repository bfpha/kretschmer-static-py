# Kretschmer/Lesbos Static

## Building the app CLI

* Create a Python virtual environment:
`python -m venv env`
* Start env:
`python source env/bin/activate`
* Install dependencies:
`pip install -r requirements.txt`
* Building the app:
    * run setup:
    `./setup.sh`
    * build webapp:
    `python run.py`

### Automatic app build process using Github Workflows
The build process is documented and available in [BUILD YML](https://github.com/acdh-oeaw/kretschmer-static-py/blob/master/.github/workflows/build.yml).
Learn more about [Github Actions](https://docs.github.com/en/actions).
After the build process finished the website is hosted using [Github Pages](https://pages.github.com/). The finished build is deployed in a separate branch called gh-pages.

## Documentation

Data to generate website content is created using Python [Pandas](https://pandas.pydata.org/) in combination with Google Sheets.
The serialized data from GSheet is converted into a JSON Object and passed to [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) a Python template engine.

Project template from https://github.com/csae8092/object-biographien.

### utlis

[utlis](https://github.com/acdh-oeaw/kretschmer-static-py/blob/master/utils.py) contains all necessary python functions to process the data. If changes were made to the gsheet a new build of the app will recognize the changes.
This is true for currently available columns. In most cases also new columns are processed and made available. The Jinja2 templates must be adapted accordingly.

### templates

The directory [templates](https://github.com/acdh-oeaw/kretschmer-static-py/tree/master/templates) contains all required Jinja2 templates. To change the HTML structure or content like URLs for e.g. images the templates have to be adapted.
To build the app only html templates are required. TTL templates are used to generate rdf/ttl metadata.

### setup

The app requires [Bootstrap](https://getbootstrap.com/) and ACDH-CH [Fundament](https://github.com/acdh-oeaw/fundament) ([dl_fundament.sh](https://github.com/acdh-oeaw/kretschmer-static-py/blob/master/dl_fundament.sh)). Running the [setup](https://github.com/acdh-oeaw/kretschmer-static-py/blob/master/setup.sh) will install both. Additionally, the website imprint is provided by an imprint ([dl_imprint.sh](https://github.com/acdh-oeaw/kretschmer-static-py/blob/master/dl_imprint.sh)) service hosted at the ACDH-CH which will be installed as well.

After the app was build all required files are saved in the [html](https://github.com/acdh-oeaw/kretschmer-static-py/tree/master/html) directory. From start this directory contains a subdir [static](https://github.com/acdh-oeaw/kretschmer-static-py/tree/master/html/static) with required CSS, JS and static images.

### Generic images and other files

All filenames for images and other files are part of the gsheet and automatically implemented using the mentioned Jinja2 templates.
If the file host changes URLs must be adapted in the underlying Jinja2 template.

# LICENSE

[MIT](https://github.com/acdh-oeaw/kretschmer-static-py/blob/master/LICENSE)
