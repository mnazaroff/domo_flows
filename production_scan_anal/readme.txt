
scanned boxes with an origin checkpoint with GBF role should not be expected to
have weight values as the GBF (currently) bypasses the scale (this should change
in the future)

datamatrixexists: can also mean if Code field is valid(there?)
all boxes destined(should arrive at) for 209


_id should be unique to a given box as there are now enough labels to not be recycled
_id entry should be updated as opposed to another record being created for  a given product that causes duplicate data
_id is related to code(i think)
package global should contain the necessary data and more reliable

package global and package generic data cannot(at this time) be joined together reliably(a lookup on _id, date, style, size, etc... should
improve reliability)

mongodb bound to have less counts than actual(as opposed to duplicate counts)


PackageGeneric info:

weigh data example document:
    _id:12088949
weight: will be the average (with noise reduction and will be used for the average)
CheckweigherResult (average)



Weights and Checkweights not sure the difference
Sample/Weights: samples used to calcualte the average

_id:12088949
DateCreate:2022-12-06T20:09:33.920+00:00
OriginCheckpointID:71
BlockID:"234MACL4"
Checkpoints:
    46:
        CheckpointID:46
        Date:2022-12-06T21:06:39.835+00:00
ScoreData:
    46:Array
ProductComposite:"p38::s21::cBULK"
ProductID:38
Size:"21"
Style:null
Content:"BULK"
CheckweigherResult:
    Event:"SamplesComplete"
    Cookie:"355ba3c2fa"
    Samples:Array
        0:21.80000114440918
        1:22.100000381469727
    Weights:
        0:21.80000114440918
        1:22.100000381469727
    CheckWeights:
        0:21.904077529907227
        1:21.967988967895508
        
Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /home/it/Dropbox/Programming/Python/domo_flows/domo_api/domo_create_dataset.py
getting dataset list...
parsing dataset list...
2022-12-06 17:29:17,340 - pydomo.foo - INFO - Created: {
    "id": "9e3e9118-4a7a-4dcf-a587-7e564b641ba1",
    "name": "MN_API_CheckpointScane_PackageGeneric",
    "rows": 0,
    "columns": 0,
    "schema": {
        "columns": [
            {
                "type": "STRING",
                "name": "_id"
            },
            {
                "type": "STRING",
                "name": "BlockID"
            },
            {
                "type": "LONG",
                "name": "Checkpoints"
            },
            {
                "type": "DOUBLE",
                "name": "CheckweigherResultAvg"
            },
            {
                "type": "DATETIME",
                "name": "DateCreate"
            },
            {
                "type": "LONG",
                "name": "OriginCheckpointID"
            },
            {
                "type": "STRING",
                "name": "ProductComposite"
            },
            {
                "type": "LONG",
                "name": "ProductID"
            },
            {
                "type": "STRING",
                "name": "Size"
            },
            {
                "type": "STRING",
                "name": "Style"
            },
            {
                "type": "STRING",
                "name": "Content"
            }
        ]
    },
    "owner": {
        "id": 545469307,
        "name": "Michael Nazaroff"
    },
    "createdAt": "2022-12-07T01:29:16Z",
    "updatedAt": "2022-12-07T01:29:17Z",
    "pdpEnabled": false,
    "policies": [
        {
            "id": 3607,
            "type": "open",
            "name": "All Rows",
            "filters": [],
            "users": [],
            "virtualUsers": [],
            "groups": []
        }
    ]
}
2022-12-06 17:29:17,376 - pydomo.foo - INFO - created dataset 9e3e9118-4a7a-4dcf-a587-7e564b641ba1
>>>         