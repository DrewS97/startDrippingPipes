# startDrippingPipes
This is a program that I made to send me a reminder text to have some faucets dripping if the temperature gets below a certain level.

Using Openweathermap's API, it grabs the hourly 48 hour forecast. Then, it determines if the temperature will drop below 18F in the next 24 hours.
If the temp will be that low or lower, a text message will be sent out to everyone in the "Phonebook" using Twilio's API.

This is automated using Windows Task Scheduler to run every night even if I'm not logged into my computer.
