# First prompt
def hello_name(user_name):
    
    print("hello_" + user_name.title() +"!")
          
hello_name("Username")

# Second Prompt

def first_odds():
    
    x = list(range(1,100,2))
    print(x)

first_odds()

# Third Prompt

def max_num_in_list(a_list):
        z= max(a_list)
        print(z)

number = (1,2,35,6,4)
        
max_num_in_list(number)

# Fourth prompt

def is_consecutive(b_list):
     return sorted(b_list) == list(range(min(b_list), max(b_list)+1))

y = [1,2,3,4,6]
w = [1,2,5,4,6,3]

print(is_consecutive(y))

print(is_consecutive(w))