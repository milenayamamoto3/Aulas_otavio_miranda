# Uma API REST simples para consumo de dados

Atenção: você precisa ter o NodeJS instalado no seu computador.  

Para subir o projeto no ar com SQLite, copie o arquivo `.env_example` para `.env`.  
'''
copy .env_example .env 
'''

Você também precisará adicionar uma secret key no arquivo `.env`:

```
TOKEN_SECRET='sua_secret_key_aqui'
```

Execute os comandos abaixo:

```
npm i
npx sequelize db:migrate
npx sequelize db:seed:all
npm run dev
```

Caso queira configurar o seu sistema para ativar o seu ambiente virtual:
Habilitar a execução de scripts temporariamente:

    Abra o PowerShell como administrador.

    Execute o comando a seguir para permitir a execução de scripts apenas 
    para a sessão atual:

    powershell

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

    Execute o comando npm run dev novamente.

Habilitar a execução de scripts permanentemente:

    Abra o PowerShell como administrador.

    Execute o comando a seguir para permitir a execução de scripts para todos
     os usuários:

    powershell

    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope LocalMachine

    Confirme a alteração digitando "Y" e pressionando Enter.

    Execute o comando npm run dev novamente.

Lembre-se de que habilitar a execução de scripts pode representar um risco 
de segurança. Certifique-se de entender os riscos envolvidos e tomar as 
medidas apropriadas para proteger seu sistema. Após concluir suas tarefas, 
você pode reverter a política de execução de scripts para seu estado original
usando o comando Set-ExecutionPolicy com a política adequada (por exemplo,
Restricted ou RemoteSigned).
______________________________________________________________________________________________________________________
npm run dev:
node "C:\Program Files\nodejs\node_modules\npm\bin\npm-cli.js" run dev
______________________________________________________________________________________________________________________

Neste ponto sua API deverá está rodando no endereço http://127.0.0.1:3001/.

Caso queira migrar para MySQL/MariaDB, edite as configurações de base de dados no arquivo `.env`, configure também o `src/config/database.js`.

Para SQLite as configurações são:

```javascript
require('dotenv').config();

module.exports = {
  dialect: 'sqlite',
  storage: './db.sqlite',
  define: {
    timestamps: true,
    underscored: true,
    underscoredAll: true,
    createdAt: 'created_at',
    updatedAt: 'updated_at',
  },
};
```

Para MySQL/MariaDB as configurações são:

```javascript
require('dotenv').config();

module.exports = {
  host: process.env.DATABASE_HOST,
  port: process.env.DATABASE_PORT,
  username: process.env.DATABASE_USERNAME,
  password: process.env.DATABASE_PASSWORD,
  database: process.env.DATABASE,
  dialectOptions: {
    timezone: 'America/Sao_Paulo',
  },
  timezone: 'America/Sao_Paulo',

  define: {
    timestamps: true,
    underscored: true,
    underscoredAll: true,
    createdAt: 'created_at',
    updatedAt: 'updated_at',
  },
};
```

Perceba que as configurações começando com `process.env.` vem do arquivo `.env`.

Os dados de usuário e senha dos arquivos de seed são:

- email = admin@email.com
- senha = 123456

Você pode obter o token JWT na rota `/tokens`, passando os dados JSON:

```json
{
	"email": "admin@email.com",
	"password": "123456"
}
```

Headers:

```
Content-Type	application/json; charset=utf-8
```
# endpoints

Os seguintes endpoints estão configurados:

## Home - não há nada aqui

- `/` - GET

## Usuários (users)
## https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods -> HTTP request methods
- `/users` - DELETE - Apaga o usuário logado
- `/users` - PUT - Atualiza o usuário logado
- `/users` - POST - Cria um usuário
- `/users/:id` - GET - Mostra o usuário do ID enviado (rota desativada)
- `/users` - GET - Mostra todos os usuários (rota desativada)

**Dados para usuários (JSON)**

```
{
	"nome": "nome válido",
	"password": "senha válida",
	"email": "email_valido@email.com"
}
```

## Tokens

- `/tokens` - POST - Obtém o token JWT

**Dados para tokens (JSON)**

```
{
	"email": "admin@email.com",
	"password": "123456"
}
```

## Aluno

- `/alunos/:id` - DELETE - Apaga o aluno do ID enviado
- `/alunos/:id` - PUT - Atualiza o aluno do ID enviado
- `/alunos` - POST - Cria um aluno
- `/alunos/:id` - GET - Mostra o aluno do ID enviado
- `/alunos` - GET - Mostra todos os alunos


**Dados para tokens (JSON)**

```
{
	"nome": "Nome",
	"sobrenome": "Sobrenome",
	"email": "email@email.com",
	"idade": "50",
	"peso": "80.04",
	"altura": "1.90"
}
```

## Fotos

Atenção aqui, esse é o único endpoint `multipart/form-data` para envio de arquivos.

- `/fotos` - POST - Recebe um arquivo de foto JPG ou PNG e um `aluno_id`.

**Dados para fotos (multipart/form-data)**

```
{
	"foto": (ARQUIVO.PNG|JPG),
	"aluno_id": ":id"
}
```