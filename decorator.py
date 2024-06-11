def greet(fx):
    print("welcome")
    fx()
    print("bye")





@greet 
def hello():
    print("hello world")
hello() 