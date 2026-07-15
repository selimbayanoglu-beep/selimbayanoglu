from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont('DejaVu', FONT_DIR + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold', FONT_DIR + 'DejaVuSans-Bold.ttf'))

PAGE = landscape(A4)
doc = SimpleDocTemplate(
    "ads_optimizasyon_raporu.pdf",
    pagesize=PAGE,
    leftMargin=10*mm, rightMargin=10*mm, topMargin=8*mm, bottomMargin=8*mm,
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('TitleX', parent=styles['Title'], fontName='DejaVu-Bold', fontSize=22, leading=25, spaceAfter=2)
meta_style = ParagraphStyle('MetaX', parent=styles['Normal'], fontName='DejaVu', fontSize=16, leading=18, textColor=colors.grey)
h2 = ParagraphStyle('H2', parent=styles['Heading2'], fontName='DejaVu-Bold', fontSize=18, leading=20, spaceBefore=6, spaceAfter=2)
body = ParagraphStyle('BodyX', parent=styles['Normal'], fontName='DejaVu', fontSize=16, leading=19)
small_note = ParagraphStyle('SmallNote', parent=styles['Normal'], fontName='DejaVu', fontSize=16, leading=18, textColor=colors.grey)

story = []

story.append(Paragraph("Google Ads Optimizasyon Raporu", title_style))
story.append(Paragraph("Hesap: 168-356-3917 &nbsp;|&nbsp; Veri aralığı: 13-15 Temmuz 2026 (hesap 3 günlük) &nbsp;|&nbsp; Rapor tarihi: 15 Temmuz 2026", meta_style))
story.append(Spacer(1, 4))

# 1. Hesap özeti
story.append(Paragraph("1. Hesap Özeti (13-15 Temmuz)", h2))
data1 = [
    ["Kampanya", "Tür / Strateji", "Bütçe", "Tıklama", "Dönüşüm", "Maliyet", "Maliyet/Dönüşüm"],
    ["Website traffic-Search-1", "Arama - Dönüşüm Maks.*", "₺250/gün", "21", "20,00", "₺290,61", "₺14,53"],
    ["aile danışmanlığı", "Akıllı (otomatik)", "₺501,60/gün", "80", "80,50", "₺272,84", "₺3,39"],
    ["TOPLAM", "-", "₺751,60/gün", "101", "100,50", "₺563,44", "₺5,61"],
]
t1 = Table(data1, colWidths=[70*mm, 55*mm, 27*mm, 22*mm, 24*mm, 28*mm, 47*mm])
t1.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'DejaVu'),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a73e8')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTSIZE', (0,0), (-1,-1), 11.5),
    ('FONTNAME', (0,0), (-1,0), 'DejaVu-Bold'),
    ('FONTNAME', (0,-1), (-1,-1), 'DejaVu-Bold'),
    ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#eef3fc')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.HexColor('#f7f9fc')]),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(t1)
story.append(Paragraph("*Bugün Maliyet Maks. Tıklama'dan Maks. Dönüşüm'e çevrildi (aşağıda madde 2).", small_note))
story.append(Spacer(1, 4))

# 2. Uygulanan değişiklikler
story.append(Paragraph("2. Uygulanan Değişiklikler", h2))
data2 = [
    ["#", "Aksiyon", "Kampanya", "Gerekçe"],
    ["1", "Teklif stratejisi değiştirildi:\nTıklama Maks. → Dönüşüm Maks.", "Website traffic-Search-1",
     "Kampanya hedefi zaten 'form/satın alma' olarak\ntanımlıydı ama teklif stratejisi tıklamayı\noptimize ediyordu - hedef ile strateji uyumsuzdu."],
    ["2", "8 negatif anahtar kelime eklendi\n(reklam grubu düzeyinde)", "Website traffic-Search-1",
     "Alakasız/düşük niyetli arama terimleri:\nkişi adları, bilgi amaçlı sorgular, B2B sorgusu\n(bkz. madde 3)."],
    ["3", "Bütçe dağılımı: değiştirilmedi", "Her ikisi", "Her iki kampanya da bütçe tavanının\nyaklaşık %35-55'ini kullanıyor - darboğaz\nbütçe değil, talep/skor. Bütçe kaydırmak\nşu an sonucu değiştirmez (madde 4)."],
]
t2 = Table(data2, colWidths=[9*mm, 72*mm, 62*mm, 130*mm])
t2.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'DejaVu'),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a73e8')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'DejaVu-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 11.5),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7f9fc')]),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(t2)
story.append(Spacer(1, 4))

