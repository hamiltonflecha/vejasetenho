# Veja se Tenho

Site institucional sobre análise de descontos consignados do INSS, descontos indevidos em benefícios e contas bancárias, e estudo de viabilidade de aposentadoria, LOAS e BPC.

Site estático (HTML + CSS puro, sem build), no mesmo formato usado pelo smsmass.com.br: barra superior fixa, barra lateral de navegação, hospedado gratuitamente no **GitHub Pages**, com o domínio próprio **vejasetenho.com.br**.

## Estrutura

```
index.html                    Home
refinanciamento.html          Refin (grátis)
novo-emprestimo.html          Novo (grátis)
portabilidade.html            Portabilidade (grátis)
margem-consignavel.html       Previsão / margem positiva / margem negativa
descontos-indevidos.html      No benefício / na conta bancária
viabilidade-beneficios.html   Aposentadoria, LOAS, BPC
acoes-inss-bancos.html        Ações contra INSS e bancos
documentos.html               CNIS, extrato consignado, extrato bancário, histórico de créditos
ajuda.html                    FAQ
style.css                     Estilos (fundo claro, sem modo escuro)
favicon.svg                   Ícone do site
CNAME                         Domínio customizado do GitHub Pages
.nojekyll                     Evita processamento Jekyll

build.py / content_*.py / generate_site.py
                               Gerador das páginas (opcional — só necessário
                               se você quiser editar o conteúdo e regerar o
                               HTML com `python3 generate_site.py`)
```

Para editar um texto, o mais simples é editar o `.html` correspondente
diretamente. Para mudanças estruturais (menu, rodapé, etc.), edite
`build.py` e os arquivos `content_*.py`, depois rode:

```bash
python3 generate_site.py
```

## 1. Publicar no GitHub Pages

1. Crie um repositório novo no GitHub (ex.: `vejasetenho-site`), **público**
   (GitHub Pages grátis exige repositório público, a menos que você tenha
   um plano pago).
2. Envie os arquivos deste diretório para o repositório:

   ```bash
   cd vejasetenho
   git init
   git add .
   git commit -m "Site inicial"
   git branch -M main
   git remote add origin https://github.com/SEU-USUARIO/vejasetenho-site.git
   git push -u origin main
   ```

3. No GitHub, vá em **Settings → Pages**.
4. Em **Build and deployment → Source**, selecione **Deploy from a branch**.
5. Em **Branch**, selecione `main` e a pasta `/ (root)`. Clique em **Save**.
6. Em **Custom domain**, digite `vejasetenho.com.br` e clique em **Save**
   (isso confirma o arquivo `CNAME` que já está no repositório).
7. Aguarde a mensagem de verificação de DNS (próximo passo) e depois marque
   **Enforce HTTPS**.

## 2. Configurar o domínio (Cloudflare)

Como o domínio `vejasetenho.com.br` já está registrado, os passos são:

1. Adicione o domínio à sua conta Cloudflare (se ainda não estiver lá) e
   aponte os *nameservers* do registrador para os nameservers que a
   Cloudflare indicar. Isso pode levar algumas horas para propagar.
2. No painel da Cloudflare, vá em **DNS → Records** e crie:

   | Tipo | Nome | Conteúdo               | Proxy status |
   |------|------|-------------------------|--------------|
   | A    | @    | 185.199.108.153         | DNS only ⚠️ (veja nota abaixo) |
   | A    | @    | 185.199.109.153         | DNS only |
   | A    | @    | 185.199.110.153         | DNS only |
   | A    | @    | 185.199.111.153         | DNS only |
   | CNAME| www  | SEU-USUARIO.github.io   | DNS only |

   > **Nota sobre o proxy da Cloudflare (nuvem laranja):** o GitHub Pages
   > emite o certificado HTTPS automaticamente comparando o DNS público do
   > domínio com o valor esperado. Enquanto o certificado ainda não foi
   > emitido, deixe os registros como **"DNS only"** (nuvem cinza). Depois
   > que o certificado for emitido pelo GitHub (aparece "DNS check
   > successful" na tela de Pages), você pode ativar o proxy da Cloudflare
   > ("Proxied", nuvem laranja) se quiser o CDN e a proteção da Cloudflare
   > — nesse caso, configure o modo SSL/TLS da Cloudflare como **"Full"**
   > (não "Flexible", para evitar loop de redirecionamento).

3. Volte em **Settings → Pages** no GitHub e confirme que o domínio
   `vejasetenho.com.br` aparece com "DNS check successful" e HTTPS
   disponível.
4. Teste: acesse `https://vejasetenho.com.br` depois da propagação do DNS
   (pode levar de alguns minutos até algumas horas).

## 3. Antes de publicar, revise

- O e-mail de contato usado no site é um placeholder
  (`contato@vejasetenho.com.br`) — troque em `build.py` (constante `EMAIL`)
  pelo e-mail real e rode `python3 generate_site.py` de novo.
- Não há número de WhatsApp cadastrado (ao contrário do site de
  referência) — se quiser adicionar, edite o botão de ícones no
  `PAGE_TEMPLATE` dentro de `build.py`.
- Os percentuais de margem consignável e os valores de renda do BPC citados
  no site podem mudar por lei — confirme os valores vigentes antes de
  publicar, e revise periodicamente.
