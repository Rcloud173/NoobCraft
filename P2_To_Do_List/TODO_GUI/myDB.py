import json

class Database:
    
    def add_user_data(self,name,email,password):
        
        with open('noobcraft/P2_To_Do_List/TODO_GUI/user_data.json', 'r') as rf:
            database = json.load(rf)

        if email in database:
            return 0
        else:
            database[email] = [name,password]
            with open('noobcraft/P2_To_Do_List/TODO_GUI/user_data.json', 'w') as wf:
                json.dump(database,wf)
                return 1
        

    def login_search(self,email,password):
        
        with open('noobcraft/P2_To_Do_List/TODO_GUI/user_data.json', 'r') as rf:
            database = json.load(rf)

            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                 return 0
            
    
    def task(self,title,priority,description):

        with open('noobcraft/P2_To_Do_List/TODO_GUI/tasks_data.json','r') as rf:
            database = json.load(rf)

            if title in database:
                return 0
            else:
                database[title] = [priority,description]
                with open('noobcraft/P2_To_Do_List/TODO_GUI/tasks_data.json', 'w') as wf:
                    json.dump(database,wf)
                    return 1
                    
                