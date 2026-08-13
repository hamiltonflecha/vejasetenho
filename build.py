#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera todas as páginas HTML do site 'Veja se Tenho' a partir de um template comum."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

SITE_NAME = "Veja se Tenho"
DOMAIN = "https://vejasetenho.com.br"
EMAIL = "contato@vejasetenho.com.br"

SIDEBAR_GROUPS = [
    {
        "label": "Início",
        "links": [
            {"href": "index.html", "text": "Home"},
        ],
    },
    {
        "label": "Veja se tenho",
        "links": [
            {"href": "refinanciamento.html", "text": "Refin (grátis)"},
            {"href": "novo-emprestimo.html", "text": "Novo (grátis)"},
            {"href": "portabilidade.html", "text": "Portabilidade (grátis)"},
            {"href": "margem-consignavel.html", "text": "Margem consignável",
             "sub": [
                 ("margem-consignavel.html#previsao", "Previsão"),
                 ("margem-consignavel.html#positiva", "Margem positiva — valor a receber"),
                 ("margem-consignavel.html#negativa", "Margem negativa"),
             ]},
            {"href": "descontos-indevidos.html", "text": "Descontos indevidos",
             "sub": [
                 ("descontos-indevidos.html#beneficio", "No benefício"),
                 ("descontos-indevidos.html#conta", "Na conta bancária"),
             ]},
        ],
    },
    {
        "label": "Estudos de viabilidade",
        "links": [
            {"href": "viabilidade-beneficios.html", "text": "Aposentadoria, LOAS e BPC"},
            {"href": "acoes-inss-bancos.html", "text": "Ações contra INSS e bancos"},
        ],
    },
    {
        "label": "Documentos necessários",
        "links": [
            {"href": "documentos.html", "text": "Índice de documentos",
             "sub": [
                 ("documentos.html#cnis", "CNIS"),
                 ("documentos.html#extrato-consignado", "Extrato de empréstimos consignados"),
                 ("documentos.html#extrato-bancario", "Extrato bancário"),
                 ("documentos.html#historico-creditos", "Histórico de créditos (SCR)"),
             ]},
        ],
    },
    {
        "label": "Ajuda",
        "links": [
            {"href": "ajuda.html", "text": "Perguntas frequentes"},
        ],
    },
]

TOPNAV = [
    ("index.html", "Início"),
    ("index.html#veja-se-tenho", "Veja se tenho"),
    ("documentos.html", "Documentos"),
    ("viabilidade-beneficios.html", "Viabilidade"),
    ("ajuda.html", "Ajuda"),
]

def render_sidebar(active_href):
    active_base = active_href.split("#")[0]
    html = ['<div class="sidebar">']
    html.append('<div class="sidebar-version">v1.0</div>')
    for group in SIDEBAR_GROUPS:
        html.append('<div class="sidebar-group">')
        html.append(f'<div class="sidebar-label">{group["label"]}</div>')
        for link in group["links"]:
            cls = ' class="ativo"' if link["href"].split("#")[0] == active_base else ""
            html.append(f'<a href="{link["href"]}"{cls}>{link["text"]}</a>')
            if "sub" in link:
                html.append('<ul class="sublist">')
                for href, text in link["sub"]:
                    html.append(f'<li><a href="{href}">{text}</a></li>')
                html.append('</ul>')
        html.append('</div>')
    html.append('</div>')
    return "\n".join(html)

def render_topnav(active_href):
    items = []
    for href, text in TOPNAV:
        cls = ' class="ativo"' if href == active_href else ""
        items.append(f'<a href="{href}"{cls}>{text}</a>')
    return "\n      ".join(items)

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{description}">

<link rel="stylesheet" href="style.css">
</head>
<body>

<!-- Barra superior -->
<div class="topbar">
  <div class="topbar-inner">
    <div style="display:flex;align-items:center;gap:12px;">
      <button class="menu-toggle" onclick="document.querySelector('.sidebar').classList.toggle('open')" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
      <div class="brand"><a href="index.html" style="text-decoration:none;color:inherit;display:flex;align-items:center;gap:7px;"><img src="favicon.svg" alt="" style="width:24px;height:24px;border-radius:6px;">Veja se<span>Tenho</span></a></div>
    </div>
    <nav>
      {topnav}
    </nav>
    <div class="topbar-right">
      <div class="topbar-search">
        <span class="search-icon">🔍</span>
        <input type="text" id="siteSearch" placeholder="Buscar no site..." aria-label="Buscar no site">
      </div>
      <div class="topbar-icons">
        <a href="#" onclick="event.preventDefault();compartilharSite();" class="icon-link icon-share" aria-label="Compartilhar" title="Compartilhar"><svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor" aria-hidden="true"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L7.04 9.81C6.5 9.31 5.79 9 5 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/></svg></a>
        <a href="mailto:{email}" class="icon-link icon-email" aria-label="Enviar e-mail" title="Enviar e-mail"><svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor" aria-hidden="true"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></a>
      </div>
    </div>
  </div>
</div>
<div id="searchResults" class="search-results"></div>

