
# MatchingTweet2Label
When we have 2 files including JSON tweets and Label of Ids file. These script are aiming at matching them: Text --> Label
Sample:
- [Json file](https://raw.githubusercontent.com/quanap5/MatchingTweet2Label/master/2015_Nepal_Earthquake_en.json)
- [Label of ID](https://github.com/quanap5/MatchingTweet2Label/blob/master/2015_Nepal_Earthquake_en.csv)

-----
## Running
Step 1: Edit nlpearthquake_2CSV.py at file_in='------.json'
-python nlpearthquake_2CSV.py 

Step 2: Edit file Combine.py at `open('2015_Cyclone_Pam_en.csv', 'rb')`  and `with open('FromJsontoRaw2015_Cyclone_Pam_en.csv', 'rU')` corresponding to [file label](https://github.com/quanap5/MatchingTweet2Label/blob/master/2015_Nepal_Earthquake_en.csv) and output [file of step1](https://github.com/quanap5/MatchingTweet2Label/blob/master/FromJsontoRaw2015_Nepal_Earthquake_en.csv) 
-python Combine.py 

Step 3: Preprocessing [output of step2](https://github.com/quanap5/MatchingTweet2Label/blob/master/ab_combined_2015_nepal_eq_cf_labels.csv)
-python preprocessingSCV.py 

The last preprocessed file is [here](https://github.com/quanap5/MatchingTweet2Label/blob/master/ab_combined_2015_nepal_eq_cf_labels_Pre.csv)

