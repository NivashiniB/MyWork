from basic import db, Puppy

#create#
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

# Read ####
all_puppies = Puppy.query.all()
print(all_puppies)

# Select by ID ###
puppy_1 = Puppy.query.get(1)
print(puppy_1)

#Filters ####
puppy_frankie = Puppy.query.filter_by(name = 'Frankie')
print(puppy_frankie.all())

#Update #######
first_pup = Puppy.query.get(1)
first_pup.age = 10
db.session.add(first_pup)
db.session.commit()
print(Puppy.query.all())

second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit(second_pup)