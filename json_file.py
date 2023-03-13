import json

dicto = {'name' : 'kostas', 'age' : 17, 'interests' : ['Football', 'Coding']}
player = '{"name" : "Dimos", "age" : 17, "interests" : ["Calisthenics", "Coding"]} '

astring = json.dumps(dicto)
adict = json.loads(player)
print(f"My favorite hobby right now is {adict['interests'][1]}")

data = [ {'Name' : 'Dimos',
          'Age' : 17,
          'Interests' : ['Calisthenics', 'Coding']},
         {'Name' : 'Kostas',
          'Age' : 17,
          'Interests' : ['Football', 'Coding']},
         {'Name' : 'Aleksis',
          'Age' : 16,
          'Interests' : ['Football', 'Lol']},
         {'Name' : 'Paulos',
          'Age' : 17,
          'Interests' : ['Motorbikes', 'Box']} ] 
  
d = open('lekseis.py', 'a')
d.write('This is a new fucking line\n')
d.close()

    
    
