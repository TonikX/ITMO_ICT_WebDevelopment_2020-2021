import React, {
  useState,
  useEffect,
  ChangeEvent,
  Dispatch,
  SetStateAction,
  FunctionComponent,
} from "react";
import { useDispatch, useSelector } from "react-redux";
import { Button, Input, Select, FormStatus } from "components";
import { authSignup } from "store/user";
import { RootState } from "store/rootReducer";
import { SignupUserProps } from "types/store";
import countryData from "data/countryData.json";
import { ReactComponent as ConfirmedIcon } from "assets/icons/confirmed.svg";
import { ReactComponent as SignupIcon } from "assets/icons/signup.svg";
import { ReactComponent as Logo } from "assets/logo.svg";
import "styles/signup.css";

export interface RegisterProps {
  setCurrentTab: Dispatch<SetStateAction<string>>;
}

export interface SignupProps {
  tab?: string;
}

const Activate = () => {
  return (
    <>
      <div className="Signup__form">
        <h1>Активация аккаунта</h1>
        <p className="Signup__email--sent">
          Вы успешно активировали свой аккаунт! <br /> Теперь вы свободно можете
          пользоваться системой.
        </p>
        <Button mode="primary" to="/">
          Продолжить
        </Button>
      </div>
      <div className="Signup__icon Signup__icon--confirmed">
        <ConfirmedIcon />
      </div>
    </>
  );
};

const Register: FunctionComponent<RegisterProps> = (props: RegisterProps) => {
  // TODO: ВАЖНО!!! ДОБАВИТЬ MANAGERLINK
  const { setCurrentTab } = props;
  const dispatch = useDispatch();
  const { isLoading, error } = useSelector((state: RootState) => state.user);
  const [profileValue, setProfileValue] = useState<SignupUserProps>({
    email: "",
    first_name: "",
    last_name: "",
    phone_number: "",
    password1: "",
    password2: "",
    country: "",
    country_code: "",
    city: "",
  });
  const [errorsValue, setErrorsValue] = useState<SignupUserProps>({
    email: "",
    first_name: "",
    last_name: "",
    phone_number: "",
    password1: "",
    password2: "",
    country: "",
    country_code: "",
    city: "",
  });
  const [isRequested, setIsRequested] = useState(false);

  const handleEdit = (
    e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    let value: string | number = e.target.value;
    const name = e.target.name;
    if (name === "email") {
      value = value.toLocaleLowerCase();
    }
    setProfileValue({ ...profileValue, [name]: value });
  };

  const handleCountryEdit = (e: ChangeEvent<HTMLSelectElement>) => {
    const countryRow = countryData.find(
      (row) => row.countryName === e.target.value
    );
    if (countryRow) {
      const { countryCode: country_code, countryName: country } = countryRow;
      setProfileValue({ ...profileValue, country, country_code });
    }
  };

  const renderEdit = (name: string, type?: string, maxLength?: number) => {
    const value = profileValue[name];
    const error = errorsValue[name];
    return (
      <Input
        name={name}
        type={type}
        value={value}
        maxLength={maxLength}
        handleChange={handleEdit}
        bottom={error}
      />
    );
  };

  const validateInput = () => {
    const errors = errorsValue;
    Object.entries(profileValue).forEach(([key, value]) => {
      switch (key) {
        case "first_name":
          errors[key] = !value.length ? "Не должно быть пустым" : "";
          break;
        case "last_name":
          errors[key] = !value.length ? "Не должно быть пустым" : "";
          break;
        case "email":
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          errors[key] = !emailRegex.test(value) ? "Указан неверный email" : "";
          break;
        case "password1":
          errors[key] =
            value.length < 6
              ? "Пароль должен содержать минимум 6 символов"
              : "";
          break;
        case "password2":
          const { password1, password2 } = profileValue;
          errors[key] =
            !password2 || password1 !== password2
              ? "Пароли должны совпадать"
              : "";
          break;
        case "country":
          errors[key] = !value.length ? "Не должно быть пустым" : "";
          break;
        case "city":
          errors[key] = !value.length ? "Не должно быть пустым" : "";
          break;
        default:
          break;
      }
    });
    setErrorsValue({ ...errors });
    return Object.values(errorsValue).every((value) => !value);
  };

  const signup = () => {
    const isValid = validateInput();
    if (isValid) {
      dispatch(authSignup(profileValue));
      setIsRequested(true);
    }
  };

  useEffect(() => {
    if (isRequested && !error && !isLoading) {
      setCurrentTab("activate");
    }
  }, [isRequested, error, isLoading, setCurrentTab]);

  return (
    <>
      <div className="Signup__form">
        <h1>Регистрация</h1>
        {error && !isLoading && <FormStatus mode="error">{error}</FormStatus>}
        <div className="Signup__form-field Signup__form-field--multiple">
          <div className="Signup__field-content">
            <span className="Signup__field-content-name">Имя</span>
            <div className="Signup__field-content-input">
              {renderEdit("first_name", undefined, 30)}
            </div>
          </div>
          <div className="Signup__field-content">
            <span className="Signup__field-content-name">Фамилия</span>
            <div className="Signup__field-content-input">
              {renderEdit("last_name", undefined, 30)}
            </div>
          </div>
        </div>
        <div className="Signup__form-field">
          <div className="Signup__field-content">
            <span className="Signup__field-content-name">Почта</span>
            <div className="Signup__field-content-input">
              {renderEdit("email", "email")}
            </div>
          </div>
        </div>
        <div className="Signup__form-field">
          <div className="Signup__field-content">
            <span className="Signup__field-content-name">Моб. телефон</span>
            <div className="Signup__field-content-input">
              {renderEdit("phone_number", "tel", 30)}
            </div>
          </div>
        </div>
        <div className="Signup__form-field Signup__form-field--multiple">
          <div className="Signup__field-content">
            <span className="Signup__field-content-name">Пароль</span>
            <div className="Signup__field-content-input">
              {renderEdit("password1", "password")}
            </div>
          </div>
          <div className="Signup__field-content">
            <span className="Signup__field-content-name">Повторить пароль</span>
            <div className="Signup__field-content-input">
              {renderEdit("password2", "password")}
            </div>
          </div>
        </div>
        <div className="Signup__form-field">
          <div className="Signup__field-content">
            <span className="Signup__field-content-name">Страна</span>
            <div className="Signup__field-content-input">
              <Select
                value={profileValue["country"]}
                title={profileValue["country"]}
                name="country"
                bottom={errorsValue["country"]}
                handleChange={handleCountryEdit}
                isSignup
              >
                {countryData.map((row) => {
                  const { countryCode, countryName } = row;
                  return (
                    <option key={countryCode} value={countryName}>
                      {countryName}
                    </option>
                  );
                })}
              </Select>
            </div>
          </div>
        </div>
        <div className="Signup__form-field">
          <div className="Signup__field-content">
            <span className="Signup__field-content-name">Город</span>
            <div className="Signup__field-content-input">
              {renderEdit("city", undefined, 80)}
            </div>
          </div>
        </div>
        <div className="Signup__form-button">
          <div className="Signup__field-content">
            <Button mode="primary" onClick={signup} disabled={isLoading}>
              Создать аккаунта
            </Button>
          </div>
        </div>
      </div>
      <div className="Signup__icon Signup__icon--signup">
        <SignupIcon />
      </div>
    </>
  );
};

