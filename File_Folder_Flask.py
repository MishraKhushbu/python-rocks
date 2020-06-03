import json
import os
import hashlib ,binascii


#==========================New Code==============================
def folder_walk(path):

    #==========Directory_Path_Namings================================
    mywork = {}
    os.chdir(path)
    new_dict = {}
    my_file_list = []
    #==========Directory_Path_Namings==================================

    for (root ,dirs ,files) in os.walk(path ,topdown = False):
        current_dir = root.split('/')[-1]
        current_file_list = os.listdir(root)

        #=========sha_code_for_files++++++======

        if len(files)!=0 :
            current_file_dict = {}
            for j in range(0, len(files), 1):
                with open(os.path.join(root,files[j]), 'rb') as f0:
                    my_file = (files[j])
                    file_contents = f0.read()
                    file_hash_contents = hashlib.sha512(file_contents).hexdigest()
                    current_file_dict[my_file] = file_hash_contents

            new_dict[current_dir] = current_file_dict

    #mywork[(root.split('/')[-1])] = new_dict
    # ========================JSON_File_Code=========================

    with open('/home/anshu/Documents/Python_Practice/Hotel_json.json', 'w') as f1:

        json.dump(new_dict, f1, indent=4)
    # ======================JSON_File_Code================================

    return (new_dict)


