### Daily Journal Api
1. Create a file called `daily-journal.db`
1. Run the sql commands in the `daily-journal.sql` file to set up the database
1. Run the debugger to start the server
1. To add tags to an entry, make a post request to `/entries` with this data:
        
        ```json
        {
            "entry": "adding tags",
            "concept": "python",
            "mood_id": 2,
            "tags": [2, 3]
        }
        ```
1. Modify the front end code to send a `tags` key with the entry data when creating an entry. The `tags` value should be an array of tag id's
