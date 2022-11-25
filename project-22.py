print()
names = ['Tanishka','Ashish','Vipul','Arpit','Krishna','Vinay','Sidharth','Rishikesh','Anushka','Anmol']
marks = [53,43,31,39,28,21,38,25,15,19]
updates = [-5,-22,-9,-7,+9,-19,-7,-3,-6,+3]

# Making The dictionary
a={}   
                     
# Updating the marks    
updated_marks=[] 
                      
# Arranging the names in order
updated_a={} 
                   
for i in range (len(names)):
    
    # Making the Dictionary of Names and Marks 
    a[names[i]]=marks[i]                  
    
    # Updating the marks    
    updated_marks+=[marks[i]+updates[i]]           
    
    # Making the Dictionary of Names and Updated-Marks 
    updated_a[names[i]]=updated_a[i]                    


