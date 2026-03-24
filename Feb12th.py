name = input("Enter the name: ")
age = int(input("Enter the age: "))
hobby = input("Enter the hobby: ")

if age <= 12:
    print(f"Hi {name}! You are a child who loves {hobby}. Keep enjoying your childhood!")

elif age <= 18:
    print(f"Hi {name}! You are a teenager who enjoys {hobby}. Great time to explore your passions!")

elif age <= 60:
    print(f"Hi {name}! You are an adult who likes {hobby}. Keep balancing work and fun!")

else:
    print(f"Hi {name}! You are a senior who enjoys {hobby}. Stay happy and healthy!")