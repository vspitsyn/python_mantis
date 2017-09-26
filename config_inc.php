<?php
$g_hostname               = 'localhost';
$g_db_type                = 'mysqli';
$g_database_name          = 'bugtracker';
$g_db_username            = 'root';
$g_db_password            = '';
$g_enable_email_notification = ON;
$g_phpMailer_method = PHPMAILER_METHOD_SMTP; # цифра 2 будет вызывать метод PHPMAILER_METHOD_SMTP
$g_smtp_host = 'email.bank.int'; #, принимающий почту
#$g_smtp_username = 'Spitsyn-VM@sviaz-bank.ru'; #обязательно указываем полное имя ящика с доменным суффиксом
#$g_smtp_password = ''; #пароль к почтовому ящику
#$g_smtp_connection_mode = ''; #если не указывать режим соединения то будет обычный SMTP метод. Можно указать значение ssl
#$g_smtp_port = '';  #если не указывать значение порта, то по умолчанию 25 порт. Если используем режим ssl то нужно указать 465 порт
#$g_administrator_email = 'Spitsyn-VM@sviaz-bank.ru';  #ящик который будет светиться с контактами администратора инстанса mantis
#$g_webmaster_email = 'Spitsyn-VM@sviaz-bank.ru';  #ящик который будет светиться с контактами вебмастера инстанса mantis
#$g_from_email = 'Spitsyn-VM@sviaz-bank.ru';  #то что будет в поле "From: "
#$g_return_path_email = 'Spitsyn-VM@sviaz-bank.ru';  #ящик который в который будут падать возвраты писем
#$g_log_level = LOG_EMAIL | LOG_EMAIL_RECIPIENT | LOG_DATABASE; #стоит включить логирование, чтобы видеть что происходит с мантисом
#$g_log_destination = 'file:/usr/local/www/mantis/logs/mantisbt.log'; # путь куда складываем логи mantis
$g_from_name = 'Mantis Bug Tracker'; # символическое имя в поле "From: "


$g_default_timezone       = 'Europe/Moscow';
$g_crypto_master_salt     = 'CzvVRQDpfDJRr1IVoF445umayBsv20xC8lrVJVyWrTE=';
