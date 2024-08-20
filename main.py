# Mark wants to bake a cake, and he needs to buy ingredients. He has a list of three ingredients: flour, sugar, and eggs.

# Mark has different priorities. 

# First, he checks if he has enough flour. 
# If he does, he'll bake the cake. 

# If he doesn't have enough flour, he checks if he has enough sugar. 

# If he has enough sugar, he'll bake a different dessert. If he doesn't have enough sugar, he checks if he has enough eggs.

# If he has enough eggs, he'll make scrambled eggs. If he doesn't have any of these ingredients, he'll make a sandwich.

# Write a program to help Mark decide what to make based on his ingredient availability and priorities.

has_flour = True 
has_sugar = True
has_eggs = True

if not has_flour:
  print("Mark will bake a cake")

else:
  if not has_sugar:
    print("Mark will bake a different dessert")
  else:
    if not has_eggs:
      print("Mark will make scrambled eggs")
    else:
      print("He will make a sandwich")
