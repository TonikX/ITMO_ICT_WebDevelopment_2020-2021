import React, { useState, HTMLAttributes, FunctionComponent } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import RcMenu, { MenuItem } from "rc-menu";
import { Login } from "containers";
import { Button } from "components";
import { authLogout } from "store/user";
import { RootState } from "store/rootReducer";
import { ReactComponent as Logo } from "assets/logo.svg";

export type CollapseType = "clickTrigger" | "responsive";

const Menu = () => {
  let history = useHistory();
  let location = useLocation();
  const currentPage = `/${location.pathname.split("/")[1]}`;
  const navigateTo = ({ key }: { key: string }) => {
    history.push(key);
  };

  return (
    <RcMenu prefixCls="Menu" className="Menu" selectedKeys={[currentPage]}>
      <MenuItem key="/" onClick={navigateTo}>
        <span className="Menu-item-text">О приюте</span>
      </MenuItem>
      <MenuItem key="/pets" onClick={navigateTo}>
        <span className="Menu-item-text">Питомцы</span>
      </MenuItem>
      <MenuItem key="/charity" onClick={navigateTo}>
        <span className="Menu-item-text">Нужна помощь</span>
      </MenuItem>
      <MenuItem key="/events" onClick={navigateTo}>
        <span className="Menu-item-text">Мероприятия</span>
      </MenuItem>
      <MenuItem key="/lost" onClick={navigateTo}>
        <span className="Menu-item-text">Потеряшки</span>
      </MenuItem>
    </RcMenu>
  );
};

const Layout: FunctionComponent<HTMLAttributes<HTMLDivElement>> & {
  Sidebar: () => JSX.Element;
  Content: FunctionComponent<HTMLAttributes<HTMLDivElement>>;
} = ({ children }) => {
  if (!children) {
    return null;
  }
  return <section className="Layout">{children}</section>;
};

const Content: FunctionComponent<HTMLAttributes<HTMLDivElement>> = ({
  children,
  ...restProps
}) => {
  if (!children) {
    return null;
  }
  return (
    <main className="Content" {...restProps}>
      {children}
    </main>
  );
};

const Sidebar = () => {
  const dispatch = useDispatch();
  const [loginVisible, setLoginVisible] = useState(false);
  const { token, name, image } = useSelector((state: RootState) => state.user);

  const openLogin = () => {
    setLoginVisible(true);
  };

  const logout = () => {
    dispatch(authLogout());
  };

  return (
    <aside className="Sidebar">
      <div className="Sidebar__logo">
        <Logo />
      </div>
      <Menu />
      {!token ? (
        <div className="Sidebar__bottom">
          <Button mode="primary" onClick={openLogin}>
            Войти
          </Button>
          {loginVisible && (
            <Login visible={loginVisible} setVisible={setLoginVisible} />
          )}
        </div>
      ) : (
        <div className="Sidebar__bottom">
          <span className="Sidebar__bottom-name">Имя: {name}</span>
          <Button mode="primary" onClick={logout}>
            Выйти
          </Button>
        </div>
      )}
    </aside>
  );
};

Layout.Sidebar = Sidebar;
Layout.Content = Content;

export default Layout;
