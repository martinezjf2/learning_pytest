
hello_world = 'Hello World'
print(hello_world)

# pip package management system to do specific tasks for packages
# install pytest by doing this command: pip install -U pytest

def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5
    
    
# to run python file run this code: python <directory path>
# to run pytest run this code: pytest <directory path>