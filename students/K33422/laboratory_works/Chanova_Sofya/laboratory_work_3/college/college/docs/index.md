# Организация учебной части колледжа

Данная документация описывает эндпоинты DRF проекта Лабораторной работы №3. 

#### Вариант: 
- №12 из курса «Основы баз данных»

#### Описание варианта:

Программная система, предназначенная для учебной части колледжа.
Обеспечивает хранение сведений о каждом преподавателе, о
дисциплинах, которые он преподает, номере закрепленного за ним кабинета, о
расписании занятий. В задачу диспетчера учебной части входит составление расписания.

#### Схема проекта:

    mkdocs.yml    # the configuration file
    docs/
        index.md  # the documentation homepage
        users/
              student.md
              teacher.md
              dispatcher.md
        api/
              schedule.md 
              groups.md
              subjects.md
              rooms.md
              grades.md
              teachings.md