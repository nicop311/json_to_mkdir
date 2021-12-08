# json_to_mkdir
Create a directory structure out of the JSON output which use the same format as the one obtained with the following bash command `$ tree -Jd`.

## Usage

Convert this JSON string or file (follwing the format of the bash command `$ tree -Jd`):

```json
[
  {"type":"directory","name":"root_dir","contents":[
    {"type":"directory","name":"subedir1_level1","contents":[
      {"type":"directory","name":"subedir11_level2","contents":[
        {"type":"directory","name":"subedir111_level3","contents":[
        ]},
        {"type":"directory","name":"subedir112_level3","contents":[
        ]},
        {"type":"directory","name":"subedir113_level3","contents":[
        ]}
      ]}
    ]},
    {"type":"directory","name":"subedir2_level1","contents":[
      {"type":"directory","name":"subedir21_level2","contents":[
        {"type":"directory","name":"subedir211_level3","contents":[
        ]}
      ]}
    ]}
  ]},
  {"type":"report","directories":8}
]
```

into directories:

```
tree /tmp/jsontodir_2021-12-08_11-49-20
```
```
/tmp/jsontodir_2021-12-08_11-49-20
└── root_dir
    ├── subedir1_level1
    │   └── subedir11_level2
    │       ├── subedir111_level3
    │       ├── subedir112_level3
    │       └── subedir113_level3
    └── subedir2_level1
        └── subedir21_level2
            └── subedir211_level3
```

### Get help documentation

Everything you need to know is in the --help doc.

```
./jsontomkdir.py -h
```

```
usage: jsontomkdir.py [-h] [-j JSONFILEINPUT] [-js JSONSTRINGINPUT] [-d DIRECTORYPATH] [-t] [-v]

        This tool creates (with os.mkdir) a directory strucure out af a
        JSON data which follows the format of bash `$ tree -Jd`.
        
        Usage:
        
        * JSON file as input:
          $ ./jsontomkdir.py -j /tmp/toDelete/tree.json -d /tmp/myDir
          
        * JSON string as input:
          ```
          $ ./jsontomkdir.py -js  '[{"type":"directory","name":"root_dir","contents":[{"type":"directory","name":"subdir","contents":[]}]},{"type":"report","directories":1}]'   -d /tmp/lolol
          Your directory is created here: /tmp/lolol .
          ```
          
          ```
          $ tree /tmp/lolol
          /tmp/lolol
          └── root_dir
              └── subdir
          ```
          
        * Test the tool to see if it works in your environment:
          ```
          $ ./jsontomkdir.py -t
          Testing with trivial example. -j and -d are omitted
          Your directory is created here: /tmp/jsontodir_2021-12-08_11-49-20 .
          ```
          ```
          $ tree /tmp/jsontodir_2021-12-08_11-49-20
          /tmp/jsontodir_2021-12-08_11-49-20
          └── root_dir
              ├── subedir1_level1
              │   └── subedir11_level2
              │       ├── subedir111_level3
              │       ├── subedir112_level3
              │       └── subedir113_level3
              └── subedir2_level1
                  └── subedir21_level2
                      └── subedir211_level3
          ```
          
          
        Add verbosity with -v.
        

optional arguments:
  -h, --help            show this help message and exit
  -j JSONFILEINPUT, --jsonfileinput JSONFILEINPUT
                        A JSON file following the format returned by the bash method $ tree -Jd.
  -js JSONSTRINGINPUT, --jsonstringinput JSONSTRINGINPUT
                        A JSON STRING following the format returned by the bash method $ tree -Jd.
  -d DIRECTORYPATH, --directorypath DIRECTORYPATH
                        TODO écrire description
  -t, --testing         Test this tool with a trivial example.
  -v, --verbose         Verbosity. Default is False.
```
