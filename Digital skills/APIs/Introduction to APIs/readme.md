# Introduction to APIs (How Computers Talk to Each Other)

In November 2025 we hosted a session on APIs (Application Programming Interfaces) and how to use them to get data from the internet without visiting a website manually. The link for which can be found [here](https://youtu.be/k2GUbQUA8qA).

The topic covered the basics of how software "talks" to other software using simple web addresses, and tools like [Postman](https://www.postman.com/) or your web browser to test them.

### Why is this useful?

1.  **Automation:** Instead of manually visiting a website to copy data (like the weather or stock prices), you can write a script to do it for you automatically every day.
2.  **Integration:** It allows different tools to work together. For example, you can make your website automatically post to Slack or Discord whenever a new file is uploaded.
3.  **Data Access:** Many organizations (like NASA, Museums, and Weather stations) provide free access to their data via APIs, allowing you to build your own creative projects.

### Pre-requisites

For this session, it helps to have a few basic tools ready.

1.  **A Web Browser**
    You already have this! Surprisingly, you can test many "Read-only" APIs simply by typing the address into your Chrome, Firefox, or Safari address bar.

2.  **A Code Editor**
    To run the scripts, you will need a place to write code.
    *   **VS Code:** A popular free editor for both Python and JavaScript.
    *   **Online Editors:** Websites like Replit or CodePen can also be used if you don't want to install anything.

3.  **Sample Data**
    We will be using a free, fun API that requires no passwords or "Keys" for these exercises:
    *   **The Random Dog API:** `https://dog.ceo/api/breeds/image/random`
    
    When you ask this address for data, it sends back a message telling you where to find a random picture of a dog.

## Exercises

### The Browser Test

Before writing code, let's see what the data looks like.
1.  Copy this URL: `https://dog.ceo/api/breeds/image/random`
2.  Paste it into your web browser's address bar and hit Enter.
3.  You will see text that looks somewhat like this:
    `{"message":"https://images.dog.ceo/breeds/beagle/n02088364_123.jpg","status":"success"}`

This format is called **JSON**. It looks a lot like a dictionary or a list. It is designed to be lightweight and easy for computers to read.

### Research an API

There are APIs for almost everything—movies, space, cats, history, and art.
Spend some time looking at [this list of public APIs](https://github.com/public-apis/public-apis). Find one that interests you.
*   Does it require an "API Key" (a password)?
*   Can you view it in your browser?
*   What kind of information does it give you (Images, Text, Numbers)?

## Python Exercise

For those comfortable with Python, we are going to write a script that "fetches" the dog data and prints out the image URL.

*Note: You may need the `requests` library. If you don't have it, you can install it by running `pip install requests` in your terminal.*

**The Challenge:**
Create a Python script that asks the API for a random dog 3 times and prints the result.

**Example Code:**

```python
import requests

# The address we want to talk to
url = "https://dog.ceo/api/breeds/image/random"

# Ask the server for the data
response = requests.get(url)

# The tool turns the raw text into a Python dictionary
data = response.json()

# We look for the 'message' inside the data, which holds the image link
print("Here is your dog image:")
print(data['message'])
```

## JavaScript Exercise

For those who prefer JavaScript, this is very common in web development. You can actually run this code directly in your browser's "Console" (Right Click -> Inspect -> Console) or in a file using Node.js.

**The Challenge:**
Write a function that fetches the data and logs the image URL to the console.

**Example Code:**

```javascript
const url = "https://dog.ceo/api/breeds/image/random";

// We use 'fetch' to go get the data
fetch(url)
  .then(response => response.json()) // Convert the text response into an object
  .then(data => {
    // 'data' is now an object we can use
    console.log("Here is your dog image:");
    console.log(data.message);
  })
  .catch(error => console.error("Something went wrong:", error));
```

## Further Reading

If you want to dive deeper into how computers communicate, we recommend reading about **HTTP Verbs** (GET, POST, PUT).
*   [Mozilla Developer Network (MDN) - What is an API?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
*   [Postman Learning Center](https://learning.postman.com/docs/getting-started/introduction/)

