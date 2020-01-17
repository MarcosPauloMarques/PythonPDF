#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import sys
import xmltodict
import webbrowser
import pdfkit
import configparser
from collections import defaultdict 
config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

with open('danfe.xml') as fd:
                doc = xmltodict.parse(fd.read())               
print(doc['NFe']['infNFe']['emit']['enderEmit'])
list = doc['NFe']['infNFe']['emit']['enderEmit']
list = [i.split()[0] for i in list]
#list = [i.split('<')[0] for i in list]
print(list)

#print(doc['NFe']['infNFe']['ide']['cDV'])
#doc['NFe']['infNFe']['det']['@nItem']['prod'].split
#prod = doc['NFe']['infNFe']['det']['@nItem']['prod']
#print(prod)

#int_cDV = int(doc['NFe']['infNFe']['ide']['cDV'])
#int_cUF = int(doc['NFe']['infNFe']['ide']['cUF'])
#int_cDVcUF = int_cUF + int_cDV
#str_cDVncUF = str(int_cDVcUF)
#print(str_cDVncUF)

        # doc['NFe']['@xmlns'] # == u'an attribute'
        # doc['NFe']['infNFe']['ide']['cUF'] # == [u'elements', u'more elements']
        # doc['NFe']['infNFe']['ide']['cNF']

#def print_html(string):
#
#    file = open("nfe.html", 'a')
#    file.write(string)
#    file.close()
#    webbrowser.open("nfe.html")
#
#print_html("")

