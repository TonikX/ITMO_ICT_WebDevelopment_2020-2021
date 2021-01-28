import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AppThunk } from "store";
import { CharitiesState, CharityProp } from "types/store";
import { getCharities } from "api/charity";

const initialState: CharitiesState = {
  charities: [],
  error: null,
  isLoading: true,
};

const charitySlice = createSlice({
  name: "charity",
  initialState,
  reducers: {
    actionStart(state) {
      state.isLoading = true;
    },
    getCharitySuccess(state, action: PayloadAction<CharityProp[]>) {
      state.charities = action.payload;
      state.isLoading = false;
    },
    getCharityFail(state, action: PayloadAction<string>) {
      state.error = action.payload;
      state.isLoading = false;
    },
  },
});

export const {
  actionStart,
  getCharitySuccess,
  getCharityFail,
} = charitySlice.actions;

export default charitySlice.reducer;

export const fetchCharity = (): AppThunk => async (dispatch) => {
  try {
    const result = await getCharities();
    dispatch(getCharitySuccess(result));
  } catch (err) {
    if (err.response && "data" in err.response) {
      const error = Object.values<string>(err.response.data)[0];
      if (error) {
        dispatch(getCharityFail(error));
      }
    }
  }
};
