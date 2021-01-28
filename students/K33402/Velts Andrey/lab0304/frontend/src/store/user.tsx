import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import {
  UserState,
  SignupUserProps,
  PasswordChangeProps,
  UserSuccessProps,
} from "types/store";
import { AppThunk } from "store";
import {
  getUserAuthState,
  postUserLogin,
  postUserLogout,
  postUserSignup,
  postUserPasswordChange,
} from "api/user";

const initialState: UserState = {
  token: "",
  username: "",
  email: "",
  name: "",
  city: "",
  country: "",
  phone_number: null,
  error: null,
  isLoading: false,
};

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    actionStart(state) {
      state.isLoading = true;
    },
    authSuccess(state, action: PayloadAction<UserSuccessProps>) {
      const { token, user } = action.payload;

      localStorage.setItem("token", token);
      return {
        ...state,
        token,
        ...user,
        error: null,
        isLoading: false,
      };
    },
    passwordSuccess(state) {
      state.error = null;
      state.isLoading = false;
    },
    passwordFail(state, action: PayloadAction<string>) {
      state.error = action.payload;
      state.isLoading = false;
    },
    signupFail(state, action: PayloadAction<string>) {
      state.error = action.payload;
      state.isLoading = false;
    },
    authLogoutSuccess: (state) => initialState,
  },
});

export const {
  actionStart,
  authSuccess,
  authLogoutSuccess,
  passwordSuccess,
  passwordFail,
  signupFail,
} = userSlice.actions;

export default userSlice.reducer;

export const authLogin = (
  username: string,
  password: string
): AppThunk => async (dispatch) => {
  try {
    dispatch(actionStart());
    const result = await postUserLogin(username, password);
    dispatch(authSuccess(result));
  } catch (err) {
    if (err.response && "data" in err.response) {
      const error = Object.values<string>(err.response.data)[0];
      if (error) {
        dispatch(passwordFail(error));
      }
    }
  }
};

export const authCheckState = (): AppThunk => async (dispatch) => {
  const token = localStorage.getItem("token");
  if (token) {
    try {
      dispatch(actionStart());
      const user = await getUserAuthState(token);
      dispatch(authSuccess({ token, user }));
    } catch (err) {
      localStorage.removeItem("token");
    }
  }
};

export const authSignup = (user: SignupUserProps): AppThunk => async (
  dispatch
) => {
  try {
    dispatch(actionStart());
    const result = await postUserSignup(user);
    dispatch(authSuccess(result));
  } catch (err) {
    if (err.response && "data" in err.response) {
      const error = Object.values<string>(err.response.data)[0];
      if (error) {
        dispatch(signupFail(error));
      }
    }
  }
};

export const authLogout = (): AppThunk => async (dispatch) => {
  const token = localStorage.getItem("token");
  if (token) {
    try {
      await postUserLogout(token);
      dispatch(authLogoutSuccess());
    } catch (err) {
      console.log(err.toString());
    }
  }
  localStorage.removeItem("token");
};
