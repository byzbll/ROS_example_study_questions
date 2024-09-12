# ROS_example_study_questions

## orn1 Dosyaları
Orn1 dosyaları, bir yayıncı ve bir abone olmak üzere iki ROS düğümü içerir. Yayıncı, rastgele tamsayılar üretir ve bunları bir ROS topiği üzerinden yayınlar. Abone ise aynı topiğe abone olarak yayınlanan sayıları dinler ve ekrana yazdırır.

### Dosyalar:
- **number_publisher_orn1.py**: 0-100 arasında rastgele sayılar üretir ve `/random_number` topiğine yayın yapar.
- **number_subscriber_orn1.py**: `/random_number` topiğine abone olur ve aldığı sayıları ekrana yazdırır.

### Example Output:
```bash
Publisher --->> [INFO] [1634556347.456789]: Publishing: 42  
[INFO] [1634556348.456789]: Publishing: 77  
Subscriber --->> [INFO] [1634556347.456789]: Received: 42  
[INFO] [1634556348.456789]: Received: 77  

orn2 dosyaları, bir sayı yayınlayıcı (publisher), bu sayıyı bir sabit ile çarpan (multiplier), ve sonucu dinleyen (subscriber) olmak üzere üç adet ROS düğümünden oluşur. Projede, bir sabit sayı yayınlanır, bu sayı belirli bir sabit ile çarpılır ve sonuç başka bir düğüm tarafından dinlenir ve ekrana yazdırılır.

## Dosyalar
1. `number_publisher_orn2.py`: Sabit bir sayı (5) üretir ve `/fixed_number` topiğine yayın yapar.
2. `multiply_subscriber_orn2.py`: `/fixed_number` topiğinden gelen sayıyı alır, bu sayıyı bir sabit ile (7) çarpar ve sonucu `/multiplied_number` topiğine yayınlar.
3. `result_subscriber_orn2.py`: `/multiplied_number` topiğine abone olur ve çarpılmış sonucu dinler.

Example Output:
Number Publisher --->>
[INFO] [1634556347.456789]: Publishing: 5
Multiply Subscriber --->>
[INFO] [1634556347.456789]: Multiplying 5 by 7 to get 35
Result Subscriber --->> 
[INFO] [1634556347.456789]: Result: 35

orn3 dosyaları, sabit bir sayı (`fixed_number`) ve bir isimle ilişkilendirilmiş bir sayının (`name_number`) yayınlandığı, ardından bu iki sayının çarpımının hesaplandığı ve ismin de terminale yazdırıldığı bir ROS uygulamasıdır.

## Dosyalar
1. `fixed_number_publisher_orn3.py`: Sabit bir sayı (3) üretir ve `/fixed_number` topiğine yayın yapar.
2. `name_number_multiplier_orn3.py`: `/fixed_number`, `/name_string` ve `/name_number` topiklerinden gelen verileri dinler, sabit sayı ile isim sayısını çarpar ve sonucu terminale yazdırır.
3. `name_number_publisher_orn3.py`: Bir isim (`Beyza`) ve bu isme karşılık gelen sayıyı (`3`) `/name_string` ve `/name_number` topiklerine yayın yapar.

Example Output:
Fixed Number Publisher --->>
[INFO] [1634556347.456789]: Publishing fixed number: 3
Name-Number Publisher --->>
[INFO] [1634556348.456789]: Publishing name: Beyza and number: 3
Name-Number Multiplier --->> 
[INFO] [1634556349.456789]: Received name: Beyza
[INFO] [1634556349.456789]: The product of 3 and 3 is 9

my_first_node.py dosyası, basit bir ROS düğümünün çalışma şeklini ve log seviyelerini göstermek amacıyla oluşturulmuştur. Düğüm, belirli bir frekansta terminale "Hello" mesajı yazdırır ve ROS log seviyelerinin nasıl kullanılacağını gösterir.
test_node düğümü, basit bir ROS düğümü başlatır, belirli aralıklarla log mesajları yayınlar ve log seviyelerini kullanarak bilgi, uyarı ve hata mesajları nasıl yazdırılır gösterir.


