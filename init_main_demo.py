class Car:
    def __init__(self):
        print('In __init__')
    

def main123():
    print('Before calling Car.')
    car = Car()
    print('After calling Car.')

if __name__ == "__main__":
    main123()