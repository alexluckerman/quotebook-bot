# quotebook_bot
A GroupMe bot that informs users who have a quote book group when they aren't correctly posting quotes

In order to use, you'll need the process_quote function to be called each time the GroupMe bot webhook is called (I'm using Google Cloud Functions to do that). Also, a group ID and an auth token for user account DMs will be sent from is necessary. And finally, the bot must actually be created through the GroupMe developer site.
