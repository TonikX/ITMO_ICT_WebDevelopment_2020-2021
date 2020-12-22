import React, {
  FunctionComponent,
  useState,
  ChangeEvent,
  Dispatch,
  SetStateAction,
} from "react";
import Dialog from "rc-dialog";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { AiOutlineMail } from "react-icons/ai";
import { IoMdClose } from "react-icons/io";
import { authLogin } from "store/user";
import { Input, Button, FormStatus } from "components";
import { RootState } from "store/rootReducer";
import { HOST_URL } from "settings";

export interface LoginProps {
  visible: boolean;
  setVisible: Dispatch<SetStateAction<boolean>>;
}

export interface SlideProps {
  setCurrentSlide: Dispatch<SetStateAction<string>>;
  onClose: () => void;
}

const Auth: FunctionComponent<SlideProps> = (props) => {
  const { setCurrentSlide } = props;

  return (
    <>
      <h1>Авторизация</h1>
      <div className="Login__inner">
        <span className="Login__description">Выберите способ авторизации</span>
        <div className="Login__field Login__fiel">
          <Button
            mode="email"
            before={<AiOutlineMail />}
            onClick={() => setCurrentSlide("email")}
          >
            Через почту
          </Button>
        </div>
      </div>
    </>
  );
};

const Email: FunctionComponent<SlideProps> = (props) => {
  const { setCurrentSlide, onClose } = props;
  const dispatch = useDispatch();

  const [loginValue, setLoginValue] = useState({ username: "", password: "" });
  const handleEdit = (
    e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const name = e.target.name;
    setLoginValue({ ...loginValue, [name]: e.target.value });
  };

  const loginUserHandler = () => {
    dispatch(authLogin(loginValue.username, loginValue.password));
  };

  const { isLoading, error } = useSelector((state: RootState) => state.user);

  return (
    <>
      <h1>Войти через почту</h1>
      <h3 className="Login__title-info">
        или{" "}
        <Link to={`/signup/`} onClick={onClose}>
          зарегистрироваться
        </Link>
      </h3>
      <div className="Login__inner">
        {error && <FormStatus mode="error">{error}</FormStatus>}
        <div className="Login__field">
          <span className="Login__field-text">E-mail</span>
          <div className="Login__field-input">
            <Input
              name="username"
              type="email"
              value={loginValue["username"]}
              handleChange={handleEdit}
            />
          </div>
        </div>
        <div className="Login__field">
          <span className="Login__field-text">Пароль</span>
          <div className="Login__field-input">
            <Input
              name="password"
              type="password"
              value={loginValue["password"]}
              handleChange={handleEdit}
            />
          </div>
        </div>
        <div className="Login__buttons">
          <Button
            mode="primary"
            onClick={loginUserHandler}
            disabled={isLoading}
          >
            Войти
          </Button>
          <Button mode="link" onClick={() => setCurrentSlide("reset")}>
            Забыли пароль?
          </Button>
        </div>
      </div>
    </>
  );
};

const ResetPass = () => {
  //   const dispatch = useDispatch();
  const [isRequested, setIsRequested] = useState(false);
  const [emailValue, setEmailValue] = useState("");

  const handleEdit = (
    e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setEmailValue(e.target.value);
  };

  const resetPassHandler = () => {
    if (emailValue) {
      //   dispatch(authResetPass(emailValue));
      setIsRequested(true);
    }
  };

  const { isLoading, error } = useSelector((state: RootState) => state.user);

  //   if (isRequested && !isLoading && !error) {
  //     return (
  //       <>
  //         <h1>Восстановление пароля</h1>
  //         <div className="Login__inner Login__inner-reset">
  //           <ResetSuccess />
  //           <span className="Login__reset-help">
  //             Проверьте вашу почту, чтобы восстановить доступ к аккаунту.
  //           </span>
  //         </div>
  //       </>
  //     );
  //   }

  return (
    <>
      <h1>Восстановление пароля</h1>
      <div className="Login__inner">
        {error && <FormStatus mode="error">{error}</FormStatus>}
        <div className="Login__field">
          <span className="Login__field-text">E-mail</span>
          <div className="Login__field-input">
            <Input
              name="username"
              type="email"
              value={emailValue}
              handleChange={handleEdit}
            />
          </div>
        </div>
        <div className="Login__buttons">
          <Button
            mode="primary"
            onClick={resetPassHandler}
            disabled={isLoading}
          >
            Восстановить пароль
          </Button>
        </div>
      </div>
    </>
  );
};

const Login: FunctionComponent<LoginProps> = (props: LoginProps) => {
  const { visible, setVisible } = props;
  const [currentSlide, setCurrentSlide] = useState("auth");
  const onClose = () => {
    setVisible(false);
  };

  const renderSlide = () => {
    switch (currentSlide) {
      case "auth":
        return <Auth setCurrentSlide={setCurrentSlide} onClose={onClose} />;
      case "email":
        return <Email setCurrentSlide={setCurrentSlide} onClose={onClose} />;
      case "reset":
        return <ResetPass />;

      default:
        return null;
    }
  };
  return (
    <Dialog
      visible={visible}
      animation="zoom"
      maskAnimation="fade"
      onClose={onClose}
      prefixCls="Login"
      closeIcon={<IoMdClose />}
      destroyOnClose
      className="Login"
    >
      {renderSlide()}
    </Dialog>
  );
};

export default Login;
