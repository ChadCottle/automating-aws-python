# coding: utf-8
#run this by typing the following
#pipenv run ipython -i ipythonsession.py
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = sessio.resource('s3')
