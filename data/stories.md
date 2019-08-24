## happy path
* greet
  - utter_greet
* number
  - utter_response1
* affirm
  - utter_first_topic
> check_topic

## topic affirm path
> check_topic
* affirm_topic
  - utter_elaborate
* affirm
  - timer_30s
  - utter_second_topic
* deny
  - utter_next_person

##topic deny path
> check_topic 
* deny
> check_vote

## vote affirm path
> check_vote
* affirm
   - utter_vote
* number

## vote deny path
> check_vote
* deny
  - utter_discuss
> check_discuss

## discuss affirm path
> check_discuss
* affirm
  - timer_5min
  - utter_continue
* number
> check_vote_2

## vote 2 affirm path
> check_vote_2
* majority
  - utter_majority
  - timer_5min
  - utter_continue 
 
## vote 2 deny path
> check_vote_2
* minority
  - utter_discuss
  
## discuss deny path
> check_ discuss
* deny
  - utter_end
* goodbye
  - funny_goodbye
  

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
