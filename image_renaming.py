import os
import shutil
import json

def main():
    #Get directory and check status
    input_directory = input("Please enter the input directory: ")
    if os.path.isdir(input_directory) == False:
        print(f"{input_directory} is not a directory.")
        exit(0)
    
    #Find files and check results
    file_list = FindFiles(input_directory, "jpg,jpeg,png")
    if(len(file_list) <= 0):
        print(f"{input_directory} contains no matching files.")
        exit(0)
    
    #List if desired.
    #if input(f"Found {len(file_list)} matching files, would you like to list them? (y/n) ").lower().startswith("y"):
    #    for x in file_list:
    #        print(x)

    print(f"Found {len(file_list)} matching files:")
    for x in file_list:
        print(x)

    #Check for images object 
    json_file_data = None
    #Automated output
    output_json_data = {}
    output_json_file_name = os.path.join(input_directory, "images_automated.json")
    json_file_name = os.path.join(input_directory, "images.json")
    json_image_file_name = None
    if os.path.exists(json_file_name):
        if os.path.isfile(json_file_name):
            with open(json_file_name) as file:
                file = open(json_file_name)
                json_file_data = json.load(file)
                if 'image_file_name' in json_file_data:
                    json_image_file_name = json_file_data['image_file_name']


    #Replace original name with the folder name or info from json file.  Easy way to give them generic names.
    rename_files_with_json = False
    rename_files_with_folder = False
    if not None == json_image_file_name:
        rename_files_with_json = input("Do you want to rename files with JSON data? (y/n) ").lower().startswith('y')
    pass
    if not rename_files_with_json:
        rename_files_with_folder = input("Do you want to rename files with the folder name? (y/n) ").lower().startswith('y')
    
    #Data to create automated JSON
    if(rename_files_with_folder):
        output_json_data["image_file_name"] = folder_name
    if(rename_files_with_json):
        output_json_data["image_file_name"] = json_image_file_name
    output_json_data["html_filename"] = "desired_file_name.html"
    output_json_data["short_title"] = "Short Title"
    output_json_data["long_title"] = "Long Title to Show on Page"
    output_json_data["description"] = [
        "Array of strings for description.",
        "Add multiple if you like."
    ]
    output_json_data["preview_file_name"] = "1200x630_image_for_sharing_preview.jpg"
    output_json_data["parent_page"] =  "parent_page.html"
    output_json_data["meta_description"] = "Description for SEO"

    image_data_for_json = {}

    #Sort files.
    file_list.sort()

    #Set and create originals directory.
    original_directory = os.path.join(input_directory, "original")
    folder_name = os.path.basename(input_directory)
    if os.path.isdir(original_directory) == False:
        os.mkdir(original_directory)

    #Number used in naming.
    i = 0

    for file in file_list:
        #Move file to originals location
        original_filename = os.path.basename(file)
        original_destination_file = os.path.join(original_directory,original_filename)
        shutil.move(file,original_destination_file)

        #Get file name and remove any leading numbers, and get extension.
        filename = os.path.basename(original_destination_file)
        filename = RemoveLeadingNumbers(filename)
        extension = filename[filename.rfind('.'):]

        #Number with leading 0's
        string_i = '{num:03d}'.format(num=i)
        #Completely rename each file with folder name or JSON data if option selected. Add prefix and only add underscore if no dash or underscore present.
        if rename_files_with_folder:
            filename = f"{string_i}_{folder_name}{extension}"
        elif rename_files_with_json:
            filename = f"{string_i}_{json_image_file_name}{extension}"
        else:
            if filename.startswith("-") | filename.startswith("_"):
                filename = string_i + filename
            else:
                filename = string_i + "_" + filename

        #Copy to input directory from original.
        output_file = os.path.join(input_directory, filename)
        image_data_for_json[filename] = "Alt text for image"
        pass
        shutil.copyfile(original_destination_file, output_file)

        #Increment for next file.
        i += 1
    output_json_data["images"] = image_data_for_json
    print("Writing output JSON file.")
    with open(output_json_file_name, "w") as output_file:
        json.dump(output_json_data, output_file, indent=4)





    pass

#Pass extension list with extensions separated by commas, no wildcard or '.' necessary.
def FindFiles(passed_directory:str, passed_extensions:str):
    extension_list = passed_extensions.split(",")
    file_list = os.listdir(passed_directory)
    return_list = []
    for file in file_list:
        for extension in extension_list:
            if file.lower().endswith(extension.replace(" ", "").lower()):
                return_list.append(os.path.join(passed_directory,file))
    return return_list

#Simply removes any leading numbers.  I use those to order pictures in the desired order, but they will be renumbered.
def RemoveLeadingNumbers(passed_string:str):
    #Keep going until the string has no length or the first character is not a digit.
    while True:
        if len(passed_string) > 0:
            if passed_string[0].isdigit():
                passed_string = passed_string[1:]
                pass
            else:
                break
        else:
            break
    return passed_string

#Keep at bottom
if __name__ == "__main__":
    main()