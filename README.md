# Yelp Reviews Analysis

#### Yelp Dataset 
https://www.yelp.com/dataset/download

### Results
### Matching Results
| Business ID	          | Prediction  | Actual Rating |
| -----------             | ----------- |  -----------  |
| Xg5qEQiB-7L6kGJ5F4K3bQ  | positive    |  5.0          |
| yGMCl0vYigshkXiZFIDTNw  |	negative	|  2.0          |
| oFHvr1cAktvU-bQgrl4aPw  |	positive	|  4.0          |
| k2b3niokS_tosjah_rzCPw  |	neutral    	|  3.5          |
| r48H_sNUGmcRGX1LsEc2mg  |	positive	|  4.5          |

### Mis-Matched results
| Business ID	          | Prediction | Actual Rating |
| -----------             | -----------|  -----------  |
| j9bWpCRwpDVfwVT_V85qeA: |  positive  |  2.5          |
| G9-OvE0PBQtDZmnGEB3HEQ: |  positive  |  3.5          |
| w4yq1IRk0DHQE995giqjGg: |  positive  |  3.5          |
| i7_JPit-2kAbtRTLkic2jA: |  neutral   |  4.0          |
| NgQmlTGtYUQHJbzUBBHvfA: |  neutral   |  4.0          |


## Scores
- Accuracy = 0.8176666666666667
- Precision = 0.7067339474662129
- Recall = 0.623658457978303
- F1-score = 0.6626024052361132
- Cross Validation Score = [0.8067983 0.80225   0.8032008]


## Usage
``` 
python3 yelp_analysis.py
```
Can also run the ipython jupyter notebook