# 3. Eklenen negatif kelimeler + 4. bulgular yan yana değil, alt alta kısa
story.append(Paragraph("3. Eklenen Negatif Anahtar Kelimeler (bugün, toplam 8)", h2))
data3 = [
    ["damla gülmez", "why do we get angry", "i just get so nervous", "aile danışmanı arayan kurumlar"],
    ["aile dizimi terapisi video", "gezgin psikolog", "maladaptive daydreaming", "partner quiz"],
]
t3 = Table(data3, colWidths=[68*mm, 68*mm, 68*mm, 69*mm])
t3.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'DejaVu'),
    ('FONTSIZE', (0,0), (-1,-1), 11),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cccccc')),
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fff4e5')),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(t3)
story.append(Paragraph("Not: Hesapta önceden (bugün erken saatte) 9 terim daha hariç tutulmuş ve öneriler panelinden 1 gereksiz anahtar kelime kaldırılmıştı - bu rapor yalnızca bu oturumda eklenenleri listeler.", small_note))
story.append(Spacer(1, 4))

# 4. Kritik bulgu
story.append(Paragraph("4. Dikkat: Doğrulanması Gereken Bulgu", h2))
data4 = [
    ["Website traffic-Search-1: %95,2 dönüşüm oranı (21 tıklamada 20 dönüşüm)"],
    ["aile danışmanlığı: %100,6 dönüşüm oranı (80 tıklamada 80,5 dönüşüm)"],
]
t4 = Table(data4, colWidths=[273*mm])
t4.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'DejaVu'),
    ('FONTSIZE', (0,0), (-1,-1), 14),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cccccc')),
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fdecea')),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(t4)
story.append(Paragraph(
    "Neredeyse her tıklamanın dönüşüme gitmesi istatistiksel olarak sıra dışı - iyi bir haber gibi görünse de tipik olarak <b>çifte "
    "sayım</b> (dönüşüm etiketinin sayfa yenilemede tekrar tetiklenmesi) veya <b>yanlış yapılandırılmış dönüşüm işlemi</b> "
    "işaretidir. Google Ads Etiket Yardımcısı (Tag Assistant) ile canlı test edilmeden bu rakamlara dayanarak bütçe artışına "
    "gidilmemeli. Espri payı: bir kampanyanın dönüşüm oranı %100'ü geçiyorsa, ya ürününüz inanılmaz ya da etiketiniz aynı "
    "siparişi iki kere kutluyor.",
    body
))
story.append(Spacer(1, 4))

# 5. Sonraki adımlar
story.append(Paragraph("5. Önerilen Sonraki Adımlar", h2))
data5 = [
    ["Dönüşüm etiketini doğrula (çifte sayım riski) - önce buna bak"],
    ["Yeni teklif stratejisi (Dönüşüm Maks.) için en az 7-14 gün / ~30 dönüşüm bekle, sonra tekrar değerlendir"],
    ["Veri yeterli hacme ulaşınca (30+ dönüşüm/kampanya) anahtar kelime bazlı budama ve hedef CPA belirleme"],
]
t5 = Table(data5, colWidths=[273*mm])
t5.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'DejaVu'),
    ('FONTSIZE', (0,0), (-1,-1), 14),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cccccc')),
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#e6f4ea')),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(t5)

doc.build(story)
print("done")
