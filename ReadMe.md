## Please ReadMe! 

#Business context
Deel clients may add funds to their Deel account using their credit and debit cards. Deel has partnered with Globepay to process all of these account funding credit and debit card transactions. Globepay is an industry-leading global payment processor and is able to process payments in many currencies from cards domiciled in many countries. Deel has connectivity into Globepay using their API. Deel clients provide their credit and debit details within the Deel web application, Deel systems pass those credentials along with any relevant transaction details to Globepay for processing.

#Problem
Deel is experiencing a decline in the acceptance rate of credit and debit card payments processed by Globepay in the recent period. The “acceptance rate” is defined as the number of accepted transactions divided by the total attempted transactions

#Root Cause Analysis
The steps for analysing the root cause problem of this project will be as follows:

Hypothesis Formulation: Several hypothesis would be formulated the potential root causes. These includes:
Currency-conversion issues: Transactions are getting declined due to currency conversion issues.
Geographic Factors: Transactions are being declined based on the country they are initiated from.
Security Factors: Transactions are getting declined due to lack of extra transaction security, i.e. cvv is not provided.
Time Factor: Declined transaction increases during a certain time/period of the year. PS: the project data contains only 6 months of transaction data.
Transaction Value: Transactions are getting declined because due to the transaction value (amount).
The above listed hypothesis will be investigated using Data Exploration and Visualization techniques (as above).
Dataset description
external_ref The card expiry year. Format: 4 digits. For example (_0fqf75KiPa0iiviKCSsU)
date_time The timestamp of the transaction.
state The binary state of the transaction. For example: Accepted or Declined.

chargeback If the transaction has been chargedback. For example: True or False
amount The amount that has been charged from the card.
currency The three-character ISO currency code.
country The two-character ISO country code of the card.
rates The exchange rate used. Funds are settled to you in USD.


# Submission Files Description
The submission folder contains the following files: 
- DeelPresentation.pdf - a presentation file of my findings. 
- Deel.ipynb - Jupyter notebook containing python codes, graphs, assumptions, and thought process.
- acceptance.csv - acceptance report data 
- chargeback.csv - chargeback report data
- Dee-Logo.png - Deel Company Logo
- DeelApp Folder - this folder contains:
        - app.py : python codes to launch the dash application 
        - requirements.txt : required modules to run the app - please install before running app.py - ``` pip install -r requirements.txt ```
        - asset folder : the application assets (dependent files)


  
        



