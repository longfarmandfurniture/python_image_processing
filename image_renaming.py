import os
import shutil

def main():
    #Get directory and check status
    input_directory = input("Please enter the input directory: ")
    if os.path.isdir(input_directory) == False:
        print(f"{input_directory} is not a directory.")
        exit(0)
    
    #Find files and check results
    file_list = FindFiles(input_directory, "jPg,jpeg, png")
    if(len(file_list) <= 0):
        print(f"{input_directory} contains no matching files.")
        exit(0)
    
    #List if desired.
    if input(f"Found {len(file_list)} matching files, would you like to list them? (y/n) ").lower().startswith("y"):
        for x in file_list:
            print(x)

    #Replace original name with the folder name.  Easy way to give them generic names.
    rename_files_with_folder = input("Do you want to rename files with the folder name? (y/n) ").lower().startswith('y')
    
    #Sort files.
    file_list.sort()

    #Set and create output directory.
    output_directory = os.path.join(input_directory, "output")
    folder_name = os.path.basename(input_directory)
    if os.path.isdir(output_directory) == False:
        os.mkdir(output_directory)

    #Number used in naming.
    i = 0

    for file in file_list:
        #Get file name and remove any leading numbers, and get extension.
        filename = os.path.basename(file)
        filename = RemoveLeadingNumbers(filename)
        extension = filename[filename.rfind('.'):]

        #Completely rename each file with folder name if option selected.
        if rename_files_with_folder:
            filename = f"{str(i)}_{folder_name}{extension}"
        #Add prefix and only add underscore if no dash or underscore present.
        else:
            if filename.startswith("-") | filename.startswith("_"):
                filename = str(i) + filename
            else:
                filename = str(i) + "_" + filename

        #Copy to ouput.
        output_file = os.path.join(output_directory, filename)
        shutil.copyfile(file, output_file)

        #Increment for next file.
        i += 1



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