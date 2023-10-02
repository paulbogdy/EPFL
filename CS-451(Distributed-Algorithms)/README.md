# Distributed Algorithms (CS-451)

This file contains the notes I took during the 2023 DA [(CS-451)](https://dcl.epfl.ch/site/education/da) course. The notes are ordered by topics, rather then by courses, and they contain the most relevant informations in my opinion (Not detailed).

**NOTE:** The notes are meant to contain all the information presented during the courses.

### Class Structure:
* **Lecture** Monday 13:15 - 15:00 [(CM13)](https://plan.epfl.ch/?room==CM%201%203) 
* **Exercises** Monday 15:15 - 12:00 (TBD)
* **Project** Tuesday 8:15 - 11:00 [(CE12)](https://plan.epfl.ch/?dim_floor=1&lang=en&dim_lang=en&tree_groups=centres_nevralgiques%2Cmobilite_acces_grp%2Censeignement%2Ccommerces_et_services&tree_group_layers_centres_nevralgiques=information_epfl%2Cguichet_etudiants&tree_group_layers_mobilite_acces_grp=metro&tree_group_layers_enseignement=&tree_group_layers_commerces_et_services=&baselayer_ref=grp_backgrounds&map_x=2533298&map_y=1152497&map_zoom=14) 
* Number of Credits: **8**

### Evaluation:
* Project | 30% | individually
* Final Exam | 70% | theoretical | closed books

## Content

* Bitcoin Uses a lot of energy

### Broadcast

* Send a message to all machines
* Failure detector implemented by a heartbeat messages
    * Reliable
    * Unreliable (Takes too long for communication)
* Notification is a broadcast
* Best-effort broadcast (beb)
    * Request: <bebBroadcast, m> (by machine)
    * Indication <bebDeliver, src, m> (by other mcahine)
    * Validity -> If 2 proccesses are correct (never fails), every broadcast by a is delivered by b
    * No duplication -> No message is delivered more than once
    * No creation -> No message is delivered unless it was broadcasted 
* (Regular) Reliable broadcast
    * Best-effort
    * Agreement -> For any message, if any **correct** process delivers m, then every process delivers m
* Uniform (reliable) broadcast
    * Uniform Agreement -> For any message, if **any** process delivers m, then every process delivers m

## Useful links:
* [Project submissions rules](https://docs.google.com/document/d/1Ai3tQeaTLD0p_2HrVTlONOUskoEExj1HdVOlfIbHdXQ)
* [Where to submit the project](https://cs451-submissions.epfl.ch:8083/)
* [Course Book](https://cdn.inst-fs-dub-prod.inscloudgate.net/ebb174db-c660-4183-b0e2-65e5b8a73cea/Introduction%20to%20Reliable%20and%20Secure%20Distributed%20Second%20Edition%202.pdf?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9lYmIxNzRkYi1jNjYwLTQxODMtYjBlMi02NWU1YjhhNzNjZWEvSW50cm9kdWN0aW9uJTIwdG8lMjBSZWxpYWJsZSUyMGFuZCUyMFNlY3VyZSUyMERpc3RyaWJ1dGVkJTIwU2Vjb25kJTIwRWRpdGlvbiUyMDIucGRmIiwidGVuYW50IjoiY2FudmFzIiwidXNlcl9pZCI6bnVsbCwiaWF0IjoxNjk2MjI0ODAwLCJleHAiOjE2OTYzMTEyMDB9.rSJF7xGv_9VsEXS_2HzpasDlYptePXcC-sPqIAJLUab0b2lzYARBOC9lAbQjbiKAfAYgXQhstrFM9z1B1zvzZw&download=1&content_type=application%2Fpdf)