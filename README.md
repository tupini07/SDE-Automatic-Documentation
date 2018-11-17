You need `python 3.*` to work on this.

To install dependencies run: 

```
pip install -r requirements.txt
```

To build the documentation `cd` to the `docs` folder and run:

```
make html
```

To publish the documentation make sure you have an account on `surge.sh`, modify the `docs/CNAME` file so that it has whatever domain URL you would like to use, and then from `docs/` execute `make publish`. 


## VM needs to have

- Postman
- Python 3.6 and project requirements
- TexLive, and latexmk (https://latextools.readthedocs.io/en/latest/install/#linux) for PDF generation
    - Need to test that both are actually compiling correctly
- surge for uploading to live
- Some browser
- Some editor