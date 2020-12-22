import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AppThunk } from "store";
import { PetsState, PetProp } from "types/store";
import { getPets } from "api/pets";

const initialState: PetsState = {
  pets: [],
  error: null,
  isLoading: true,
};

const petsSlice = createSlice({
  name: "pets",
  initialState,
  reducers: {
    actionStart(state) {
      state.isLoading = true;
    },
    getPetsSuccess(state, action: PayloadAction<PetProp[]>) {
      state.pets = action.payload;
      state.isLoading = false;
    },
    getPetsFail(state, action: PayloadAction<string>) {
      state.error = action.payload;
      state.isLoading = false;
    },
  },
});

export const { actionStart, getPetsSuccess, getPetsFail } = petsSlice.actions;

export default petsSlice.reducer;

export const fetchPets = (): AppThunk => async (dispatch) => {
  try {
    const result = await getPets();
    dispatch(getPetsSuccess(result));
  } catch (err) {
    if (err.response && "data" in err.response) {
      const error = Object.values<string>(err.response.data)[0];
      if (error) {
        dispatch(getPetsFail(error));
      }
    }
  }
};
