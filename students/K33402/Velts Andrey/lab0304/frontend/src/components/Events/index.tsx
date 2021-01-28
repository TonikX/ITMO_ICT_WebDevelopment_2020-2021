import { useState, FunctionComponent } from "react";
import { format, getDate } from "date-fns";
import { utcToZonedTime } from "date-fns-tz";
import { ru } from "date-fns/locale";
import Tabs from "../Tabs";
import Timetable from "./Timetable";
import { EventsSuccessProps } from "types/store";
import { parseUnix } from "utils";

const { TabPane } = Tabs;

export interface EventsProps {
  events: EventsSuccessProps;
  isLoading: boolean;
}

const Events: FunctionComponent<EventsProps> = (props: EventsProps) => {
  const { events, isLoading } = props;
  const [previousMonth] = useState(new Date());
  const [currentDay, setCurrentDay] = useState(new Date());
  const [nextMonth] = useState(new Date());

  const selectDay = (key: string) => {
    console.log(key);
  };

  const getPreviousMonth = () => {
    previousMonth.setMonth(currentDay.getMonth() - 1);
    return format(previousMonth, "LLLL", { locale: ru });
  };

  const getNextMonth = () => {
    nextMonth.setMonth(currentDay.getMonth() + 1);
    return format(nextMonth, "LLLL", { locale: ru });
  };

  return (
    <div className="Events">
      <h3>Твори добро</h3>
      <h1>Мероприятия</h1>
      <div className="Events__months">
        <span className="Events__month">{getPreviousMonth()}</span>
        <span className="Events__month Events__month-selected">
          {format(currentDay, "LLLL", { locale: ru })}
        </span>
        <span className="Events__month">{getNextMonth()}</span>
      </div>
      <div className="Events__date">
        <Tabs className="Events__days" onChange={selectDay}>
          {events &&
            Object.entries(events).map(([key, value]) => {
              const day = getDate(
                utcToZonedTime(parseUnix(key), "Europe/Moscow")
              );
              return (
                <TabPane tab={day} key={key}>
                  <Timetable day={day} data={value} />
                </TabPane>
              );
            })}
        </Tabs>
      </div>
    </div>
  );
};

export default Events;
