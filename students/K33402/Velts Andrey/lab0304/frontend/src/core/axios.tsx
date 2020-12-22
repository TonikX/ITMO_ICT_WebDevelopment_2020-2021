import axios from "axios";
import { BACKEND_URL } from "settings";

axios.defaults.baseURL = BACKEND_URL;

export default axios;
