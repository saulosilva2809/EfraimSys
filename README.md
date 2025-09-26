# EfraimSys - Sistema de Gestão Empresarial

Sistema de gestão empresarial desenvolvido em Django, focado em controle financeiro, gestão de funcionários e dashboard analítico.

## 🚀 Funcionalidades

### 💰 Módulo Financeiro
- **Dashboard Financeiro**: Visão geral com KPIs de receitas, despesas e saldo
- **Gestão de Contas**: Controle de contas bancárias e saldos
- **Transações**: Registro e acompanhamento de receitas e despesas
- **Relatórios**: Análise de gastos por categoria e transações recentes

### 👥 Módulo de Funcionários
- **Cadastro de Funcionários**: Gestão completa de dados pessoais
- **Funções e Cargos**: Controle de hierarquia organizacional
- **Relatórios de RH**: Análises e estatísticas da equipe

### 🔐 Sistema de Autenticação
- **Login/Logout**: Sistema seguro de autenticação
- **Perfil de Usuário**: Gestão de dados pessoais
- **Controle de Acesso**: Permissões baseadas em usuário

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.6
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de Dados**: SQLite (desenvolvimento)
- **Task Queue**: Celery 5.5.3 + Redis
- **Monitoramento**: Flower 2.0.1
- **Processamento de Imagens**: Pillow 11.3.0

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git

## 🔧 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/EfraimSys.git
cd EfraimSys
```

### 2. Crie um ambiente virtual
```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual
**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente
```bash
cp .env.example .env
```
Edite o arquivo `.env` com suas configurações:
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 6. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 8. Execute o servidor
```bash
python manage.py runserver
```

O sistema estará disponível em: `http://localhost:8000`

## 📁 Estrutura do Projeto

```
EfraimSys/
├── apps/
│   ├── authentication/     # Sistema de autenticação
│   ├── base/              # Módulo base (dashboard, home)
│   ├── employees/         # Gestão de funcionários
│   └── finances/          # Módulo financeiro
├── core/                  # Configurações do Django
├── templates/             # Templates HTML
├── static/               # Arquivos estáticos
├── .env.example          # Exemplo de configurações
├── requirements.txt      # Dependências do projeto
└── manage.py            # Script de gerenciamento Django
```

## 🎨 Interface

O sistema possui uma interface moderna e responsiva com:
- **Design System**: Padrão visual consistente (EfraimSys)
- **Dashboard Interativo**: KPIs animados e gráficos
- **Responsividade**: Adaptável a diferentes dispositivos
- **UX Otimizada**: Navegação intuitiva e performance otimizada

## 🔄 Funcionalidades Avançadas

### Celery (Tarefas Assíncronas)
Para executar tarefas em background:
```bash
# Terminal 1 - Redis Server
redis-server

# Terminal 2 - Celery Worker
celery -A core worker --loglevel=info

# Terminal 3 - Flower (Monitoramento)
celery -A core flower
```

### Comandos Úteis
```bash
# Coletar arquivos estáticos
python manage.py collectstatic

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Shell interativo
python manage.py shell
```

## 🚀 Deploy

### Preparação para Produção
1. Configure `DEBUG=False` no `.env`
2. Defina `ALLOWED_HOSTS` apropriadamente
3. Configure banco de dados de produção
4. Execute `python manage.py collectstatic`

### Variáveis de Ambiente de Produção
```env
SECRET_KEY=sua-chave-secreta-super-forte
DEBUG=False
ALLOWED_HOSTS=seudominio.com,www.seudominio.com
DATABASE_URL=postgresql://user:password@localhost:5432/efraimsys
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

- **Desenvolvedor**: Saulo
- **Email**: seu-email@exemplo.com
- **LinkedIn**: [Seu LinkedIn](https://linkedin.com/in/seu-perfil)

## 🎯 Roadmap

- [ ] Módulo de Vendas
- [ ] Integração com APIs de pagamento
- [ ] Relatórios avançados com gráficos
- [ ] App mobile
- [ ] Integração com contabilidade

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!**