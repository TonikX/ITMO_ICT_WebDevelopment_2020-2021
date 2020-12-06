import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AppThunk } from "store";
import { LostPetsState, LostPetProps, PostPetProps } from "types/store";
import { getLost, createLost } from "api/lost";

const initialState: LostPetsState = {
  lost: [],
  error: null,
  isLoading: true,
};

const lostSlice = createSlice({
  name: "lost",
  initialState,
  reducers: {
    actionStart(state) {
      state.isLoading = true;
    },
    getLostSuccess(state, action: PayloadAction<LostPetProps[]>) {
      state.lost = action.payload;
      state.isLoading = false;
    },
    getLostFail(state, action: PayloadAction<string>) {
      state.error = action.payload;
      state.isLoading = false;
    },
    postLostSuccess(state, action: PayloadAction<LostPetProps>) {
      state.lost.push(action.payload);
      state.isLoading = false;
    },
  },
});

export const {
  actionStart,
  getLostSuccess,
  getLostFail,
  postLostSuccess,
} = lostSlice.actions;

export default lostSlice.reducer;

export const fetchLost = (): AppThunk => async (dispatch) => {
  try {
    const result = await getLost();
    dispatch(getLostSuccess(result));
  } catch (err) {
    if (err.response && "data" in err.response) {
      const error = Object.values<string>(err.response.data)[0];
      if (error) {
        dispatch(getLostFail(error));
      }
    }
  }
};

export const postLost = (lost: FormData): AppThunk => async (dispatch) => {
  try {
    const result = await createLost(lost);
    console.log(result);
    dispatch(postLostSuccess(result));
  } catch (err) {
    if (err.response && "data" in err.response) {
      const error = Object.values<string>(err.response.data)[0];
      if (error) {
        dispatch(getLostFail(error));
      }
    }
  }
};
