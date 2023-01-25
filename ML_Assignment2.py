#!/usr/bin/env python
# coding: utf-8

# In[6]:


import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
L1 = sorted(ages)
#1 sorting the given list and storing into a new list and displaying minimum and max age
print("Sorted list:",L1)
print("Min age =",sorted_ages_list[0],"Max age =",sorted_ages_list[-1])
min = L1[0]
max = L1[-1]


# In[18]:


#2 adding min and max to the list
L1.append(min)
L1.append(max)

length = len(sorted_ages_list)
print("After appending the elements: ",sorted_ages_list)

#Finding the median
print('median =',statistics.median(ages))
print('mean =',statistics.mean(ages))

#finding the sum
length = len(sorted_ages_list)
sum = 0
for i in L1:
  sum += i

# finding the average
average = sum/length
print("Average :",average)

# finding the range
Range = sorted_ages_list[-1] - sorted_ages_list[0]
print("Range :",Range)


# In[22]:


# Question 2
# empty dictionary called dog
dog = {}
#Adding the keys name, color, breed, legs, age to the dog dictionary
dog = {"name":'Pug', "color":"grey", "breed":'pugs', "legs":4, "age":5}
print(dog)
#Create a student dictionary and add first_name, last_name, gender, age, marital status,skills, country, city and address as keys for the dictionary



student = {
    "first_name":'Mahi',
    "last_name":'Pulagam', 
    "gender":'Female', 
    "age":'22',
    "marital status": 'Unmarried',
    "skills":['Cooking','Dancing','reading books'], 
    "country":'United states', 
    "city":'Overland park', 
    "address":'8112w,pointroyale'
}

#length of the student dictionary
print("\nThe length of Student dictionary is : ",len(student))
#value of skills and check the data type
print("\nType :",type(student['skills']))
#Modify the skills values by adding one or two skills
student['skills'].append("team lead")
print("\nThe skills are adding an extra skill:",student['skills'])
#Get the dictionary keys as a list
print("\nThe keys in student dictionary :",student.keys())
#Get the dictionary values as a list
print("\nThe values in student dictionary :",student.values())


# In[1]:


#question3
sisters = ('pinky','sony','mike')
brothers = ('john','nick','jones')
siblings = sisters+brothers
print (siblings)
father_mother = ('nike','Anshu')
print(father_mother)
family_members = siblings+father_mother
print(family_members)


# In[25]:


#question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
len(it_companies)
it_companies.add('Twitter')
print(it_companies)
new_companies = ('wipro','TCS','Accenture')
it_companies.update(new_companies)
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
#5 What is the difference between remove and discard
'''
The difference between remove and discard is if we want to delete an element in the set that is not
present in the set by using remove then gives an error whereas discard
doesn't show any error it just keeps the set un disturbed
'''
print("\ndiscard usage",it_companies.discard('Tekaroon'))
print(A|B)
print(A&B)
print(A.issubset(B))
print(A.isdisjoint(B))
print("\nJoining A with B:",A.union(B))
print("Joining B with A:",B.union(A))
C=A^B
print(C)
del(A)
del(B)
Set=set(age)
print(Set)
print("\nThe length of list is :",len(age),"and set is :",len(Set))


# In[26]:


#q5
import math

constant = math.pi
radius = 30

#Area of a circle Finding
area_of_circle = constant * radius * radius
print("Area :",area_of_circle)


# In[27]:


#q5
circum_of_circle= 2 * constant * radius
print("Circumference :",circum_of_circle)


# In[28]:


#q5
new_radius = float(input("Enter the radius value: "))
Area = constant * new_radius * new_radius

print("for given radius = ",new_radius,"\nArea :",Area)


# In[29]:


#q6
sentence = "I am a teacher and I love to inspire and teach people"

#splitting the string for getting the individual elements
Split = sentence.split(" ")
sp_set = set(Split)
print("Set: ",sp_set)
print("Number of unique words: ",len(sp_set))


# In[30]:


#q7
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")


# In[31]:


#q8
radius = 10
area = 3.14 * radius ** 2
print('The area of circle with radius {} is {} meters square.'.format(radius, area))  


# In[ ]:


#q9
import math
Num = int(input("Number of  students:"))
Lbs=[]
Wts=[]
for i in range(Num):
    Lbs.append(int(input()))
for b in Lbs:
    a=(math.floor((b/2.2046) * 100 ) )/ 100;
    Wts.append(a)
print(Wts)


# In[ ]:




