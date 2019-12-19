def helloWorld():
    print("Hello World!")

def threeHello():
    for i in range(3):
        helloWorld()
        
if __name__ == "__main__":
    threeHello()
