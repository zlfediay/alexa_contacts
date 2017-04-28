This application looks up contacts by first and last name, providing a description of the contact via Amazon Alexa.

Instructions for testing the Alexa skill:

1. Log into or create an account for the Amazon developer portal at https://developer.amazon.com/

2. Click the Alexa button (third from the right on top nav)

3. Click 'Get started' under Alexa Skills Kit

4. Click the Add New Skill button on the top right

5. For name field, enter: Contacts. For Invocation Name, enter: contacts.

6. Click Next

7. Copy the contents of the IntentSchema.json file in the folder speech_assets into the Intent Schema window

8. Under custom slop types, click Add Slot Type. Name it LAST_NAMES. Paste in the contents of the LastNames.txt file in the speech_assets folder and click Save.

9. Copy the contents of the SampleUtterances.txt file from the speech_assets folder into the Sample Utterances window and save it.

10. Click Next

11. Change service endpoint to HTTPS

12. Click the North America region textbox

13. Enter the URL that was sent in my message (looks like execute-api...)

14. Click Next

15. Select the radio button 'My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority'

16. Click next

You can now test the skill by typing responses into the Service Simulator. You can also test the skill using an Amazon Echo that is connected to the account you logged in with. Try it out by saying 'Alexa, open Contacts.'