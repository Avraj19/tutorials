# creat a little program that askes the user for the following details;
# name, high, favorite color, a secrate number,

# capture input and tailor a welcome message without secrete number


user_name = input("Enter your name: ")
user_height = input("Enter your height in cm: ")
user_color = input("Enter your favourite color: ")
user_secrete_number = input("Enter your a secrete number : ")

print(f"Hi {user_name}, welcome to Sparta Global,"
      f" wow you are tall at {user_height} cm."
      f" What a coincidences my favorite color is {user_color} too.")
