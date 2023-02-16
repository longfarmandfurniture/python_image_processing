import os

def main():
    input_directory = input("Please enter the input directory: ")
    if os.path.isdir(input_directory) == False:
        print(f"{input_directory} is not a directory.")
        exit(0)
    
    file_list = FindFiles(input_directory, "jPg,jpeg, png")

    if(len(file_list) <= 0):
        print(f"{input_directory} contains no matching files.")
        exit(0)
    
    if input(f"Found {len(file_list)} matching files, would you like to list them? (y/n) ").lower().startswith("y"):
        for x in file_list:
            print(x)




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


#Keep at bottom
if __name__ == "__main__":
    main()