def wash_car(amount_paid : float):
    if amount_paid == 12.00:
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")
    if amount_paid == 6.50:
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

amount_paid = float(input("Enter the amount paid: "))

wash_car(amount_paid)