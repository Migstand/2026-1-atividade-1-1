# Sistemas Operacionais - Atividade 1.1 Avaliativa de 2026.1, 23/03, Miguel Rodrigues Spínola da Hora

## Introdução
  Essa atividade se trata da primeira avaliação da matéria Sistemas Operacionais de 2026.1. O objetivo é conseguir executar uma simples aplicação Django via Docker seguindo o guia do professor da diciplina.

## Relato das atividades
    Para conseguir executar a atividade, seguindo 4 etapas.
    Na primeira, criei um fork, clonei o repositório da atividade, criei uma pasta app, criei um arquivo app/requirements.txt.
    Na Segundo, criei um arquivo app/Dockerfile.dev, depois construi a imagem de desenvolvimento e executei o container de desenvolvimento com volume mapeado.
    ![Build](/imagens/Build.png)
    ![Run](/imagens/Run.png)

    Na terceira, Dentro do container, criei um projeto Django, junto de uma aplicação Django com as configurações de banco de dados SQLite3, adicionando a aplicação no arquivo
    settings.py e configurando o ALLWED_HOSTS. Executei as migrações do banco de dados e criei um superusário admin e fiz uma view simples configurando a URLs da aplicação e do projeto.
    ![Comandos](/imagens/Primeiroscmd.png)
    ![Migrate](/imagens/Migrate.png) 
    ![Admin](/imagens/Admin.png)

    Por fim, consegui executar servidor de desenvolvimento e testar a aplicação com sucesso.
    ![Olá](/imagens/Primeira pagina.png) 
    ![Funcionando](/imagens/Segunda pagina.png)


## Considerações finais
    Com isso, o que aprendi nessa atividade foram comandos básicos de docker: build, run, junto de pequenas aplicações Django.
    Sobre as minhas dificuldades, as minhas primeiras impressões seriam de que teria dificuldade para aprender os comandos devido a fala rápida do professor, mas consegui tirar minhas dúvidas e aprender o conteúdo.