#import Api

#print horizontal rule
def print_hr(val='='):       
    print("".join([val for i in range(0,154)]))

def doc_get_score_avg(ScoreData):
    score_sum = 0
    N_score = 0
    
    for val in ScoreData.values():       
        score_sum = score_sum + val["Score"]
        N_score = N_score + 1

    if N_score == 0:
        return None

    return score_sum/N_score

##def doc_get_composite_list(doc):
##    data_api = Api.Api('Package_Generic_Details').SKV({ 'Code': doc["Code"] })
##    data_composite =  data_api["Product_Composite"] #unique object identifier
##    data_composite_list = data_composite.split("::")
##
##    while len(data_composite_list)<3:
##        data_composite_list.append("")
##   
##    return data_composite_list


def doc_print_scores(doc):    
    if "ScoreData" not in doc.keys():
        print("ScoreData not available")
        return 
    print("_id:{0}".format(doc["_id"]))
    ScoreData = doc["ScoreData"]
    for key,val in ScoreData.items():
        print("Checkpoint:{0}\nScore:{1}\n".format(key, val["Score"]))        

def json_extract(obj, key, scalar=False):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    if not values:       
        raise KeyError("key {} not found".format(key))

    if scalar:
        return values[0]
    
    return values
