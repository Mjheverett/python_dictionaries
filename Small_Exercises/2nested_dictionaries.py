ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# Write a python expression that gets the email address of Ramit.
# Write a python expression that gets the first of Ramit's interests.
# Write a python expression that gets the email address of Jasmine.
# Write a python expression that gets the second of Jan's two interests.

ramit_email = ramit["email"]
print(ramit_email)

ramits_first_interest = ramit["interests"][0]
print(ramits_first_interest)

friends = ramit["friends"]
jasmines_email = friends[0]["email"]
print(jasmines_email)

jans_second_interest = friends[1]["interests"][1]
print(jans_second_interest)