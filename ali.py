#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dell
#
# Created:     05-02-2024
# Copyright:   (c) Dell 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# When input has to be taken from the user
# input the no of test cases
i = int(input("No of test cses"))
# Loop for i no of test cases
for j in range(i):
  # input the no of people in between and the height of ali and Gi-Hun
  N = int(input(" People"))
  K= int(input("Height"))
  l=[]
  # for the no of people
  for h in range(N):
 # range of height of all the people
    b= int(input("Rnge of height"))
    # converting to a list
    l.append(b)
    # for storing minimum no of people to be shot
  count=0
  # for checking the no of people who need to be shot
  for j in l:
    # if someone's height is greater than the height of ali then
    if j>K:
      # count value is incremented
      count+=1
  print(count)
# When input has to be taken from the user
# input the no of test cases
i = int(input("No of test cses"))
# Loop for i no of test cases
for j in range(i):
  # input the no of people in between and the height of ali and Gi-Hun
  N = int(input(" People"))
  K= int(input("Height"))
  l=[]
  # for the no of people
  for h in range(N):
 # range of height of all the people
    b= int(input("Rnge of height"))
    # converting to a list
    l.append(b)
    # for storing minimum no of people to be shot
  count=0
  # for checking the no of people who need to be shot
  for j in l:
    # if someone's height is greater than the height of ali then
    if j>K:
      # count value is incremented
      count+=1
  print(count)
