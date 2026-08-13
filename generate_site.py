#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build import build_page
from content_index import CONTENT as IDX
from content_verificacoes import REFIN, NOVO, PORTABILIDADE
from content_margem import MARGEM
from content_descontos import DESCONTOS
from content_viabilidade import VIABILIDADE, ACOES
from content_documentos import DOCUMENTOS
from content_ajuda import AJUDA

build_page(
    "index.html",
    "Veja se Tenho — descontos indevidos, consignado e benefícios do INSS",
    "Veja se você tem descontos indevidos no benefício do INSS ou na conta bancária, refinanciamento ou novo consignado não reconhecido, e a viabilidade de aposentadoria, LOAS e BPC.",
    "Veja se Tenho",
    "index.html",
    IDX,
)

build_page(
    "refinanciamento.html",
    "Refin — veja se você tem um refinanciamento de consignado ativo | Veja se Tenho",
    "Verificação gratuita: veja se você tem um refinanciamento de empréstimo consignado ativo no seu benefício do INSS.",
    "Refin — Veja se Tenho",
    "refinanciamento.html",
    REFIN,
)

build_page(
    "novo-emprestimo.html",
    "Novo — veja se um novo empréstimo consignado foi contratado em seu nome | Veja se Tenho",
    "Verificação gratuita: veja se um novo empréstimo consignado foi contratado em seu nome, com ou sem autorização.",
    "Novo empréstimo — Veja se Tenho",
    "novo-emprestimo.html",
    NOVO,
)

build_page(
    "portabilidade.html",
    "Portabilidade — veja se houve portabilidade do seu consignado | Veja se Tenho",
    "Verificação gratuita: veja se houve portabilidade do seu empréstimo consignado e se as condições realmente melhoraram.",
    "Portabilidade — Veja se Tenho",
    "portabilidade.html",
    PORTABILIDADE,
)

build_page(
    "margem-consignavel.html",
    "Margem consignável: previsão, positiva e negativa | Veja se Tenho",
    "Entenda a previsão de margem, a margem positiva (valor a receber) e a margem negativa do seu consignado do INSS.",
    "Margem consignável — Veja se Tenho",
    "margem-consignavel.html",
    MARGEM,
)

build_page(
    "descontos-indevidos.html",
    "Descontos indevidos no benefício e na conta bancária | Veja se Tenho",
    "Como identificar descontos indevidos no seu benefício do INSS e na sua conta bancária: consignado não reconhecido, cartão benefício, tarifas e seguros.",
    "Descontos indevidos — Veja se Tenho",
    "descontos-indevidos.html",
    DESCONTOS,
)

build_page(
    "viabilidade-beneficios.html",
    "Viabilidade de aposentadoria, LOAS e BPC | Veja se Tenho",
    "Veja se você já tem direito a se aposentar, ou a benefícios assistenciais como LOAS e BPC, junto ao INSS.",
    "Aposentadoria, LOAS e BPC — Veja se Tenho",
    "viabilidade-beneficios.html",
    VIABILIDADE,
)

build_page(
    "acoes-inss-bancos.html",
    "Ações contra o INSS e contra bancos | Veja se Tenho",
    "Análise crítica sobre quando situações de desconto indevido ou benefício negado costumam justificar buscar orientação jurídica.",
    "Ações contra INSS e bancos — Veja se Tenho",
    "acoes-inss-bancos.html",
    ACOES,
)

build_page(
    "documentos.html",
    "Documentos necessários: CNIS, extratos e histórico de créditos | Veja se Tenho",
    "Guia completo, gratuito, de como tirar o CNIS, o extrato de empréstimos consignados, o extrato bancário e o histórico de créditos (Registrato/SCR).",
    "Documentos necessários — Veja se Tenho",
    "documentos.html",
    DOCUMENTOS,
)

build_page(
    "ajuda.html",
    "Ajuda e perguntas frequentes | Veja se Tenho",
    "Perguntas frequentes sobre o Veja se Tenho: análise de descontos consignados do INSS e de contas bancárias.",
    "Ajuda — Veja se Tenho",
    "ajuda.html",
    AJUDA,
)

print("\nSite gerado com sucesso.")
