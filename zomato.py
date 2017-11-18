import urllib.request,json,sys
import codecs,json2html
from textblob import TextBlob
import json
import numpy as np
from keras.models import model_from_yaml
from keras.preprocessing import sequence
import h5py

with open('/home/utkarsh/.keras/datasets/imdb_word_index.json') as data_file:    
    data = json.load(data_file)

class Zomato:
    
    def __init__(self,api_key,response_content_type="application/json",base_url="https://developers.zomato.com/api/v2.1/"):
        if api_key:
            self.api_key = api_key
        else:
            print("NO API KEY GIVEN.")
            return
            
        self.response_content_type = response_content_type
        self.base_url = base_url
        self.response_content_type = response_content_type
        self.all_endpoints = ["categories",
                                "cities",
                                "collections",
                                "cuisines",
                                "establishments",
                                "geocode",
                                "location_details",
                                "locations",
                                "dailymenu",
                                "restaurant",
                                "reviews",
                                "search"
                            ]

        self.endpoint_param =  {"categories":{},
                                "cities":{"q":{'type':'string'},
                                        "lat":{'type':'double'},
                                        "lon":{'type':'double'},
                                        "city_ids":{'type':'string'},
                                        "count":{'type':'integer'}},
                                "collections":{"lat":{'type':'double'},
                                                "lon":{'type':'double'},
                                                "city_id":{'type':'integer'},
                                                "count":{'type':'integer'}},
                                "cuisines":{"lat":{'type':'double'},
                                            "lon":{'type':'double'},
                                            "city_id":{'type':'integer'}},
                                "establishments":{"lat":{'type':'double'},
                                                  "lon":{'type':'double'},
                                                  "city_id":{'type':'integer'}},
                                "geocode":{"required":["lat","lon"],
                                           "lat":{'type':'double'},"lon":{'type':'double'}},
                                "location_details":{"required":["entity_id","entity_type"],
                                                    "entity_id":{'type':'integer'},
                                                    "entity_type":{'type':'string'}},
                                "locations":{"required":["query"],
                                            "query":{'type':'string'},
                                            "lat":{'type':'double'},
                                            "lon":{'type':'double'},
                                            "count":{'type':'integer'}},
                                "dailymenu":{"required":["res_id"],
                                             "res_id":{'type':'integer'}},
                                "restaurant":{"required":["res_id"],
                                              "res_id":{'type':'integer'}},
                                "reviews":{"required":["res_id"],
                                           "res_id":{'type':'integer'},
                                           "start":{'type':'integer'},
                                           "count":{'type':'integer'}},
                                "search":{"entity_id":{'type':'integer'},
                                          "entity_type":{'type':'string'},
                                          "start":{'type':'integer'},
                                          "count":{'type':'integer'},
                                          "lat":{'type':'double'},
                                          "lon":{'type':'double'},
                                          "q":{'type':'string'},
                                          "radius":{'type':'double'},
                                          "cuisines":{'type':'string'},
                                          "establishment_type":{'type':'string'},
                                          "collection":{'type':'string'},
                                          "order":{'type':'string'},"sort":{'type':'string'}}
                              }
    
    def parse(self,endpoint,parameters=None):
        if endpoint not in self.all_endpoints:
            print("Not a valid endpoint.")
            print(self.all_endpoints)
            return
        all_parameters = ""
        parameters = parameters.replace(" ","")
        params = parameters.split(",")
        para_value = []
        for param in params:
            para_value.extend( param.split("="))
        endpoint_dict = self.endpoint_param[endpoint]
        
        if parameters:
            if "required" in endpoint_dict.keys():
                required_param_list = endpoint_dict["required"]
                if not all(required_param in para_value for required_param  in required_param_list):
                    print("Required value missing!!!")
                    return
            i = 0
            length = len(para_value)
            while i < length:
                if para_value[i] in self.endpoint_param[endpoint.lower()].keys():
                    all_parameters = all_parameters + str(para_value[i])+"="+str(para_value[i+1])+"&"
                else:
                    print("Parameter is not valid, use help to find the list of all parameter for a given endpoint.")
                    return
                i = i + 2
        else:
            if "required" in endpoint_dict.keys():
                print("Required value missing!!!!")
                return
                
        if all_parameters:
            all_parameters = all_parameters[:-1]
        self._execute(endpoint.lower(),all_parameters)
            
    def _execute(self,endpoint,parameter):
        url = self.base_url + endpoint + "?" + parameter
        print(url)
        req = urllib.request.Request(url)
        if self.response_content_type == "application/json": 
            req.add_header('Accept', self.response_content_type)
            req.add_header("user_key", self.api_key)  
            try:
                res = urllib.request.urlopen(req)
                print(res.getcode())
                reader = codecs.getreader("utf-8")
                json_data = json.load(reader(res))  
                #print(json2html.convert(json = json_data))
                i=0
                avgpositive=0
                avgnegative=0
                total=5
                while i<total:
                    print(json.dumps(json_data['user_reviews'][i]['review']['id'], indent=4, sort_keys=True))
                    test = (json.dumps(json_data['user_reviews'][i]['review']['review_text'], indent=4, sort_keys=True))
                    print(test)
                    splited = (test.split(" "))
                    cbow = [[]]
                    for words in test.split(" "):
                        if(words in data):
                            if(data[words]>=20000):
                                data[words]=0
                            cbow[0].append(data[words])
                        else:
                            cbow[0].append(0)

                    cbow = np.asarray(cbow)
                    cbow = cbow.tolist()
                    yaml_file = open('imdb_lstm_keras.yaml', 'r')
                    loaded_model_yaml = yaml_file.read()
                    yaml_file.close()
                    loaded_model = model_from_yaml(loaded_model_yaml)

                    loaded_model.load_weights("imdb_lstm_keras.h5")
                    #print("Loaded model from disk")

                    #k=5
                    loaded_model.compile(loss="mse", optimizer="adam", metrics=['accuracy'])

                    cbow = sequence.pad_sequences(cbow,maxlen=80)

                    #print("Towards 0 is good, Towards 1 is bad ")
                    print("Sentiment Analysis Value: ", analysis.sentiment.polarity)
                    print((loaded_model.predict(cbow)))
                    analysis = TextBlob(json.dumps(json_data['user_reviews'][i]['review']['review_text'], indent=4, sort_keys=True))
                    
                    if analysis.sentiment.polarity > 0:
                        avgpositive+=analysis.sentiment.polarity
                    elif analysis.sentiment.polarity < 0:
                        avgnegative+=analysis.sentiment.polarity
                    #print("\n")
                    i=i+1
                print('\nOverall Positive Sentiment Percentage Value:', (avgpositive/total)*100)
                print('Overall Negative Sentiment Percentage Value:', (avgnegative/total)*100)

            except urllib.request.HTTPError as e:
                print(str(e.code)+"\t"+e.reason)
                return
        elif self.response_content_type == "application/xml":
            req.add_header('Accept', self.response_content_type)
            req.add_header("user_key", self.api_key) 
            try:
                res = urllib.request.urlopen(req)
                print(res.code())
            except urllib.request.HTTPError as e:
                print(str(e.code)+"\t"+e.reason)
                return
        else:
            print("ERROR: Response content type can only be applcation/json or application/xml.")
            return
    
            
