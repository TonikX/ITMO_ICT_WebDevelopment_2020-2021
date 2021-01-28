import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AppThunk } from "store";
import { EventsState, EventsSuccessProps } from "types/store";
import { getEventsSchedule } from "api/events";

const initialState: EventsState = {
  events: [],
  error: null,
  isLoading: true,
};

const eventsSlice = createSlice({
  name: "events",
  initialState,
  reducers: {
    actionStart(state) {
      state.isLoading = true;
    },
    getEventsSuccess(state, action: PayloadAction<EventsSuccessProps>) {
      state.events = action.payload;
      state.isLoading = false;
    },
    getEventsFail(state, action: PayloadAction<string>) {
      state.error = action.payload;
      state.isLoading = false;
    },
  },
});

export const {
  actionStart,
  getEventsSuccess,
  getEventsFail,
} = eventsSlice.actions;

export default eventsSlice.reducer;

export const fetchEvents = (): AppThunk => async (dispatch) => {
  try {
    const result = await getEventsSchedule();
    dispatch(getEventsSuccess(result));
  } catch (err) {
    if (err.response && "data" in err.response) {
      const error = Object.values<string>(err.response.data)[0];
      if (error) {
        dispatch(getEventsFail(error));
      }
    }
  }
};
