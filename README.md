# курсовая работа по базовой части
## Из доп. заданий реализована возможность качать фото из ОК.
#### Причина: играя в игру "получить токен" проиграл
![обезьянка за компютером](images/6f432fe3dbc7c93c9efb84787621d963.gif)
##### ~~Получение токенов в задании самое трудное~~

## Программа позволяет сохранять фото пользователя вк или ок по id на яндекс диске

### при входе в программу можно увидеть 4 команды:
* svk - сохранить фото пользователя с вк
* sok - сохранить фото пользователя с ок
* stoken - установить токен для яндекс диска
* exit - выйти

### Первым делом надо инициализировать хранилище:
* ввести команду stoken
* ввести токен от яндекс диска  

После ввода токена будет отправлен тестовый запрос и если он будет успешным вы увидите:  

```
Токен сохранен успешно
```

иначе ~~значит, что вы все сломали~~ фотографии сохранить  не получится

### Сохранение фотографий из ВК на примере команды svk:

* ввести id пользователя (в качестве теста 552934290)
* ввести максимальное кол-во фотографий, которое хотите сохранить

При успешном запросе начнется сохраненение фотографий в директорию vk_'id-пользователя' (для теста vk_552934290)  

Сохранение файлов происходит поочередно. Во время процесса сохранения файла в консоле можно увидеть (в качестве примера)  :  
```
Сохранение фото с именем 4_1594036496.png в директории vk_552934290
```

в результате успешного сохранения выведется:  
```
Фото сохранено успешно
```

После процедуры сохранения всех файлов в консоль произойдет вывод json файла с данными сохраняемых фотографий:
```
Успешно загруженные файлы: 
```

```
[
  {
    "file_name": "4_1594036496.png",
    "height": 1096,
    "width": 788,
    "url": "https://sun9-48.userapi.com/impg/hZBImqkCXbzy3VGIhn30Jj4P3RWurerkaZZSnw/oDCgWwpSe34.jpg?size=788x1096&quality=96&sign=c4dd55f91ae178aa6f6ad6c14ce6cd4c&c_uniq_tag=u7Tqeio-kEtrWqLTPywWPFhhGHGuWuqONBJ7tdKCUAs&type=album"
  },
  {
    "file_name": "3_1593979270.png",
    "height": 800,
    "width": 800,
    "url": "https://sun9-77.userapi.com/impg/oFiwQBOqvXfWUtxWvqxcMyvSeMIZhiK3ki9Ssw/1J6DiX6JDr8.jpg?size=800x800&quality=96&sign=bba662d0ca0bcff8ed8e4ab5e5b5266e&c_uniq_tag=9O-sXQPZSOpED9Mdsoml0by9HkDzYVIdQRX5htRO9_w&type=album"
  }
]
```

Сохраненние командой sok выглядит аналогично

