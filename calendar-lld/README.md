## Calendar LLD

Discuss how to add recurring events

### Requirements - 
- Create user:  Done
- Create calendar: Done
- Create event: Done
- Get events for a user in a day (w/ start and end time) Done
- Find available slots in a day (w/ start and end time): Done
- get conflicting slots in a day Done

### Entities - 
- user
- event
- calendar
- user_calendar

Relationship : user -> user_calendar -> calendar -> events

Why maintain user_calendar separately?
- We can let users have multiple calendars this way with different configuration / access
- When a calendar is shared with somebody, we can just ceate a new user_calendar for this new user with limited access defined by a new property called 'role'

### How is data stored in calendar?

Calendar:

    {
        "id": "c0",
        "name": "TestCalendar",
        "day_wise_events": {
            "10102023": [< event_1 >, < event_2 >],
            "11102023": [< event_3 >, < event_4 >]
        }
    }