# COMANDOS DO DJANGO

1. ``pip install django ``-> Instala o Django no projeto.
2. ``django-admin startproject nome_do_projeto .`` -> Criando um novo projeto em django.
3. ``python manage.py runserver`` -> Subindo o servidor.
4. ``python manage.py startapp nome_do_app`` -> Criando um novo app.
5. ``python manage.py migrate`` ->  Realiza as migrações(ativa) do projeto.
6. ``python manage.py createsuperuser`` -> Criar um novo super usuário.
7. ``python manage.py changepassword nomedousuario`` -> Altera a senha, caso você esqueça.
8. ``python manage.py makemigrations`` -> Cria/gera um novo pacote de migração (Útil para novo app e alteração do BD).



# ATIVIDADE
1. Criar um model para o médico com as informações: 
 - Nome
 - Sobrenome
 - E-mail
 - Data da Criação
 - Telefone
 - CRM (6 digitos), será string
 - Especialidade 
 - Mensagem
 - Ativo = True 

 2. Na Exibição do Portal administrativo, deverá ser apresentado:
 - Id, Nome, email, telefone, especialidade, crm, ativo

 # Professor 
-> Características: 
1. disciplina
2. nome
3. idade
4. cpf
5. endereco
6. telefone
7. disciplina
8. ativo 
9. data do cadastro

# Aluno
-> Características: 
1. matricula
2. nome
3. idade
4. cpf
5. endereco
6. telefone
8. ativo 
9. data do cadastro
    
# Turma
-> Características: 
1. turma
2. turno
3. professor
4. aluno
5. ativo
6. data do cadastro
7. observação


