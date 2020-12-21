from rest_framework import serializers
from timefhuman import timefhuman

from .models import *

import spacy
nlp = spacy.load("en_core_web_md")

from datetime import datetime
from dateutil import tz

from duckling import DucklingWrapper

class tfRequestResponseSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, data):
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz(data['timezone'])
        utc = timefhuman(data['request'].lower())
        if type(utc)==type(datetime.now()):
            utc = utc.replace(tzinfo=from_zone)
            central = utc.astimezone(to_zone)
            result = str(central)
        else:
            result=""

        if result!="":
            year=result[:4]
            month=result[5:7]
            day=result[8:10]
            hour=result[11:13]
            minutes=result[14:16]
            seconds=result[17:]
            result='{Year:' + year + ',Month:' + month + ',Day:' + day + ',Hour:' + hour + ',Minutes:' + minutes + ',Seconds:' + seconds + '}'

        data['detected_date_response']=result

        return data

    class Meta:
        model = timefhumanRequestResponse
        fields = ('request', 'timezone', 'detected_date_response')

class spRequestResponseSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, data):
        doc = nlp(data['request'])
        result="{"
        for ent in doc.ents:
            result += "'"  + str(ent.text) + "':'" + str(ent.label_) + "',"
        result += "}"

        data['entity_detect_response']=result

        return data

    class Meta:
        model = spacyRequestResponse
        fields = ('request', 'entity_detect_response')

"""class dkRequestResponseSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, data):
        d = DucklingWrapper()
        data['duckling_response']=d.parse(data['request'])

        return data

    class Meta:
        model = ducklingRequestResponse
        fields = ('request', 'duckling_response')"""
