from bottle import *
import os
import File_Folder_Flask

# Server startup message
@route("/", methods=['POST', 'GET'])
def home():
    return (
        "Welcome! To the homepage")

@route("/<path:path>", methods=['POST', 'GET'])
def getProviderRoute(path):
    print(path)
    my_output =  File_Folder_Flask.folder_walk("/"+ path)
    return my_output

run(host='localhost', port=8080)



