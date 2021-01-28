import { axios } from "core";
import { SignupUserProps, PasswordChangeProps } from "types/store";

/**
 * Request to the server to log out
 *
 * @param token - The access token
 *
 */
export const postUserLogout = async (token: string) => {
  await axios.post("/auth/logout/", null, {
    headers: {
      Authorization: `Token ${token}`,
    },
  });
};

/**
 * Request to the server for authentication of user
 *
 * @param username - The username of the user
 * @param password - The user's password
 * @returns The access token and user information
 *
 */
export const postUserLogin = async (username: string, password: string) => {
  let { data } = await axios.post("/auth/login/", {
    username,
    password,
  });
  return data;
};

/**
 * Request to the server for user registration
 *
 * @param user - The object with user fields
 * @returns The access token and user information
 *
 */
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
