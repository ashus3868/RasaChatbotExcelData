## happy path
* greet
  - utter_greet
  
## say goodbye
* goodbye
  - utter_goodbye

## store data to excel deny Story
* add_data
  - Form_Info
  - form{"name": "Form_Info"}
  - form{"name": null}
* deny
  - utter_goodbye
  
## store data to excel affirm Story
* add_data
  - Form_Info
  - form{"name": "Form_Info"}
  - form{"name": null}
* affirm
  - action_save_data
  
## fetch info
* ask_info{"column":"email","occup":"trainer"}
  - action_fetch_data