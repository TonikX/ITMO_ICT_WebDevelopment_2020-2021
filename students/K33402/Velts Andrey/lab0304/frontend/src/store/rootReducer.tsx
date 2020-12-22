import { combineReducers } from "@reduxjs/toolkit";

import userReducer from "./user";
import petsReducer from "./pets";
import charityReducer from "./charity";
import lostReducer from "./lost";
import eventsReducer from "./events";

const rootReducer = combineReducers({
  user: userReducer,
  pets: petsReducer,
  charity: charityReducer,
  lost: lostReducer,
  events: eventsReducer,
});

export type RootState = ReturnType<typeof rootReducer>;
export default rootReducer;
