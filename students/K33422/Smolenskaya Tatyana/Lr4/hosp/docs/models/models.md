# Описание моделей данных

Информация о "проектировании" модели, описание итоговой "базы данных"

## Доктор
Doctor(AbstractUser):

    id = primary_key, индивидуален и уникален, создаётся автоматически
    fio = фио врача (будет "возвращаться")
    speciality = специальность (вписывается)
    
    education_types = (
        ('VSH', "Высшее"),
        ('VSN', "Высшее неоконченное"),
        ('SRD', "Среднее"),
        ('SRS', "Среднее специальное"),
    )
    
    education = выбор из уровней образования. Это минимальные значения, с которыми принимают в клинику
    birthdate = дата рождения
    work_years = трудовой стаж

## Кабинет
Cabinet(models.Model):

    number = primary_key, индивидуален и уникален (будет "возвращаться")
    owner = ответственный
    phone = номер телефона

## Расписание
Schedule(models.Model):

    id = primary_key, индивидуален и уникален, создаётся автоматически
    id_doctor = foreignkey от "Doctor"
    number_cabinet = foreignkey от "Cabinet"
    start_time = время начала
    end_time = время конца
    day = день недели

## Прейскурант
Price(models.Model):

    id = primary_key, индивидуален и уникален, создаётся автоматически
    name = название услуги (будет "возвращаться")
    price = стоимость (в рублях)

## Пациент
Patient(models.Model):

    id = primary_key, индивидуален и уникален, создаётся автоматически
    fio = фио пациента (будет "возвращаться")
    birthdate = дата рождения
    phone = номер телефона
    passport = паспортные данные

## Диагноз
Diagnosis(models.Model):

    id = primary_key, индивидуален и уникален, создаётся автоматически
    name = название диагноза (будет "возвращаться")

## Медкарта
Medcard(models.Model):

    id_patient = foreignkey от "Patient"
    id_diagnosis = foreignkey от "Diagnosis"
    start_date = дата установки диагноза
    status = статус заболевания

## Приём у врача
Meeting(models.Model):

    id = primary_key, индивидуален и уникален, создаётся автоматически
    id_patient = foreignkey от "Patient"
    id_doctor = foreignkey от "Doctor"
    id_price = foreignkey от "Price"
    date_meet = дата приёма
    time_meet = время приёма
    status = текущее состояние
    price_status = проверка оплаты