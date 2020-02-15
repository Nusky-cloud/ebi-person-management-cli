import requests

PERSON_API_BASE = "http://localhost:8080/person";
USERNAME = "admin";
PASSWORD = "password";

person_id = "";
	
def display_main_menu():
	print("\n==========Person Management==========");
	print("Create new person      => 1");
	print("Update existing person => 2");
	print("Fetch person details   => 3");
	print("Fetch all persons      => 4");
	print("Remove existing person => 5");
	print("Exit System            => 6");
	print("Please enter the number to proceed : ", end = "");
	user_input = input();
	
	if user_input == "1":
		create_or_update_person(False);
	elif user_input == "2":
		create_or_update_person(True);
	elif user_input == "3":
		fetch_person_details(False);
	elif user_input == "4":
		fetch_all_persons();
	elif user_input == "5":
		remove_person();
	elif user_input == "6":
		return;
	else:
		print('Please enter a valid number!\n');
		display_main_menu();

def create_or_update_person(is_update):
	print("\n==========Person Management - Create / Update Person==========");
	
	global person_id;
	person_id = "";
	if is_update:
		fetch_person_details(True);
	
	first_name = "";
	while not first_name.strip():
		print("\nFirst Name is mandatory!");
		print("Please enter person first name : ", end = "");
		first_name = input();
	
	last_name = "";
	while not last_name.strip():
		print("\nLast Name is mandatory!");
		print("Please enter person last name : ", end = "");
		last_name = input();
	
	person_age = "";
	while not person_age.isdigit():
		print("\nAge should be a number!");
		print("Please enter person age : ", end = "");
		person_age = input();
		if not person_age.strip():
			break;
	
	print("Please enter favourite color : ", end = "");
	favourite_color = input();
	
	print("Please enter hobbies separated by commas : ", end = "");
	hobbies = input();
	
	person_data = { "personId": person_id if is_update else None, "firstName": first_name.strip(), "lastName": last_name.strip(), "age": person_age.strip(), 
				"favouriteColor": favourite_color.strip(), "hobby": [] if not hobbies.strip() else hobbies.strip().split(",") };
	
	if is_update:
		response = requests.put(PERSON_API_BASE + "/update", json = person_data, auth = (USERNAME, PASSWORD));
		if response.status_code != 200:
			raise requests.HTTPError(response.json()['message']);
		print('Person updated successfully!');
	else:
		response = requests.post(PERSON_API_BASE + "/create", json = person_data, auth = (USERNAME, PASSWORD));
		if response.status_code != 201:
			raise requests.HTTPError(response.json()['message']);
		print('Person created successfully!');
		
	display_main_menu();

def fetch_person_details(forUpdate):
	if not forUpdate:
		print("\n==========Person Management - View One Person Details==========");
	
	global person_id;
	person_id = "";
	while not person_id.strip() or not person_id.strip().isdigit():
		print("\nPerson id should be a number and it is required!");
		print("Please enter person id : ", end = "");
		person_id = input();
	
	response = requests.get(PERSON_API_BASE + "/" + person_id.strip(), auth = (USERNAME, PASSWORD));
	if response.status_code == 200:
		print('Person fetched successfully!\n');
		person_data = response.json()['body'];
		
		if forUpdate:
			print("Person old values");
			print("-----------------");
		print("Person Id : ", person_data['personId']);
		print("First Name : ", person_data['firstName']);
		print("Last Name : ", person_data['lastName']);
		print("Age : ", person_data['age']);
		print("Favourite Color : ", person_data['favouriteColor']);
		print("Hobbies : ", ", ".join(person_data['hobby']) if len(person_data['hobby']) > 0 else "");
		if forUpdate:
			return;
	elif response.status_code == 204:
		print('Sorry, No record found for the provided person id!');
	else:
		raise requests.HTTPError(response.json()['message']);
	
	display_main_menu();

def fetch_all_persons():
	print("\n==========Person Management - View All Person Details==========");
	
	response = requests.get(PERSON_API_BASE + "/getAll", auth = (USERNAME, PASSWORD));
	if response.status_code == 200:
		print('All persons fetched successfully!\n');
		all_persons_data = response.json()['body'];
		
		print('Person Id\t||\tFirst Name\t||\tLast Name\t||\tAge\t||\tFavourite Color\t||\tHobbies');
		for person_data in all_persons_data:
			print(person_data['personId'], "\t||\t", person_data['firstName'], "\t||\t", person_data['lastName'], "\t||\t", person_data['age'], 
				"\t||\t", person_data['favouriteColor'], "\t||\t", ", ".join(person_data['hobby']) if len(person_data['hobby']) > 0 else "");
	elif response.status_code == 204:
		print('Sorry, No person records found!');
	else:
		raise requests.HTTPError(response.json()['message']);
	
	display_main_menu();

def remove_person():
	print("\n==========Person Management - Remove Person==========");
	
	existing_person_id = "";
	while not existing_person_id.strip() or not existing_person_id.strip().isdigit():
		print("\nPerson id should be a number and it is required!");
		print("Please enter person id : ", end = "");
		existing_person_id = input();
	
	response = requests.delete(PERSON_API_BASE + "/remove/" + existing_person_id.strip(), auth = (USERNAME, PASSWORD));
	if response.status_code == 200:
		print('Person removed successfully!');
	elif response.status_code == 204:
		print('Sorry, No record found for the provided person id!');
	else:
		raise requests.HTTPError(response.json()['message']);
	
	display_main_menu();

# Entry Point
display_main_menu();
