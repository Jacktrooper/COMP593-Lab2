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
                'genre': 'Supernaturall'
            },
            {
                'title': 'war of tomarrow',
                'genre': 'Acctsion'
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    about_me['Movies'].insert(1, {'title' : 'love is war','genra' : 'Romace'})
    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ('SAUSE', 'HAM'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(me):
    print(f" My name is {me['Full_Name'].title()} but you can call me Sir {me['Frist_Name'].title()} My student ID is {me['Student_ID']}")
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(me, toppings):
    toppings = 'SAUSE', 'HAM'
    me['Pizza_Toppings'].extend(toppings)
    for i,p in enumerate(me['Pizza_Toppings']):
        me['Pizza_Toppings'][i] = p.lower()
    me['Pizza_Toppings'].sort()

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(me):
    print('\nThe Pizza Toppings list is:')
    for b in me['Pizza_Toppings']:
        print(f'- {b}')

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(me):
    print('\nThe Movie genre list is:')
    Movie_genre = [g["Movies"].upper() for g in me["genre"]]
    Movie_genres = ', '.join(Movie_genre)
    print(Movie_genres)

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(me):
    print('\nThe Movie genre list is:')
    Movie_genre = [g["Movies"].upper() for g in me["genre"]]
    Movie_genres = ', '.join(Movie_genre)
    print(Movie_genres)
    
if __name__ == '__main__':
    main()