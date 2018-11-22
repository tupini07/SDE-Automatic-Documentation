You need `python 3.*` to work on this.

To install dependencies run: 

```
pip install -r requirements.txt
```

To build the documentation `cd` to the `docs` folder and run:

```
make html
```

To publish the documentation make sure you have [surge](https://surge.sh) installed: modify the `docs/CNAME` file so that it has whatever domain URL you would like to use, and then from `docs/` execute `make publish`. 


## Checklist for VM

- [x] Postman
- [x] Python 3.6 and project requirements
- [x] [TexLive, and latexmk](https://latextools.readthedocs.io/en/latest/install/#linux) for PDF generation
- [x] surge for uploading to live
- [x] Browser
- [x] VM autologin


