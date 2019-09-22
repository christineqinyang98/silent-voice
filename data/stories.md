## happy path
* greet
  - utter_greet
* number
  - utter_response 
* affirm
  - utter_first_topic
> check_topic

## topic affirm path
> check_topic
* affirm_topic
  - utter_elaborate
* affirm
  - utter_second_topic
* deny
  - utter_next_person
> check_topic

##topic deny path
> check_topic 
* deny_topic
   - utter_start_vote
> check_vote

## vote affirm path
> check_vote
* affirm
   - utter_vote
* number
   - utter_vote
> check_vote

## vote deny path
> check_vote
* deny
  - utter_discuss
> check_discuss

## discuss affirm path
> check_discuss
* affirm
  - utter_continue
> check_vote_2

## vote 2 affirm path
> check_vote_2
* majority
  - utter_majority
  - utter_continue 
> check_vote_2
 
## vote 2 deny path
> check_vote_2
* minority
  - utter_discuss_next
> check_discuss
  
## discuss deny path
> check_discuss
* deny
  - utter_end
* goodbye
  - utter_funny





