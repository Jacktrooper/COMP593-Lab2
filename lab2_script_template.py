def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'Full_Name': 'Jack Corso',
        'Frist_Name' : 'Jack',
        'Student_ID': 8557543,
        'Pizza_Toppings': 
        [
            'PEPPERONI', 'CHEASE', 'SPICE'
        ],
        'Movies': 
        [
            
            {
             'title': 'my hero accadima two heros', 
             'genra': 'Supernaturall'
            },
                        {
                'title': 'war of tomarrow',
                'genra': 'Acctsion'
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    about_me['Movies'].insert(1, 'harry potter')
    print_about_me(Moive_extra)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print(f" My name is {about_me['Full_Name'].title()} but you can call me Sir {about_me['Frist_Name'].title()} My student ID is {about_me['Student_ID']}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    toppings = 'SAUSE', 'HAM'
    about_me['Pizza_Toppings'].extend(toppings)
    for i,p in enumerate(about_me['Pizza_Toppings']):
        about_me['Pizza_Toppings'][i] = p.lower()
    about_me['Pizza_Toppings'].sort()
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nThe player list is:')
    for b in about_me['Pizza_Toppings']:
        print(f'- {b}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print('\nThe Movie genre list is:')
    for i,m in enumerate(about_me['Movies']):
        if i < len(about_me['Movies']) - 1:
            print(f'- {m["my hero accadima two heros"]}', end='')
    else:
        print(f'- {m["my hero accadima two heros"]}')
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    
    return
    
if __name__ == '__main__':
    main()