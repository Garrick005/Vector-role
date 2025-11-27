Установка и базовая настройка Vector
------------------------------------

Данная роль предназначена для установки и базовой настройки Vector на deb дистрибутивы.


Requirements
------------

Предназначен для установка на deb-дистрибутивы. 

Role Variables
--------------

Default vars:
vector_version: 'latest'
vector_service_ensure: 'started'
vector_service_enable: true

Vars:
vector_version: "0.44.0"
vector_config_path: "/etc/vector/vector.yaml"
=======
---
lighthouse_root: /var/www/lighthouse
lighthouse_repo: https://github.com/VKCOM/lighthouse.git
lighthouse_nginx_conf_path: /etc/nginx/sites-available/lighthouse
lighthouse_server_name: lighthouse.local
>>>>>>> beefe3c (Lighthouse role)

Example Playbook
----------------

- name: Установка Vector
  hosts: your host
  roles:
    - vector 

License
-------

MIT


