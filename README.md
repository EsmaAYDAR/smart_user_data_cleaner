# akıllı veri temizleme projesi (smart_user_data_cleaner)
Python string metotları ile veri ön işleme çalışması

Bu projede ham ve düzensiz (kirli) verilerin Python kullanarak analiz edilebilir hale getirilmesini amaçladım.

## Proje Hakkında
Kullanıcılardan gelen hatalı girişleri (fazla boşluklar, karışık büyük/küçük harf kullanımı vb.) otomatik olarak temizleyen düzenleyen bir çalışma.

## Kullanılan Teknolojiler ve Metotlar
Proje kapsamında aşağıdaki Python metotları aktif olarak kullanılmıştır:

- strip(): Verinin başındaki ve sonundaki gereksiz boşlukları temizledim.
- split(): Veriyi belirli bir ayırıcıya göre parçalara ayırdım.
- title(): İsim ve soyisim verilerini baş harfi büyük formatına getirdim.
- lower(): Email adresi gibi verileri standartlaştırmak için ve projede intendiği için gerekli verideki tüm harfleri küçülttüm.

##  Örnek Çıktı
**Ham Veri:** = "  AhMeT  yILMAZ ;  23 ;  1.78 ;  ahmetYILMAZ@GMAIL.Com   "
**Temizlenmiş Veri:** = ['Ahmet Yilmaz'; '23'; '1.78';'ahm]![çıktı day1](https://github.com/user-attachments/assets/22f688ff-92f0-4f5b-8e3b-90ed976e1a6c)
