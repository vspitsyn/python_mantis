<?php
$g_hostname               = 'localhost';
$g_db_type                = 'mysqli';
$g_database_name          = 'bugtracker';
$g_db_username            = 'root';
$g_db_password            = '';
$g_enable_email_notification = ON;
$g_phpMailer_method = PHPMAILER_METHOD_SMTP; # ����� 2 ����� �������� ����� PHPMAILER_METHOD_SMTP
$g_smtp_host = 'email.bank.int'; #, ����������� �����
#$g_smtp_username = 'Spitsyn-VM@sviaz-bank.ru'; #����������� ��������� ������ ��� ����� � �������� ���������
#$g_smtp_password = ''; #������ � ��������� �����
#$g_smtp_connection_mode = ''; #���� �� ��������� ����� ���������� �� ����� ������� SMTP �����. ����� ������� �������� ssl
#$g_smtp_port = '';  #���� �� ��������� �������� �����, �� �� ��������� 25 ����. ���� ���������� ����� ssl �� ����� ������� 465 ����
#$g_administrator_email = 'Spitsyn-VM@sviaz-bank.ru';  #���� ������� ����� ��������� � ���������� �������������� �������� mantis
#$g_webmaster_email = 'Spitsyn-VM@sviaz-bank.ru';  #���� ������� ����� ��������� � ���������� ���������� �������� mantis
#$g_from_email = 'Spitsyn-VM@sviaz-bank.ru';  #�� ��� ����� � ���� "From: "
#$g_return_path_email = 'Spitsyn-VM@sviaz-bank.ru';  #���� ������� � ������� ����� ������ �������� �����
#$g_log_level = LOG_EMAIL | LOG_EMAIL_RECIPIENT | LOG_DATABASE; #����� �������� �����������, ����� ������ ��� ���������� � ��������
#$g_log_destination = 'file:/usr/local/www/mantis/logs/mantisbt.log'; # ���� ���� ���������� ���� mantis
$g_from_name = 'Mantis Bug Tracker'; # ������������� ��� � ���� "From: "


$g_default_timezone       = 'Europe/Moscow';
$g_crypto_master_salt     = 'CzvVRQDpfDJRr1IVoF445umayBsv20xC8lrVJVyWrTE=';
