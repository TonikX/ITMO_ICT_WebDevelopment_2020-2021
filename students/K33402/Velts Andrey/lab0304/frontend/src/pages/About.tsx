import { Button } from "components";
import about from "assets/img/about.png";

const AboutPage = () => {
  return (
    <div className="About">
      <div className="About__section">
        <h3>Полезная информация</h3>
        <h1>
          Приют домашних <br />
          животных — “Ангел”
        </h1>
        <div className="About__content">
          <p className="About__description">
            Приют для кризисных животных, а для кого-то и дом "Ангел", где
            находится около 300 различных животных. <br />
            <br /> Этих милашек Вы видели когда-то на улицах города, спасали их
            в трудных для них ситуациях. <br />
            <br /> Мы же дарим им любовь, тепло и лечение. Приют, рассчитан для
            кризисных животных. Содержание наших питомцев альтернативное, то
            есть все животные, проживают как домашние. <br />
            <br /> Лечатся, стерилизуются, проходят соц. адаптацию, получают
            первичные навыки образования и ищут свой дом.
          </p>
          <img src={about} className="About__image" alt="About Dog" />
        </div>
      </div>
      <div className="About__section About__section--time">
        <h1>За все время работы приюта</h1>
        <div style={{ height: "150px", overflow: "hidden" }}>
          <svg
            viewBox="0 0 500 150"
            preserveAspectRatio="none"
            style={{ height: "100%", width: "100%" }}
          >
            <path
              d="M-32.44,10.36 C149.99,150.00 402.64,-98.19 518.90,71.53 L500.00,150.00 L0.00,150.00 Z"
              style={{ stroke: "none", fill: "#caeee6" }}
            ></path>
          </svg>
        </div>
        <div className="About__content">
          <div className="About__cards">
            <div className="About__card">
              <div className="About__card-title">30000+</div>
              <div className="About__card-description">
                Рублей было собрано с момента основания приюта
              </div>
            </div>
            <div className="About__card">
              <div className="About__card-title">350+</div>
              <div className="About__card-description">
                Животных получили необходимую своевременную помощь благодаря Вам
              </div>
            </div>
            <div className="About__card">
              <div className="About__card-title">900+</div>
              <div className="About__card-description">
                Кг корма для собак и котов было куплено на собранные средства
              </div>
            </div>
            <div className="About__card">
              <div className="About__card-title">3+</div>
              <div className="About__card-description">
                Года с Вашей помощью мы лечим и кормим наших животных
              </div>
            </div>
          </div>
          <div className="About__help-button">
            <Button mode="secondary">Пожертвовать</Button>
          </div>
        </div>
        <div style={{ height: "150px", overflow: "hidden" }}>
          <svg
            viewBox="0 0 500 150"
            preserveAspectRatio="none"
            style={{
              height: "100%",
              width: "100%",
              transform: "rotate(180deg)",
            }}
          >
            <path
              d="M-32.44,10.36 C149.99,150.00 402.64,-98.19 518.90,71.53 L500.00,150.00 L0.00,150.00 Z"
              style={{ stroke: "none", fill: "#caeee6" }}
            ></path>
          </svg>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;
