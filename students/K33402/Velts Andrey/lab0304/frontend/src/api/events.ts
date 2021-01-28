import { axios } from "core";

export const getEventsSchedule = async () => {
  let { data } = await axios.get("/events/schedule/");
  return data;
};
