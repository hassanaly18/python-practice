class Father: 
    def get_last_name(self): 
        return "Smith" 
        
    def get_eye_color(self): 
        return "Green" 
 
class Mother: 
    def get_eye_color(self): 
        return "Blue" 
 
# Child inherits from BOTH Father and Mother 
class Child(Father, Mother): 
    pass 
 
# Create an object of the Child class 
c = Child() 
 
# It has access to methods from all parents 
print(f"Last Name: {c.get_last_name()}") 
print(f"Eye Color: {c.get_eye_color()}") 