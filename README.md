Unicode-debugger shows the bytes that make up a text, the name of the character and
the classes it belongs to. And displays how codepoints group into emojis.

TODO: favicon https://realfavicongenerator.net

``` sh
echo "const NAMES = {" > unicode-names.js
curl https://www.unicode.org/Public/UCD/latest/ucd/NamesList.txt | grep ^[0-9] | awk -F'\t' '{print "0x"$1":","\""$2"\","}' >> unicode-names.js
echo "};" >> unicode-names.js
```

Deploying changes:

``` sh
rsync -av --exclude=.* ~/unicode-debugger/ root@159.203.13.241:/srv/www/html/
```