<!-- Sidebar esquerda -->
{sidebar}

<div class="main">

{content}

  <footer>
    <div class="wrap">
      {SITE_NAME} — análise de descontos consignados do INSS e de contas bancárias, e estudo de viabilidade de benefícios previdenciários. Não somos um escritório de advocacia; nossas análises são de caráter informativo e não substituem a consulta a um(a) advogado(a).
    </div>
  </footer>

</div><!-- /main -->

<script>
const searchIndex = {search_index};

function normalizar(s){{
  return s.toLowerCase().normalize("NFD").replace(/[\\u0300-\\u036f]/g,"");
}}
function buscar(q){{
  const nq = normalizar(q);
  if(nq.length < 2) return [];
  return searchIndex.filter(i =>
    normalizar(i.t).includes(nq) || normalizar(i.d).includes(nq)
  ).slice(0,10);
}}
function renderResultados(items){{
  const box = document.getElementById("searchResults");
  if(items.length === 0){{
    box.innerHTML = '<div class="rempty">Nada encontrado.</div>';
    box.classList.add("show");
    return;
  }}
  box.innerHTML = items.map(i =>
    '<a href="' + i.u + '"><div class="rtitle">' + i.t + '</div><div class="rsnippet">' + i.d + '</div></a>'
  ).join("");
  box.classList.add("show");
}}
document.addEventListener("DOMContentLoaded", function(){{
  const inp = document.getElementById("siteSearch");
  const box = document.getElementById("searchResults");
  if(inp){{
    inp.addEventListener("input", function(){{
      const r = buscar(this.value);
      if(this.value.trim().length < 2){{ box.classList.remove("show"); return; }}
      renderResultados(r);
    }});
    inp.addEventListener("blur", function(){{ setTimeout(()=>box.classList.remove("show"), 200); }});
    inp.addEventListener("focus", function(){{ if(this.value.trim().length >= 2){{ renderResultados(buscar(this.value)); }} }});
  }}
}});

function compartilharSite(){{
  const url = "{domain}";
  const txt = "Veja se você tem direito a revisão de descontos do INSS ou de bancos: " + url;
  if(navigator.share){{
    navigator.share({{title:"{SITE_NAME}", text:"Análise de descontos consignados do INSS", url:url}}).catch(()=>{{}});
  }} else {{
    window.open("https://wa.me/?text=" + encodeURIComponent(txt), "_blank");
  }}
}}
</script>

</body>
</html>
"""

SEARCH_INDEX = [
    {"t": "Home", "d": "Página inicial do Veja se Tenho", "u": "index.html"},
    {"t": "Refin (grátis)", "d": "Verifique se você já tem um refinanciamento de consignado ativo", "u": "refinanciamento.html"},
    {"t": "Novo empréstimo (grátis)", "d": "Verifique se um novo consignado foi contratado em seu nome", "u": "novo-emprestimo.html"},
    {"t": "Portabilidade (grátis)", "d": "Entenda e verifique portabilidades de consignado", "u": "portabilidade.html"},
    {"t": "Margem consignável", "d": "Previsão de margem, margem positiva e margem negativa", "u": "margem-consignavel.html"},
    {"t": "Descontos indevidos", "d": "Descontos indevidos no benefício e na conta bancária", "u": "descontos-indevidos.html"},
    {"t": "Aposentadoria, LOAS e BPC", "d": "Estudo de viabilidade de aposentadoria, LOAS e BPC", "u": "viabilidade-beneficios.html"},
    {"t": "Ações contra INSS e bancos", "d": "Análise crítica sobre possíveis ações judiciais e administrativas", "u": "acoes-inss-bancos.html"},
    {"t": "Documentos necessários", "d": "CNIS, extrato de consignado, extrato bancário e histórico de créditos", "u": "documentos.html"},
    {"t": "CNIS", "d": "O que é e como tirar o CNIS pelo Meu INSS", "u": "documentos.html#cnis"},
    {"t": "Extrato de empréstimos consignados", "d": "Como emitir o extrato de consignado pelo Meu INSS", "u": "documentos.html#extrato-consignado"},
    {"t": "Extrato bancário", "d": "Como obter o extrato bancário para análise de descontos", "u": "documentos.html#extrato-bancario"},
    {"t": "Histórico de créditos", "d": "Registrato e SCR do Banco Central", "u": "documentos.html#historico-creditos"},
    {"t": "Ajuda", "d": "Perguntas frequentes e contato", "u": "ajuda.html"},
]

import json

def build_page(filename, title, description, og_title, active_href, content):
    html = PAGE_TEMPLATE.format(
        title=title,
        description=description,
        canonical=f"{DOMAIN}/{filename}" if filename != "index.html" else f"{DOMAIN}/",
        og_title=og_title,
        topnav=render_topnav(active_href),
        sidebar=render_sidebar(active_href),
        content=content,
        SITE_NAME=SITE_NAME,
        search_index=json.dumps(SEARCH_INDEX, ensure_ascii=False),
        domain=DOMAIN,
        email=EMAIL,
    )
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("gerado:", filename)