const Signup: FunctionComponent<SignupProps> = (props: SignupProps) => {
  const { tab } = props;

  const [currentTab, setCurrentTab] = useState("register");

  const renderTab = () => {
    switch (currentTab) {
      case "register":
        return <Register setCurrentTab={setCurrentTab} />;
      case "activate":
        return <Activate />;

      default:
        return null;
    }
  };

  useEffect(() => {
    if (tab) {
      setCurrentTab(tab);
    }
  }, [tab]);

  return (
    <div className="Signup">
      <div className="Background">
        <svg
          width="238"
          height="219"
          viewBox="0 0 238 219"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="Polygon Polygon-1"
        >
          <path
            d="M191.52 1.88116L140.916 190.735L2.66533 52.4845L191.52 1.88116Z"
            stroke="#067DFF"
            stroke-width="2"
          />
        </svg>
        <svg
          width="238"
          height="219"
          viewBox="0 0 238 219"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="Polygon Polygon-2"
        >
          <path
            d="M191.52 1.88116L140.916 190.735L2.66533 52.4845L191.52 1.88116Z"
            stroke="#067DFF"
            stroke-width="2"
          />
        </svg>
        <svg
          width="633"
          height="732"
          viewBox="0 0 633 732"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="Polygon Polygon-3"
        >
          <path
            d="M1.00006 2.54819L630.791 366.158L1.00003 729.768L1.00006 2.54819Z"
            stroke="#067DFF"
            stroke-width="2"
          />
        </svg>
        <svg
          width="633"
          height="732"
          viewBox="0 0 633 732"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="Polygon Polygon-4"
        >
          <path
            d="M1.00006 2.54819L630.791 366.158L1.00003 729.768L1.00006 2.54819Z"
            stroke="#067DFF"
            stroke-width="2"
          />
        </svg>
        <svg
          width="215"
          height="233"
          viewBox="0 0 215 233"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="Polygon Polygon-5"
        >
          <path
            d="M27.5063 2.48046L212.357 139.532L1.24133 231.092L27.5063 2.48046Z"
            stroke="#067DFF"
            stroke-width="2"
          />
        </svg>
        <svg
          width="215"
          height="233"
          viewBox="0 0 215 233"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="Polygon Polygon-6"
        >
          <path
            d="M27.5063 2.48046L212.357 139.532L1.24133 231.092L27.5063 2.48046Z"
            stroke="#067DFF"
            stroke-width="2"
          />
        </svg>
        <svg
          width="905"
          height="942"
          viewBox="0 0 905 942"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="Polygon Polygon-7"
        >
          <path
            d="M2.53336 314.982L723.933 314.983L363.233 939.733L2.53336 314.982Z"
            stroke="#067DFF"
            stroke-width="2"
          />
        </svg>
        <svg
          width="905"
          height="942"
          viewBox="0 0 905 942"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="Polygon Polygon-8"
        >
          <path
            d="M2.53336 314.982L723.933 314.983L363.233 939.733L2.53336 314.982Z"
            stroke="#067DFF"
            stroke-width="2"
          />
        </svg>
      </div>

      <div className="Section__wrapper">{renderTab()}</div>
    </div>
  );
};

export default Signup;
