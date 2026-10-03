# Web Development Fundamentals: APIs & HTTP

An **API (Application Programming Interface)** is a messenger that lets two different software applications talk to each other.

---

## Client vs. Server
* **Client:** The device or app that *asks* for information (like your web browser or a mobile app).
* **Server:** The powerful computer that *stores* data and *fulfills* the request (like a remote cloud computer running a database).

---

## HTTP Protocol & The Request-Response Cycle
* **HTTP (HyperText Transfer Protocol):** The standard language and set of rules that clients and servers use to talk to each other on the web.
* **Request & Response Cycle:**
  1. **Request:** The client sends a message to the server asking for something.
  2. **Processing:** The server reads the request and checks its logic or database.
  3. **Response:** The server sends back the result (data or an error message).

---

## HTTP Methods (The Actions)
* **GET:** Read or retrieve data from the server (e.g., loading a list of products).
* **POST:** Create new data on the server (e.g., signing up for a new account).
* **PUT:** Replace or fully update an existing resource (e.g., updating an entire user profile).
* **DELETE:** Remove a resource from the server (e.g., deleting a photo).

---

## Status Codes (The Results)
* **200 OK:** Standard success; the request worked perfectly.
* **201 Created:** Success; a new resource was successfully created (commonly used with POST).
* **400 Bad Request:** Client error; the server couldn't understand the request due to invalid syntax or missing data.
* **404 Not Found:** Client error; the requested page or data does not exist on the server.
* **500 Internal Server Error:** Server error; something broke on the server's end while processing the request.

---

## Headers & Body
* **Headers:** Metadata or extra info sent along with a message (e.g., authentication tokens, content types like `application/json`, or device details).
* **Body:** The actual data payload being sent or received (e.g., the JSON text containing a user's name and email during a signup request).
