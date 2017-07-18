#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "Number of people: ", len(enron_data)
no_of_features = len(enron_data[enron_data.keys()[0]])  
print "Number of features/person: ", no_of_features

count = 0;
for i in enron_data:
    if enron_data[i]["poi"] == 1:
        count += 1

print "Number of POI: ", count
print "\n"
print "James Prentice Information: ", enron_data["PRENTICE JAMES"]
print "\n"
print "Wesley Colwell Emails to POI: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Jeffrey K Skilling Stock Options: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Skilling Salary: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Lay Salary: ", enron_data["LAY KENNETH L"]["total_payments"]
print "Fastow Salary: ", enron_data["FASTOW ANDREW S"]["total_payments"]

count_salary = 0
valid_email = 0
for i in enron_data:
    if enron_data[i]["salary"] != "NaN":
        count_salary += 1
    if enron_data[i]["email_address"] != "NaN":
        valid_email += 1

print "\n"
print "Valid Email: ", valid_email
print "Listed salary: ", count_salary
