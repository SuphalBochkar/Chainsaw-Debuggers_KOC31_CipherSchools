print()
names = ['Tanishka','Ashish','Vipul','Arpit','Krishna','Vinay','Sidharth','Rishikesh','Anushka','Anmol']
marks = [63,83,31,39,28,21,38,25,15,19]
updates = [-15,-22,-10,-17,+19,-9,-7,-16,-6,+3]

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
    updated_a[names[i]]=updated_marks[i] 

# Sorting the old dictionary                   
sorted_a=sorted(a.items(), key=lambda z:(z[1],z[0]), reverse=True)

# Sorting the old dictionary                   
sorted_updated=sorted(updated_a.items(), key=lambda z:(z[1],z[0]),reverse=1)
b=sorted_a
c=sorted_updated

# # !Top Ranker in one row
for i in range(len(b)):
    if c[0][0] == b[i][0] :
        print(f"Name: {c[0][0]}, New Marks {c[0][1]}, New Rank: 1, Old Marks {b[i][1]}, Old Rank: {i+1}  Rank Jump: {i}" ) 
print()


# ! Print All Students 
for i in range(len(c)):
    print(f"Rank: {i+1} ")
    print(f"Name: {c[i][0]}")
    print(f"New Marks: {c[i][1]}")
    for j in range(len(b)):
        if c[i][0] == b[j][0]:
                print(f"Rank Jump: {(j-i)}")
                print(f"Old rank: {j+1}")
                print(f"Old Marks: {b[j][1]}")
    print()

print()