file = open("nfe.html", 'w')
file.write("""
   <style type="text/css">
    @media print {
        @page {
            margin-left: 15mm;
            margin-right: 15mm;
        }

        footer {
            page-break-after: always;
        }
    }

    * {
        margin: 0;
    }

    .ui-widget-content {
        border: none !important;
    }

    .nfe-square {
        margin: 0 auto 2cm;
        box-sizing: border-box;
        width: 2cm;
        height: 1cm;
        border: 1px solid #000;
    }

    .nfeArea.page {
        width: 18cm;
        position: relative;
        font-family: "Times New Roman", serif;
        color: #000;
        margin: 0 auto;
        overflow: hidden;
    }

    .nfeArea .font-12 {
        font-size: 12pt;
    }

    .nfeArea .font-8 {
        font-size: 8pt;
    }

    .nfeArea .bold {
        font-weight: bold;
    }

    .nfeArea .area-name {
        font-family: "Times New Roman", serif;
        color: #000;
        font-weight: bold;
        margin: 5px 0 0;
        font-size: 6pt;
        text-transform: uppercase;
    }

    .nfeArea .txt-upper {
        text-transform: uppercase;
    }

    .nfeArea .txt-center {
        text-align: center;
    }

    .nfeArea .txt-right {
        text-align: right;
    }

    .nfeArea .nf-label {
        text-transform: uppercase;
        margin-bottom: 3px;
        display: block;
    }

    .nfeArea .nf-label.label-small {
        letter-spacing: -0.5px;
        font-size: 4pt;
    }

    .nfeArea .info {
        font-weight: bold;
        font-size: 8pt;
        display: block;
        line-height: 1em;
    }

    .nfeArea table {
        font-family: "Times New Roman", serif;
        color: #000;
        font-size: 5pt;
        border-collapse: collapse;
        width: 100%;
        border-color: #000;
        border-radius: 5px;
    }

    .nfeArea .no-top {
        margin-top: -1px;
    }

    .nfeArea .mt-table {
        margin-top: 3px;
    }

    .nfeArea .valign-middle {
        vertical-align: middle;
    }

    .nfeArea td {
        vertical-align: top;
        box-sizing: border-box;
        overflow: hidden;
        border-color: #000;
        padding: 1px;
        height: 5mm;
    }

    .nfeArea .tserie {
        width: 32.2mm;
        vertical-align: middle;
        font-size: 8pt;
        font-weight: bold;
    }

    .nfeArea .tserie span {
        display: block;
    }

    .nfeArea .tserie h3 {
        display: inline-block;
    }

    .nfeArea .entradaSaida .legenda {
        text-align: left;
        margin-left: 2mm;
        display: block;
    }

    .nfeArea .entradaSaida .legenda span {
        display: block;
    }

    .nfeArea .entradaSaida .identificacao {
        float: right;
        margin-right: 2mm;
        border: 1px solid black;
        width: 5mm;
        height: 5mm;
        text-align: center;
        padding-top: 0;
        line-height: 5mm;
    }

    .nfeArea .hr-dashed {
        border: none;
        border-top: 1px dashed #444;
        margin: 5px 0;
    }

    .nfeArea .client_logo {
        height: 27.5mm;
        width: 28mm;
        margin: 0.5mm;
    }

    .nfeArea .title {
        font-size: 10pt;
        margin-bottom: 2mm;
    }

    .nfeArea .txtc {
        text-align: center;
    }

    .nfeArea .pd-0 {
        padding: 0;
    }

    .nfeArea .mb2 {
        margin-bottom: 2mm;
    }

    .nfeArea table table {
        margin: -1pt;
        width: 100.5%;
    }

    .nfeArea .wrapper-table {
        margin-bottom: 2pt;
    }

    .nfeArea .wrapper-table table {
        margin-bottom: 0;
    }

    .nfeArea .wrapper-table table+table {
        margin-top: -1px;
    }

    .nfeArea .boxImposto {
        table-layout: fixed;
    }

    .nfeArea .boxImposto td {
        width: 11.11%;
    }

    .nfeArea .boxImposto .nf-label {
        font-size: 5pt;
    }

    .nfeArea .boxImposto .info {
        text-align: right;
    }

    .nfeArea .wrapper-border {
        border: 1px solid #000;
        border-width: 0 1px 1px;
        height: 75.7mm;
    }

    .nfeArea .wrapper-border table {
        margin: 0 -1px;
        width: 100.4%;
    }

    .nfeArea .content-spacer {
        display: block;
        height: 10px;
    }

    .nfeArea .titles th {
        padding: 3px 0;
    }

    .nfeArea .listProdutoServico td {
        padding: 0;
    }

    .nfeArea .codigo {
        display: block;
        text-align: center;
        margin-top: 5px;
    }

    .nfeArea .boxProdutoServico tr td:first-child {
        border-left: none;
    }

    .nfeArea .boxProdutoServico td {
        font-size: 6pt;
        height: auto;
    }

    .nfeArea .boxFatura span {
        display: block;
    }

    .nfeArea .boxFatura td {
        border: 1px solid #000;
    }

    .nfeArea .freteConta .border {
        width: 5mm;
        height: 5mm;
        float: right;
        text-align: center;
        line-height: 5mm;
        border: 1px solid black;
    }

    .nfeArea .freteConta .info {
        line-height: 5mm;
    }

    .page .boxFields td p {
        font-family: "Times New Roman", serif;
        font-size: 5pt;
        line-height: 1.2em;
        color: #000;
    }

    .nfeArea .imgCanceled {
        position: absolute;
        top: 75mm;
        left: 30mm;
        z-index: 3;
        opacity: 0.8;
        display: none;
    }

    .nfeArea.invoiceCanceled .imgCanceled {
        display: block;
    }

    .nfeArea .imgNull {
        position: absolute;
        top: 75mm;
        left: 20mm;
        z-index: 3;
        opacity: 0.8;
        display: none;
    }

    .nfeArea.invoiceNull .imgNull {
        display: block;
    }

    .nfeArea.invoiceCancelNull .imgCanceled {
        top: 100mm;
        left: 35mm;
        display: block;
    }

    .nfeArea.invoiceCancelNull .imgNull {
        top: 65mm;
        left: 15mm;
        display: block;
    }

    .nfeArea .page-break {
        page-break-before: always;
    }

    .nfeArea .block {
        display: block;
    }

    .label-mktup {
        font-family: Arial !important;
        font-size: 8px !important;
        padding-top: 8px !important;
    }
</style>
<!-- /Header -->
<!-- Recebimentos -->
<div class="page nfeArea">
    <div class="boxFields" style="padding-top: 20px;">
        <table cellpadding="0" cellspacing="0" border="1">
            <tbody>
                <tr>
                    <td colspan="2" class="txt-upper">
                        Recebemos de [ds_company_issuer_name] os produtos e serviços constantes na nota fiscal indicada
                        ao lado
                    </td>
                    <td rowspan="2" class="tserie txt-center">
                        <span class="font-12" style="margin-bottom: 5px;">NF-e</span>
                        <span>Nº [nl_invoice]</span>
                        <span>Série [ds_invoice_serie]</span>
                    </td>
                </tr>
                <tr>
                    <td style="width: 32mm">
                        <span class="nf-label">Data de recebimento</span>
                    </td>
                    <td style="width: 124.6mm">
                        <span class="nf-label">Identificação de assinatura do Recebedor</span>
                    </td>
                </tr>
            </tbody>
        </table>
        <hr class="hr-dashed" />
        <table cellpadding="0" cellspacing="0" border="1">
            <tbody>
                <tr>
                    <td rowspan="3" style="width: 30mm">
                        <img class="client_logo" src="" alt=""
                            onerror=" javascript:this.src='data:image/png;base64'" />
                    </td>
                    <td rowspan="3" style="width: 46mm; font-size: 7pt;" class="txt-center">
                        <span class="mb2 bold block">[ds_company_issuer_name]</span>
                        <span class="block">[ds_company_address]</span>
                        <span class="block">
                            [ds_company_neighborhood] - [nu_company_cep]
                        </span>
                        <span class="block">
                          """  + doc['NFe']['infNFe']['ide']['cUF'] + """ - """ + doc['NFe']['infNFe']['ide']['cNF'] + """ - Fone: [nl_company_phone_number]
                        </span>
                    </td>
                    <td rowspan="3" class="txtc txt-upper" style="width: 34mm; height: 29.5mm;">
                        <h3 class="title">Danfe</h3>
                        <p class="mb2">Documento auxiliar da Nota Fiscal Eletrônica </p>
                        <p class="entradaSaida mb2">
                            <span class="identificacao">
                                <span>[ds_code_operation_type]</span>
                            </span>
                            <span class="legenda">
                                <span>0 - Entrada</span>
                                <span>1 - Saída</span>
                            </span>
                        </p>
                        <p>
                            <span class="block bold">
                                <span>Nº</span>
                                <span>[nl_invoice]</span>
                            </span>
                            <span class="block bold">
                                <span>SÉRIE:</span>
                                <span>[ds_invoice_serie]</span>final
                            </span>
                            <span class="block">
                                <span>Página</span>
                                <span>[actual_page]</span>
                                <span>de</span>
                                <span>[total_pages]</span>
                            </span>
                        </p>
                    </td>
                    <td class="txt-upper" style="width: 85mm;">
                        <span class="nf-label">Controle do Fisco</span>
                        <span class="codigo">{BarCode}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="nf-label">CHAVE DE ACESSO</span>
                        <span class="bold block txt-center info">[ds_danfe]</span>
                    </td>
                </tr>
                <tr>
                    <td class="txt-center valign-middle">
                        <span class="block">Consulta de autenticidade no portal nacional da NF-e </span>
                        www.nfe.fazenda.gov.br/portal ou no site da Sefaz Autorizada.
                    </td>
                </tr>
            </tbody>
        </table>
        <!-- Natureza da Operação -->
        <table cellpadding="0" cellspacing="0" class="boxNaturezaOperacao no-top" border="1">
            <tbody>
                <tr>
                    <td>
                        <span class="nf-label">NATUREZA DA OPERAÇÃO</span>
                        <span class="info">[_ds_transaction_nature]</span>
                    </td>
                    <td style="width: 84.7mm;">
                        <span class="nf-label">[protocol_label]</span>
                        <span class="info">[ds_protocol]</span>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Inscrição -->
        <table cellpadding="0" cellspacing="0" class="boxInscricao no-top" border="1">
            <tbody>
                <tr>
                    <td>
                        <span class="nf-label">INSCRIÇÃO ESTADUAL</span>
                        <span class="info">[nl_company_ie]</span>
                    </td>
                    <td style="width: 67.5mm;">
                        <span class="nf-label">INSCRIÇÃO ESTADUAL DO SUBST. TRIB.</span>
                        <span class="info">[nl_company_ie_st]</span>
                    </td>
                    <td style="width: 64.3mm">
                        <span class="nf-label">CNPJ</span>
                        <span class="info">[nl_company_cnpj_cpf]</span>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Destinatário/Emitente -->
        <p class="area-name">Destinatário/Emitente</p>
        <table cellpadding="0" cellspacing="0" class="boxDestinatario" border="1">
            <tbody>
                <tr>
                    <td class="pd-0">
                        <table cellpadding="0" cellspacing="0" border="1">
                            <tbody>
                                <tr>
                                    <td>
                                        <span class="nf-label">NOME/RAZÃO SOCIAL</span>
                                        <span class="info">[ds_client_receiver_name]</span>
                                    </td>
                                    <td style="width: 40mm">
                                        <span class="nf-label">CNPJ/CPF</span>
                                        <span class="info">[nl_client_cnpj_cpf]</span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                    <td style="width: 22mm">
                        <span class="nf-label">DATA DE EMISSÃO</span>
                        <span class="info">[dt_invoice_issue]</span>
                    </td>
                </tr>
                <tr>
                    <td class="pd-0">
                        <table cellpadding="0" cellspacing="0" border="1">
                            <tbody>
                                <tr>
                                    <td>
                                        <span class="nf-label">ENDEREÇO</span>
                                        <span class="info">[ds_client_address]</span>
                                    </td>
                                    <td style="width: 47mm;">
                                        <span class="nf-label">BAIRRO/DISTRITO</span>
                                        <span class="info">[ds_client_neighborhood]</span>
                                    </td>
                                    <td style="width: 37.2 mm">
                                        <span class="nf-label">CEP</span>
                                        <span class="info">[nu_client_cep]</span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                    <td>
                        <span class="nf-label">DATA DE ENTR./SAÍDA</span>
                        <span class="info">[dt_input_output]</span>
                    </td>
                </tr>
                <tr>
                    <td class="pd-0">
                        <table cellpadding="0" cellspacing="0" style="margin-bottom: -1px;" border="1">
                            <tbody>
                                <tr>
                                    <td>
                                        <span class="nf-label">MUNICÍPIO</span>
                                        <span class="info">[ds_client_city_name]</span>
                                    </td>
                                    <td style="width: 34mm">
                                        <span class="nf-label">FONE/FAX</span>
                                        <span class="info">[nl_client_phone_number]</span>
                                    </td>
                                    <td style="width: 28mm">
                                        <span class="nf-label">UF</span>
                                        <span class="info"></span>
                                    </td>
                                    <td style="width: 51mm">
                                        <span class="nf-label">INSCRIÇÃO ESTADUAL</span>
                                        <span class="info">[ds_client_ie]</span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                    <td>
                        <span class="nf-label">HORA ENTR./SAÍDA</span>
                        <span id="info">[hr_input_output]</span>
                    </td>
                </tr>
            </tbody>
        </table>
        <!-- Fatura -->
        <div class="boxFatura">
            <p class="area-name">Fatura</p>
            [duplicates]
        </div>

        <!-- Calculo do Imposto -->
        <p class="area-name">Calculo do imposto</p>
        <div class="wrapper-table">
            <table cellpadding="0" cellspacing="0" border="1" class="boxImposto">
                <tbody>
                    <tr>
                        <td>
                            <span class="nf-label label-small">BASE DE CÁLC. DO ICMS</span>
                            <span class="info">[tot_bc_icms]</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO ICMS</span>
                            <span class="info">[tot_icms]</span>
                        </td>
                        <td>
                            <span class="nf-label label-small" style="font-size: 4pt;">BASE DE CÁLC. DO ICMS ST</span>
                            <span class="info">[tot_bc_icms_st]</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO ICMS ST</span>
                            <span class="info">[tot_icms_st]</span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. IMP. IMPORTAÇÃO</span>
                            <span class="info"></span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. ICMS UF REMET.</span>
                            <span class="info"></span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO FCP</span>
                            <span class="info">[tot_icms_fcp]</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO PIS</span>
                            <span class="info"></span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. TOTAL DE PRODUTOS</span>
                            <span class="info">[vl_total_prod]</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span class="nf-label">VALOR DO FRETE</span>
                            <span class="info">[vl_shipping]</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO SEGURO</span>
                            <span class="info">[vl_insurance]</span>
                        </td>
                        <td>
                            <span class="nf-label">DESCONTO</span>
                            <span class="info">[vl_discount]</span>
                        </td>
                        <td>
                            <span class="nf-label">OUTRAS DESP.</span>
                            <span class="info">[vl_other_expense]</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO IPI</span>
                            <span class="info">[tot_total_ipi_tax]</span>
                        </td>
                        <td>
                            <span class="nf-label">V. ICMS UF DEST.</span>
                            <span class="info"></span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. APROX. DO TRIBUTO</span>
                            <span class="info">{ApproximateTax}</span>
                        </td>
                        <td>
                            <span class="nf-label label-small">VALOR DA CONFINS</span>
                            <span class="info"></span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. TOTAL DA NOTA</span>
                            <span class="info">[vl_total]</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <!-- Transportador/Volumes transportados -->
        <p class="area-name">Transportador/volumes transportados</p>
        <table cellpadding="0" cellspacing="0" border="1">
            <tbody>
                <tr>
                    <td>
                        <span class="nf-label">RAZÃO SOCIAL</span>
                        <span class="info">[ds_transport_carrier_name]</span>
                    </td>
                    <td class="freteConta" style="width: 32mm">
                        <span class="nf-label">FRETE POR CONTA</span>
                        <div class="border">
                            <span class="info">[ds_transport_code_shipping_type]</span>
                        </div>
                        <p>0 - Emitente</p>
                        <p>1 - Destinatário</p>
                    </td>
                    <td style="width: 17.3mm">
                        <span class="nf-label">CÓDIGO ANTT</span>
                        <span class="info">[ds_transport_rntc]</span>
                    </td>
                    <td style="width: 24.5mm">
                        <span class="nf-label">PLACA</span>
                        <span class="info">[ds_transport_vehicle_plate]</span>
                    </td>
                    <td style="width: 11.3mm">
                        <span class="nf-label">UF</span>
                        <span class="info">[ds_transport_vehicle_uf]</span>
                    </td>
                    <td style="width: 29.5mm">
                        <span class="nf-label">CNPJ/CPF</span>
                        <span class="info">[nl_transport_cnpj_cpf]</span>
                    </td>
                </tr>
            </tbody>
        </table>

        <table cellpadding="0" cellspacing="0" border="1" class="no-top">
            <tbody>
                <tr>
                    <td class="field endereco">
                        <span class="nf-label">ENDEREÇO</span>
                        <span class="content-spacer info">[ds_transport_address]</span>
                    </td>
                    <td style="width: 32mm">
                        <span class="nf-label">MUNICÍPIO</span>
                        <span class="info">[ds_transport_city]</span>
                    </td>
                    <td style="width: 31mm">
                        <span class="nf-label">UF</span>
                        <span class="info">[ds_transport_uf]</span>
                    </td>
                    <td style="width: 51.4mm">
                        <span class="nf-label">INSC. ESTADUAL</span>
                        <span class="info">[ds_transport_ie]</span>
                    </td>
                </tr>
            </tbody>
        </table>
        <table cellpadding="0" cellspacing="0" border="1" class="no-top">
            <tbody>
                <tr>
                    <td class="field quantidade">
                        <span class="nf-label">QUANTIDADE</span>
                        <span class="content-spacer info">[nu_transport_amount_transported_volumes]</span>
                    </td>
                    <td style="width: 31.4mm">
                        <span class="nf-label">ESPÉCIE</span>
                        <span class="info">[ds_transport_type_volumes_transported]</span>
                    </td>
                    <td style="width: 31mm">
                        <span class="nf-label">MARCA</span>
                        <span class="info">[ds_transport_mark_volumes_transported]</span>
                    </td>
                    <td style="width: 31.5mm">
                        <span class="nf-label">NUMERAÇÃO</span>
                        <span class="info">[ds_transport_number_volumes_transported]</span>
                    </td>
                    <td style="width: 31.5mm">
                        <span class="nf-label">PESO BRUTO</span>
                        <span class="info">[vl_transport_gross_weight]</span>
                    </td>
                    <td style="width: 32.5mm">
                        <span class="nf-label">PESO LÍQUIDO</span>
                        <span class="info">[vl_transport_net_weight]</span>
                    </td>
                </tr>
            </tbody>
        </table>
        <!-- Dados do produto/serviço -->
        <p class="area-name">Dados do produto/serviço</p>
        <div class="wrapper-border">
            <table cellpadding="0" cellspacing="0" border="1" class="boxProdutoServico">
                <thead class="listProdutoServico" id="table">
                    <tr class="titles">
                        <th class="cod" style="width: 15.5mm">CÓDIGO</th>
                        <th class="descrit" style="width: 66.1mm">DESCRIÇÃO DO PRODUTO/SERVIÇO</th>
                        <th class="ncmsh">NCMSH</th>
                        <th class="cst">CST</th>
                        <th class="cfop">CFOP</th>
                        <th class="un">UN</th>
                        <th class="amount">QTD.</th>
                        <th class="valUnit">VLR.UNIT</th>
                        <th class="valTotal">VLR.TOTAL</th>
                        <th class="bcIcms">BC ICMS</th>
                        <th class="valIcms">VLR.ICMS</th>
                        <th class="valIpi">VLR.IPI</th>
                        <th class="aliqIcms">ALIQ.ICMS</th>
                        <th class="aliqIpi">ALIQ.IPI</th>
                    </tr>
                    <tr>
                        <td>1234</td>
                        <td>Comida</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                        <td>1</td>
                    </tr>
                </thead>
                <tbody>
                    [items]
                </tbody>
            </table>
        </div>
        <!-- Calculo de ISSQN -->
        <p class="area-name">Calculo do issqn</p>
        <table cellpadding="0" cellspacing="0" border="1" class="boxIssqn">
            <tbody>
                <tr>
                    <td class="field inscrMunicipal">
                        <span class="nf-label">INSCRIÇÃO MUNICIPAL</span>
                        <span class="info txt-center">[ds_company_im]</span>
                    </td>
                    <td class="field valorTotal">
                        <span class="nf-label">VALOR TOTAL DOS SERVIÇOS</span>
                        <span class="info txt-right">[vl_total_serv]</span>
                    </td>
                    <td class="field baseCalculo">
                        <span class="nf-label">BASE DE CÁLCULO DO ISSQN</span>
                        <span class="info txt-right">[tot_bc_issqn]</span>
                    </td>
                    <td class="field valorIssqn">
                        <span class="nf-label">VALOR DO ISSQN</span>
                        <span class="info txt-right">[tot_issqn]</span>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Dados adicionais -->
        <p class="area-name">Dados adicionais</p>
        <table cellpadding="0" cellspacing="0" border="1" class="boxDadosAdicionais">
            <tbody>
                <tr>
                    <td class="field infoComplementar">
                        <span class="nf-label">INFORMAÇÕES COMPLEMENTARES</span>
                        <span>[ds_additional_information]</span>
                    </td>
                    <td class="field reservaFisco" style="width: 85mm; height: 24mm">
                        <span class="nf-label">RESERVA AO FISCO</span>
                        <span></span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
""")
file.close()
#pdfkit.from_file('nfe.html', 'nfe.pdf', configuration=config)



        
