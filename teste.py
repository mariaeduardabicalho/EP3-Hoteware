# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:20:07 2017

@author: steph
"""
from firebase import firebase
firebase = firebase.FirebaseApplication('https://ep3-hotware.firebaseio.com', None)
result = firebase.get('/users', None)
print(result)


