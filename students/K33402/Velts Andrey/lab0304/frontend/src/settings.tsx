let DEBUG = true;
let HOST_URL = "https://angel.ru";
let BACKEND_URL = "https://api.angel.ru";

if (DEBUG) {
  HOST_URL = "http://angel.ru:3000";
  BACKEND_URL = "http://api.angel.ru:8000";
}

export { HOST_URL, BACKEND_URL };
