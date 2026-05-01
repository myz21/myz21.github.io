# Proje Çalıştırma Talimatları

Bu proje, Next.js ile oluşturulmuş statik bir web sitesidir. Projeyi yerel olarak çalıştırmak için bir statik dosya sunucusu kullanmanız gerekmektedir.

## Yöntem 1: `serve` Kullanarak (Önerilen)

Eğer Node.js ve npm yüklüyse, `serve` paketini kullanarak projeyi kolayca çalıştırabilirsiniz.

1. `serve` paketini global olarak yükleyin (eğer yüklü değilse):
   ```bash
   npm install -g serve
   ```

2. Proje dizinine gidin:
   ```bash
   cd /home/neo/Downloads/portfolio-pi-umber-47.vercel.app
   ```

3. Projeyi çalıştırın:
   ```bash
   serve .
   ```

   Bu komut, projeyi genellikle `http://localhost:3000` adresinde başlatacaktır. Tarayıcınızdan bu adresi ziyaret ederek siteyi görüntüleyebilirsiniz.

## Yöntem 2: Python'ın Basit HTTP Sunucusunu Kullanarak

Eğer Python yüklüyse, Python'ın yerleşik HTTP sunucusunu kullanabilirsiniz.

1. Proje dizinine gidin:
   ```bash
   cd /home/neo/Downloads/portfolio-pi-umber-47.vercel.app
   ```

2. HTTP sunucusunu başlatın:
   ```bash
   python3 -m http.server
   ```

   Bu komut, projeyi genellikle `http://localhost:8000` adresinde başlatacaktır. Tarayıcınızdan bu adresi ziyaret ederek siteyi görüntüleyebilirsiniz.
