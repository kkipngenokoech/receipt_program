#creating items for sale and their prices
item_1,price_1="novels",200.45
item_2,price_2="SMPS",600.65
item_3,price_3="calculator",2500

#creating a company that does the selling
company_name="pie_solutions"
company_address="39,mbagathi"
company_city="nairobi,kenya"

#closing statement
closing_message="\t\tthank you for shopping with us today"

#the receipt itself:
print("*"*50)
print("\t\t {}".format(company_name.title()))
print("\t\t {}".format(company_address))
print("\t\t {}".format(company_city))
print("="*50)
print("\tproduct name\tproduct price")
print("\t{}\t\t    shs{}".format(item_1.title(),price_1))
print("\t{}\t\t    shs{}".format(item_2.title(),price_2))
print("\t{}\t\tshs{}".format(item_3.title(),price_3))
print("="*50)
print("\t\t\tTotal ",price_1+price_2+price_3)
print("="*50)
print("\n{}\n".format(closing_message))
print("*"*50)