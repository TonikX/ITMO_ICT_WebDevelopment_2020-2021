import { useState, FunctionComponent } from "react";
import { LostPetProps } from "types/store";
import { Button, Spinner, Post } from "components";
import { BACKEND_URL } from "settings";

export interface LostProps {
  lost: LostPetProps[];
  isLoading: boolean;
}

const LostCards: FunctionComponent<LostProps> = (props: LostProps) => {
  const { lost, isLoading } = props;

  if (isLoading) {
    return (
      <div className="Lost__content">
        <Spinner size="large" />
      </div>
    );
  }

  return (
    <div className="Lost__content">
      {lost &&
        lost.length > 0 &&
        lost.map((item) => (
          <div className="Lost__item">
            <div className="Lost__card">
              <img src={item.image} alt="Lost Card" />
              <div className="Lost__card-content">
                <span>
                  <b>Город: </b>
                  {item.city}
                </span>
                <span>
                  <b>Приметы: </b>
                  {item.description}
                </span>
                <span>
                  <b>Место: </b>
                  {item.location}
                </span>
                <span>
                  <b>Контакты: </b>
                  {item.contacts}
                </span>
              </div>
            </div>
            <span className="Lost__info-name">{item.name}</span>
            <span className="Lost__info-description">{`${item.gender} / ${item.age}`}</span>
          </div>
        ))}
    </div>
  );
};

const Lost: FunctionComponent<LostProps> = (props: LostProps) => {
  const { lost, isLoading } = props;
  const [postVisible, setPostVisible] = useState(false);

  const openPost = () => {
    console.log(2323);
    setPostVisible(true);
  };

  return (
    <div className="Lost">
      <h3>Обратите внимание</h3>
      <div className="Lost__header">
        <h1>
          Потерянные любмичики <br />
          ищут своих хозяев
        </h1>
        <div className="Lost__button">
          <Button mode="secondary" onClick={openPost}>
            Выставить объявление
          </Button>
          {postVisible && (
            <Post visible={postVisible} setVisible={setPostVisible} />
          )}
        </div>
      </div>
      <LostCards lost={lost} isLoading={isLoading} />
    </div>
  );
};

export default Lost;
