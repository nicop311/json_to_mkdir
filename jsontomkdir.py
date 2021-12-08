#!/usr/bin/env python3
import os
import json
import argparse
from datetime import datetime

# This jsonstring variable is used only for testing this tool.
# This jsonstring is obtained with bash tool: $ tree -Jd
jsonstring = \
"""
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
"""



def jsonstring_to_dir(inputjsonstring=jsonstring,
                      outputdir="/tmp/jsontodir_" 
                      + datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
                      verbose=False):
    """Creates ($ mkdir) a linux directory structure out of a JSON string input.
    
    This method takes the JSON output of the bash function "tree -Jd" and
    creates
    
    $ tree -Jd > tree_directroy_struct.json
    
    For example, the following directory structure would produce the following
    JSON output:
    
    ```bash
    $ tree
    .
    └── root_dir
        ├── subedir1_level1
        │   └── subedir11_level2
        │       ├── subedir111_level3
        │       ├── subedir112_level3
        │       └── subedir113_level3
        └── subedir2_level1
            └── subedir21_level2
                └── subedir211_level3
    ```
    
    ```JSON
    [
      {"type":"directory","name":"./root_dir","contents":[
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
    
    
    Args:
        inputjsonstring (str): A JSON string.
        outputdir (str, optional): Path of the directory. Defaults to "/tmp".
    """
    # Make the output directory:
    try: 
        os.makedirs(outputdir)
    except OSError as error: 
        print("Error: can not create root output directory: {}".format(error))
        
    # convert from JSON to python dict.
    try:
        datadict = json.loads(inputjsonstring)
    except ValueError as error2:
        print("Invalid JSON: {}".format(error2))
        exit(1)

    # create the directory structure
    dict_to_dir(datadict, outputdir, verbose)
    print("Your directory is created here: {} . ".format(outputdir))



def json_to_dir(jsonfile,
                outputdir="/tmp/jsontodir_" 
                + datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
                verbose=False):
    """Takes a JSON file (obtained with $ tree -Jd) and creates directories.
    
    See method jsonstring_to_dir which does the same, only on jsonstrings
    instead of JSON files.

    Args:
        inputjsonfile (File): A JSON File.
        outputdir (str, optional): Path of the directory. Defaults to "/tmp".
    """
    # Make the output directory:
    try: 
        os.makedirs(outputdir)
    except OSError as error: 
        print("Error: can not create root output directory: {}".format(error))
    
    try: 
        with open(jsonfile, 'r') as inputjsonfile:
            try:
                # convert from JSON to python dict.
                datadict = json.load(inputjsonfile)
                
                # create the directory structure
                dict_to_dir(datadict, outputdir, verbose)
                print("Your directory is created here: {}. ".format(outputdir))
                inputjsonfile.close()
            except ValueError as error:
                print("Invalid JSON: {}".format(error))
                exit(1)
            finally:
                inputjsonfile.close()
    except FileNotFoundError as error2:
        print("File not found: {}".format(error2))



def dict_to_dir(input_dict,
                dir,
                verbose=False):
    """Takes a python directories as input and creates directories.
    
    The python directories should be produced out of the JSON output from
    bash $ tree -Jd.
    
    This is a recursive function.
    
    Args:
        input_dict ([type]): [description]
        dir ([type]): [description]
    """
    # A python dict is composed of lists and dicts.
    # This step handles an object of type dict:
    if type(input_dict) is dict:
        if input_dict['type']=="directory":
            path = os.path.join(dir, input_dict['name'])
            if verbose:
                print("mkdir " + path)
            try:
                os.mkdir(path)
            except OSError as error: 
                print(error)
                
            if input_dict['contents'] is not []:
                path = os.path.join(dir, input_dict['name'])
                dict_to_dir(input_dict['contents'], path, verbose)
                
    # This step handles an object of type list:
    elif type(input_dict) is list:
        for elmt in range(len(input_dict)):
            dict_to_dir(input_dict[elmt], dir, verbose)
    # TODO: should raise error.
    # If the input_dict is not valid, the method should raise an error.
    else:
        print("The format of this Python dictionnary is not valid.")



def main():
    usage = \
        """
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
        """
    
    
    parser = argparse.ArgumentParser(
                          description = usage,
                          formatter_class=argparse.RawTextHelpFormatter
                          )

    parser.add_argument("-j", "--jsonfileinput",
                        help="A JSON file following the format returned by "
                        "the bash method $ tree -Jd.",
                        required=False)
    
    parser.add_argument("-js", "--jsonstringinput",
                        help="A JSON STRING following the format returned by "
                        "the bash method $ tree -Jd.",
                        required=False)

    parser.add_argument("-d", "--directorypath",
                        help="TODO écrire description",
                        required=False)
    
    parser.add_argument("-t", "--testing",
                        help="Test this tool with a trivial example.",
                        action='store_true',
                        required=False)
    
    parser.add_argument("-v","--verbose",
                        help="Verbosity. "
                        "Default is False.",
                        action='store_true',
                        default=False)

    args = parser.parse_args()
    
    if args.testing:
        print("Testing with trivial example. -j and -d are omitted")
        jsonstring_to_dir(verbose=args.verbose)
    elif args.jsonfileinput!=None:
        json_to_dir(args.jsonfileinput,
                    args.directorypath,
                    args.verbose)
    elif args.jsonstringinput!=None:
        jsonstring_to_dir(args.jsonstringinput,
                          args.directorypath,
                        args.verbose)
    else:
        print("Error in parameters.")
    
    
    
if __name__=="__main__":
    main()
