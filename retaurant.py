import datetime


class Resto():
    def __init__(self, owner, menu, Restoname):
        self.Restoname = Restoname
        self.owner = owner
        self.menu = menu

    def ShowMenu(self):
        for food in self.menu:
            print(food)


if __name__ == '__main__':
    Pratik = Resto("Pratik", ["Roti", "Paratha", "Fried Rice", "Biryani", "Papad",
                   "Pizza", "Momos", "Burgur", "Pasta", "Noodles", "Salad", "Soup"], "Food Corner")

    while True:
        print('Choose a Option:\n1. View Menu\n2.Order Food\n3.Give Feedback')
        user_choice = int(input())

        if user_choice == 1:
            Pratik.ShowMenu()

        if user_choice == 2:
            name = input("Enter Your Name : \n")
            order = input("Enter Order Items Separated by Comma: \n")
            orderedList = order.split(",")
            print(f"{name} , You have ordered {orderedList}")
            Confirmation = input(
                "Are you sure you want to order the things above?\nTYPE 'y' for yes or 'n' for no")
            if Confirmation == 'y' or Confirmation == 'Y':
                print(f"Thanks for Ordering Food\n Your Food will be served soon!")
                with open("orders.txt", "a") as y:
                    y.write(f"Ordered By {name}\nOrder: {orderedList}")

            elif Confirmation == 'N' or Confirmation == 'n':
                print(f"Argh! Nevermind!")
                exit()

        if user_choice == 3:
            time = datetime.datetime.now()
            namee = input("Enter Your Name Please : \n")
            feedback = input("Please enter your feedback : \n")
            with open('feedbacks.txt', "a") as f:
                f.write(f"By {namee} at {time}\nFeedback : " +
                        feedback + "\n\n")
