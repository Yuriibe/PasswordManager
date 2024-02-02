import json
import os

class PasswordManager:

    def __init__(self) -> None:
        self.dataBaseName = None
        self.option = None
        self.data = {"Index":[], "Name":[], "Password":[]}
        self.line_length = 20  # Length of the line of equal signs

    def getDataBaseName(self):
        return self.dataBaseName

    def createNewDb(self, dbName):
        self.dataBaseName = dbName
        path = "passwordSave/" + dbName + ".json"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print("=" * self.line_length)
        with open(path, "w") as write_file:
            json.dump(self.data, write_file)
       
    def get_files_from_folder(self):
        folder_path = "passwordSave/"
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return files

        
    def switch(self, firstInput):
        while True:
            if firstInput == 1:
                self.createNewDb()
                firstInput = None 
            if firstInput == 2:
                files = self.get_files_from_folder()
                for key, file in enumerate(files):
                    print(key)
                    print(file)
                existingDbIndex = int(input("DB Index"))                
                fileName = files[existingDbIndex]
                dot_index = fileName.find(".")
                if dot_index != -1:
                # Extract the part of the string before the dot
                    filtered_string = fileName[:dot_index]
                    self.dataBaseName = filtered_string
                    try:
                        with open("passwordSave/"+file, "r") as json_file:
                            self.data = json.load(json_file)
                        print("Data loaded successfully:")
                        print(self.data)
                    except FileNotFoundError:
                        print(f"File not found: {file}")
                    except json.JSONDecodeError as e:
                        print(f"JSON decoding error: {e}")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                firstInput = None 
            print("=" * self.line_length)
            print("1) Show existing password")
            print("2) Add new password")
            print("3) Delete password")
            print("4) Update password")
            print("5) Exit")
            inputForNewDB = input("What would you like to do? ")
            print(self.dataBaseName)
            print(self.data)
            try:
                inputForNewDB = int(inputForNewDB)
            except ValueError:
                print("Please enter a valid number.")
                continue

            match inputForNewDB:
                case 1:
                    print("Showing passwords...")
                    self.showPasswords()
                case 2:
                    nameInput = input("Input the name of the Password: ")
                    passwordInput = input("Input your Password: ")
                    self.addPassword(nameInput, passwordInput)
                case 3:
                    index = input("Enter Index: ")
                    self.deletePassword(int(index))
                case 4:
                    indexToChange = int(input("Welcher Index soll geändert werden: "))
                    newPassword = input("Enter New Password: ")
                    self.updatePassword(indexToChange,newPassword)
                case 5:
                    print("Exiting...")
                    break  
                case _:
                    print("Invalid option selected.")

    def showPasswords(self):
        min_length = min(len(lst) for lst in self.data.values())
        for i in range(min_length):
            print(f"Entry {i}:")
            for key in self.data:
                print(f"  {key}: {self.data[key][i]}")
            print()  
    
    def addPassword(self, name, password):
        index = len(self.data['Name'])
        print("index: " + str(index))
        self.data["Index"].append(index)
        self.data["Name"].append(name)
        self.data["Password"].append(password)
        path = "passwordSave/"+self.getDataBaseName()+".json"
        self.updateFile()

    def deletePassword(self, index):
        if all(int(index) < len(self.data[key]) for key in self.data):
            for key in self.data:
                print(self.data[key][index])
                del self.data[key][index]
            print(f"Entry at index {index} has been removed.")
            self.updateFile()
        else:
            print(f"Invalid index: {index}. No entry removed.")
            
    
    def updatePassword(self, index, newPassword):
        #keyToChange = input("Welchen Wert Möchtest du Ändern")
        if all(int(index) < len(self.data[key]) for key in self.data):
            for key in self.data:
                self.data["Password"][index] = newPassword
            self.updateFile()
    

    def updateFile(self):
        path = "passwordSave/"+self.getDataBaseName()+".json"
        with open(path, "w") as write_file:
            json.dump(self.data, write_file)


if __name__ == "__main__":
    password_manager = PasswordManager()
    print("=" * password_manager.line_length)
    print("PasswordManager".center(password_manager.line_length))
    print("=" * password_manager.line_length)
    print("1) Create new password database")
    print("2) Start with existing database")
    print("3) Cancel")

    try:
        firstInput = int(input("What do you want to do? "))
        password_manager.switch(firstInput)
    except ValueError:
        print("Invalid input. Please enter a number.")
