import { axios } from "core";
import { SignupUserProps, PasswordChangeProps } from "types/store";

export const postUserLogout = async (token: string) => {
  let { data } = await axios.post("/auth/logout/", null, {
    headers: {
      Authorization: `Token ${token}`,
    },
  });
  return data;
};

export const postUserLogin = async (username: string, password: string) => {
  let { data } = await axios.post("/auth/login/", {
    username,
    password,
  });
  return data;
};

export const postUserSignup = async (user: SignupUserProps) => {
  let { data } = await axios.post("/auth/signup/", user);
  return data;
};

export const postUserPasswordChange = async (
  token: string,
  password: PasswordChangeProps
) => {
  let { data } = await axios.post("/auth/password/change/", password, {
    headers: {
      Authorization: `Token ${token}`,
    },
  });
  return data;
};

export const getUserAuthState = async (token: string) => {
  let { data } = await axios.get("/user/", {
    headers: {
      Authorization: `Token ${token}`,
    },
  });
  return data;
};
