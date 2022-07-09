Unicode-debugger shows the code points that make up a text and their names

TODO: and the classes it belongs to

---

View the site locally

``` sh
python3 -m http.server
```

Look at the source data

``` sh
curl https://www.unicode.org/Public/UCD/latest/ucd/NamesList.txt | less
```

Update the data in [codepoint-names.js](./codepoint-names.js)

``` sh
pip install requests
python update_codepoint_names.py
```

Check which code points are missing

``` sh
node
```

``` javascript
.load codepoint-names.js
for (let x = 0; x < 0x110000; x++) { if (!NAMES[x]) { console.log(x.toString(16)) } }
```
