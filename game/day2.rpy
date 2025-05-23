label day2_intro:
    scene office_morning with fade
    play music "ost/morning.ogg" volume 0.5 fadein 2.0 loop

    a "Доброе утро, Георгий! Сегодня снова неспокойно — ночью в городских чатах появились фото мёртвой рыбы и жалобы на странный запах у воды."

    a "Министр экологии просит срочно доложить о ваших действиях. А ещё поступили новые обращения — теперь уже по поводу мусора и стихийных свалок у реки."
    
    g "Похоже, придётся разбираться и с отходами, и с водой..."

    a "Кого примем первым сегодня?"

    menu:
        "Житель с жалобой на свалку":
            jump case_dump
        "Владелец автомойки":
            jump case_carwash
        "Немного подумать о вчерашнем":
            jump case_thoughts


label case_thoughts:
    $ rating += 1

    if rating >= 5:
        g "Несмотря на то, что я действовал решительно, строго, кажется, еще есть куда стремиться"
    elif rating >= 0:
        g "Я сомневаюсь в том, что все их проблемы стоят моего внимания, но я сделал, что мог"
    else:
        g"Жители сомневаются в моей компетентности, но и они сами не решают свои проблемы"

    menu:
        "Житель с жалобой на свалку":
            jump case_dump
        "Владелец автомойки":
            jump case_carwash


label case_dump:
    show citizen at left

    "В кабинет заходит мужчина с распечатанными фотографиями."

    "Житель" "Здравствуйте! За городом появилась огромная свалка — мусор прямо у берега, всё стекает в реку. Никто не убирает, а запах стоит ужасный!"

    menu:
        "Попросить показать фото":
            "Житель" "Вот, смотрите — тут и покрышки, и канистры, и даже старая мебель..."
        "Спросить, кто выбрасывает мусор":
            "Житель" "Все подряд! И дачники, и какие-то грузовики по ночам."
        "Спросить, обращался ли уже в администрацию":
            "Житель" "Писал — только обещания. А теперь дети боятся гулять у воды!"

    g "Спасибо, мы займёмся этим."

    menu:
        "Организовать срочную уборку силами города":
            $ rating += 2
            "Житель" "Спасибо! Надеюсь, теперь порядок наведёте."
        "Поручить штрафовать нарушителей":
            $ rating += 1
            "Житель" "Штрафуйте, только бы убрали!"
        "Порекомендовать жителям самим убирать":
            $ rating -= 2
            "Житель" "Мы и так убираем, но мусорят снова!"

    hide citizen
    jump after_case3


label case_carwash:
    show carwash_owner at left

    "В кабинет заходит мужчина в рабочей одежде, на руках следы автошампуня."

    "Владелец автомойки" "Здравствуйте, у меня проблема — ко мне пришли с проверкой, говорят, что я сливаю грязную воду в ливнёвку. Но у меня нет денег на очистку!"

    menu:
        "Спросить, как утилизирует воду":
            "Владелец автомойки" "Просто в канализацию, как все."
        "Спросить, есть ли фильтры":
            "Владелец автомойки" "Нет, это дорого."
        "Спросить, были ли жалобы":
            "Владелец автомойки" "Соседи жалуются, что после дождя у них во дворе пена."

    g "Спасибо за честность."

    menu:
        "Обязать установить фильтры":
            $ rating += 1
            "Владелец автомойки" "Попробую найти деньги, но это сложно."
        "Выписать штраф":
            $ rating -= 1
            "Владелец автомойки" "Да за что! Я и так еле держусь."
        "Порекомендовать закрыться на время проверки":
            $ rating -= 2
            "Владелец автомойки" "Это разорение! Лучше бы помогли..."

    hide carwash_owner
    jump after_case3


label after_case3:
    a "Поступило тревожное сообщение: ночью кто-то слил неизвестную жидкость в реку. Экологи и полиция уже на месте, ищут виновных. Министр ждёт вашего решения."

    menu:
        "Позвонить министру":
            jump call_minister
        "Поручить помощнику подготовить отчёт":
            jump report_assistant


label call_minister:
    play music "ost/phone.ogg" volume 0.1

    p "Георгий, ситуация серьёзная. Если не принять меры — город может остаться без чистой воды. Какие ваши действия?"

    menu:
        "Ввести временный запрет на купание и забор воды из реки":
            $ rating += 2
            p "Решительно! Это поможет выиграть время для анализа."
        "Попросить министерство о помощи техникой":
            $ rating += 1
            p "Хорошо, направим мобильные лаборатории и очистные станции."
        "Сделать вид, что всё под контролем":
            $ rating -= 2
            p "Это опасно. Если что-то случится — ответственность на вас."

    stop music fadeout 1.0
    jump midday2


label report_assistant:
    a "Я подготовлю отчёт и отправлю министру. Но жители ждут объяснений!"

    jump midday2


label midday2:
    scene city with fade
    play music "ost/ambient_2.ogg" volume 0.5 fadein 2.0 loop

    a "В городе растёт тревога. В соцсетях обсуждают фотографии и ждут вашей реакции."

    menu:
        "Выступить с обращением к жителям":
            $ rating += 1
            g "Дорогие жители! Мы работаем над решением проблемы, организуем уборку и усиляем контроль."
        "Промолчать":
            $ rating -= 1
            a "Люди волнуются, что власти молчат."

    a "Вечером поступил новый сигнал: в реке обнаружены мёртвые утки. Экологи требуют срочных мер."

    menu:
        "Организовать выездную лабораторию":
            $ rating += 2
            a "Люди видят, что вы действуете."
        "Поручить разобраться полиции":
            $ rating += 1
            a "Полиция займётся расследованием."
        "Игнорировать":
            $ rating -= 2
            a "Жители возмущены бездействием."

    jump end_of_day2


label end_of_day2:
    scene office_evening with fade
    play music "ost/night.ogg" volume 0.3 fadein 2.0 loop

    a "День окончен. Сегодня вы приняли важные решения. Рейтинг среди жителей: [rating]."

    g "Завтра решающий день. Справимся ли мы?.."

    "{i}Георгий засыпает, но тревога не отпускает...{/i}"

    jump day3_intro
