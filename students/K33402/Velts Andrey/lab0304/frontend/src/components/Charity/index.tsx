import { FunctionComponent } from "react";
import { Button, Spinner } from "components";
import { CharityProp } from "types/store";
import { getPrecentage } from "utils";
import { BACKEND_URL } from "settings";
import banner1 from "assets/banners/pay.png";
import banner2 from "assets/banners/sms.png";
import banner3 from "assets/banners/thing.png";

export interface CharitiesProps {
  charities: CharityProp[];
  isLoading: boolean;
}

const CharityCardLarge: FunctionComponent<CharityProp> = (
  props: CharityProp
) => {
  const {
    id,
    title,
    description,
    goal_money,
    current_money,
    donation_times,
    image,
  } = props;
  const precentage = getPrecentage(current_money, goal_money);

  return (
    <div className="Charity__card" key={id}>
      <img
        src={`${BACKEND_URL}${image}`}
        alt="Charity Card"
        className="Charity__card-image"
      />
      <div className="Charity__card-content">
        <div className="Charity__card-title">{title}</div>
        <div className="Charity__card-description">{description}</div>
        <div className="Charity__card-fund">
          <span className="Charity__fund-total">{`${current_money} руб.`}</span>
          <div className="Charity__fund-progress">
            <span style={{ width: precentage }}></span>
          </div>
          <div className="Charity__fund-info">
            <span>Собрано {precentage}</span>
            <span>{`${goal_money} руб.`}</span>
          </div>
          <span className="Charity__fund-amount">
            Пожертвований: {donation_times}
          </span>
        </div>
      </div>
    </div>
  );
};

const CharityCardVerticall: FunctionComponent<CharityProp> = (
  props: CharityProp
) => {
  const { id, title, image } = props;

  return (
    <div
      key={id}
      className="Charity__card"
      style={{ backgroundImage: `url(${BACKEND_URL}${image})` }}
    >
      <div className="Charity__card-content">
        <div className="Charity__card-title">{title}</div>
        <div className="Charity__card-description">
          Срочная лечебная помощь необходима питмоцам нашего приюта
        </div>
        <div className="Charity__card-button">
          <Button mode="primary">Поддержать</Button>
        </div>
      </div>
    </div>
  );
};

const CharityCardMedium: FunctionComponent<CharityProp> = (
  props: CharityProp
) => {
  const { id, title, current_money, goal_money, donation_times, image } = props;
  const precentage = getPrecentage(current_money, goal_money);

  return (
    <div key={id} className="Charity__card">
      <img
        src={`${BACKEND_URL}${image}`}
        alt="Charity Card"
        className="Charity__card-image"
      />
      <div className="Charity__card-content">
        <div className="Charity__card-title">{title}</div>

        <div className="Charity__card-fund">
          <div className="Charity__fund-progress">
            <span style={{ width: precentage }}></span>
          </div>
          <div className="Charity__fund-info">
            <span>Собрано {precentage}</span>
            <span>{`${current_money} руб.`}</span>
          </div>
          <span className="Charity__fund-amount">
            Пожертвований: {donation_times}
          </span>
        </div>
      </div>
    </div>
  );
};

const CharityCards: FunctionComponent<CharitiesProps> = (
  props: CharitiesProps
) => {
  const { charities, isLoading } = props;

  if (isLoading) {
    return (
      <div className="Charity__cards Charity__cards--empty">
        <Spinner size="large" />
      </div>
    );
  }

  return (
    <div className="Charity__cards">
      {charities &&
        charities.length > 0 &&
        charities.map((charity, index) => {
          switch ((index + 1) % 3) {
            case 1:
              return <CharityCardLarge {...charity} />;
            case 2:
              return <CharityCardVerticall {...charity} />;
            case 3:
              return <CharityCardMedium {...charity} />;
            default:
              return <CharityCardMedium {...charity} />;
          }
        })}
    </div>
  );
};

const Charity: FunctionComponent<CharitiesProps> = (props: CharitiesProps) => {
  const { charities, isLoading } = props;

  return (
    <div className="Charity">
      <h3>Кто, если не мы</h3>
      <h1>Кампании по сбору пожертвований</h1>
      <div className="Charity__content">
        <div className="Charity__header">
          <div
            className="Charity__banner"
            style={{ backgroundImage: `url(${banner1})` }}
          >
            Автоплатеж
          </div>
          <div
            className="Charity__banner"
            style={{ backgroundImage: `url(${banner2})` }}
          >
            Sms-платеж
          </div>
          <div
            className="Charity__banner"
            style={{ backgroundImage: `url(${banner3})` }}
          >
            Помочь делом
          </div>
        </div>
        <CharityCards charities={charities} isLoading={isLoading} />
      </div>
    </div>
  );
};

export default Charity;
