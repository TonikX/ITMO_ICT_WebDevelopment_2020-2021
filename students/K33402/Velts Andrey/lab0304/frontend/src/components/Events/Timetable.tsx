import React, { FunctionComponent } from "react";
import { AiOutlineHeart, AiOutlineClockCircle } from "react-icons/ai";
import { classNames } from "utils";
import { EventProps } from "types/store";
import { format } from "date-fns";
import { utcToZonedTime } from "date-fns-tz";
import { parseUnix } from "utils";
import { ReactComponent as PawIcon } from "assets/icons/paw.svg";

export interface ScheduleItemProps {
  event: EventProps;
}

export interface TimetableProps {
  data: EventProps[];
  day: number;
}

const ScheduleItem: FunctionComponent<ScheduleItemProps> = ({
  event,
}: ScheduleItemProps) => {
  const { title, category, start_date, end_date } = event;
  const startDate = format(
    utcToZonedTime(parseUnix(start_date), "Europe/Moscow"),
    "H:mm"
  );
  const endDate = format(
    utcToZonedTime(parseUnix(end_date), "Europe/Moscow"),
    "H:mm"
  );

  return (
    <div
      className={classNames("Timetable__event", `Timetable__event-${category}`)}
    >
      <div className="Timetable__event-icon">
        {category === "physical" ? <PawIcon /> : <AiOutlineHeart />}
      </div>
      <div className="Timetable__event-content">
        <span className="Timetable__event-title">{title}</span>
        <div className="Timetable__event-meta">
          <div className="Timetable__event-time">
            <AiOutlineClockCircle />
            <span className="Timetable__event-time-text">
              {startDate}
              {" - "}
              {endDate}
              {" МСК"}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

const Timetable: FunctionComponent<TimetableProps> = (
  props: TimetableProps
) => {
  const { data, day } = props;
  let hours = [];
  const nowHour = new Date().getDate() === day ? new Date().getHours() : 14; // Get current hour of the day

  for (let i = nowHour; i < 24; i++) {
    hours.push(i + ":00");
  }

  return (
    <div className="Timetable">
      <ul className="Timetable__list">
        {hours.length &&
          hours.map((hour) => {
            let event = data.find(
              (event) => format(parseUnix(event["start_date"]), "H:ss") === hour
            );
            return (
              <li className="Timetable__item Timetable__item-empty" key={hour}>
                <div className="Timetable__item-timestamp">{hour}</div>
                <div className="Timetable__item-content">
                  {event ? (
                    <ScheduleItem event={event} />
                  ) : (
                    <div className="Timetable__item-tail"></div>
                  )}
                </div>
              </li>
            );
          })}
      </ul>
    </div>
  );
};

export default Timetable;
