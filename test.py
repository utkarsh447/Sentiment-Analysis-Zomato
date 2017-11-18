from zomato import Zomato
z = Zomato("e63ba94f05815d6d297781b94f9bcd07")
# A call to categories endpoint from zomato API.
#z.parse("categories","")
# A call to restaurants endppoint from zomato 
# API with required parameters res_id
print("Enter The Category To check details of: \
	\n\t1. All Database Restaurant's sentiment analysis\
	\n\t2. Burger King Restaurant's sentiment analysis\
	\n\t3. Dominos Restaurant's sentiment analysis\
	\n\t4. McDonalds Restaurant's sentiment analysis\
	\n\t5. Haldiram's Restaurant's sentiment analysis")
choice=input("Your Choice: ")
print(choice)

if choice=='1':
	print("Burger King, Cannaught Place: ")
	z.parse("reviews","res_id=310448")
	print("\n")
	print("QDs, Hudson Lane: ")
	z.parse("reviews","res_id=4825")

elif choice=='2': #Burger King
# Burger King, Cannaught Place: 310448
# Burger King, Saket: 310078
# Burger King, Nehru Place: 310780
# Burger King, Rajouri Garden: 18216903
# Burger King, Vasant Kunj: 310723
	print("Burger King, Cannaught Place: ")
	z.parse("reviews","res_id=310448")
	print("/****************************************************************************************************************************/")
	print("\n")

	print("Burger King, Saket: ")
	z.parse("reviews","res_id=310078")
	print("/****************************************************************************************************************************/")
	print("\n")

	print("Burger King, Nehru Place: ")
	z.parse("reviews","res_id=310780")
	print("/****************************************************************************************************************************/")
	print("/****************************************************************************************************************************/")
	print("\n")

	# print("Burger King, Rajouri Garden: ")
	# z.parse("reviews","res_id=18216903")
	# print("\n")

	# print("Burger King, Vasant Kunj: ")
	# z.parse("reviews","res_id=310723")
	# print("\n")


elif choice=='3':
	# Dominos, Cannaught Place: 143
	# Dominos, Kamla Nagar: 207
	# Dominos, Saket: 219
	# Dominos, Greater Kailash: 202
	# Dominos, Pitampura: 214
	print("Dominos, Cannaught Place: ")
	z.parse("reviews","res_id=143")
	print("/****************************************************************************************************************************/")
	print("\n")

	print("Dominos, Kamla Nagar: ")
	z.parse("reviews","res_id=207")
	print("/****************************************************************************************************************************/")
	print("\n")

	print("Dominos, Saket: ")
	z.parse("reviews","res_id=219")
	print("/****************************************************************************************************************************/")
	print("/****************************************************************************************************************************/")
	print("\n")

	# print("Dominos, Greater Kailash: ")
	# z.parse("reviews","res_id=202")
	# print("/****************************************************************************************************************************/")
	# print("\n")

	# print("Dominos, Pitampura: ")
	# z.parse("reviews","res_id=214")
	# print("/****************************************************************************************************************************/")
	# print("\n")
elif choice=='4':
	# McDonalds, Nehru Place: 196
	# McDonalds, Cannaught Place: 177
	# McDonalds, Kamla Nagar: 190
	# McDonalds, Vasant Vihar: 171
	# McDonalds, Sarojini Nagar: 9657

	print("McDonalds, Nehru Place: ")
	z.parse("reviews","res_id=196")
	print("/****************************************************************************************************************************/")
	print("\n")

	print("McDonalds, Cannaught Place: ")
	z.parse("reviews","res_id=177")
	print("/****************************************************************************************************************************/")
	print("\n")

	print("McDonalds, Kamla Nagar: ")
	z.parse("reviews","res_id=190")
	print("/****************************************************************************************************************************/")
	print("/****************************************************************************************************************************/")
	print("\n")

	# print("McDonalds, Vasant Vihar: ")
	# z.parse("reviews","res_id=171")
	# print("/****************************************************************************************************************************/")
	# print("\n")

	# print("McDonalds, Sarojini Nagar: ")
	# z.parse("reviews","res_id=9657")
	# print("/****************************************************************************************************************************/")
	# print("\n")
elif choice=='5':
	print("Haldirams, Cannaught Place: ")
	z.parse("reviews","res_id=2298")
	print("/****************************************************************************************************************************/")
	print("\n")

	print("Haldirams, Janak Puri: ")
	z.parse("reviews","res_id=18277230")
	print("/****************************************************************************************************************************/")
	print("\n")

	print("Haldirams, Moti Nagar: ")
	z.parse("reviews","res_id=1097")
	print("/****************************************************************************************************************************/")
	print("\n")