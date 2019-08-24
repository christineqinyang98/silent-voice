## happy path
* greet
  - utter_greet
* number
  - utter_response1
* affirm
  - utter_first_topic

## topic path
* topic
  - utter_elaborate
* affirm
  - timer_30s
  - utter_


## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
