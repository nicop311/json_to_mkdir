# json_to_mkdir
Create a directory structure out of the JSON output which use the same format as the one obtained with the following bash command `$ tree -Jd`.

## Usage

### Get help documentation

```
./jsontodir.py -h
```
```
usage: jsontodir.py [-h] [-j JSONFILEINPUT] [-js JSONSTRINGINPUT] [-d DIRECTORYPATH] [-t] [-v]

        This tool creates (with os.mkdir) a directory strucure out af a
        JSON data which follows the format of bash `$ tree -Jd`.
        
        Usage:
        
        * JSON file as input:
          $ ./jsontodir.py -j /tmp/toDelete/tree.json -d /tmp/myDir
          
        * JSON string as input:
          $ ./jsontodir.py -js  '[{"type":"directory","name":"root_dir","contents":[{"type":"directory","name":"subdir","contents":[]}]},{"type":"report","directories":1}]'   -d /tmp/lolol
          
        * Test the tool to see if it works in your environment:
          $ ./jsontodir.py -t
          
          
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
