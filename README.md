# Validate-Phone-Number
Validate Phone Number with Country, you will need to register at rapidapi and get a key.

# Phone Data Checker

The Phone Data Checker is a simple graphical user interface (GUI) application that validates phone numbers based on the country initials provided.

## Dependencies:
- `requests`
- `tkinter`

## How It Works:

### 1. Setup and Configuration:
- The script uses the `requests` library to interact with the [RapidAPI's phone number validation endpoint](https://phonenumbervalidatefree.p.rapidapi.com/ts_PhoneNumberValidateTest.jsp).
- Remember to set your RapidAPI key in the `headers` dictionary in place of `YOUR API KEY HERE`.

### 2. Graphical User Interface:
- The script uses `tkinter` to generate a GUI with:
  - Two input fields: One for the phone number and one for the country initials.
  - A "Check" button to trigger the validation.

### 3. Validation Process:
- When the "Check" button is pressed:
  1. The script retrieves the phone number and country initials provided.
  2. It sends these details to the RapidAPI endpoint to validate the phone number.
  3. Once a response is received, a message box pops up, showing detailed results about the entered phone number.

## Running the Script:
To run the Phone Data Checker, simply execute the Python script. You'll be presented with the GUI where you can enter your desired phone number and country initials. Click the "Check" button to validate and get results.

---

Remember to replace `YOUR API KEY HERE` with your actual RapidAPI key.
