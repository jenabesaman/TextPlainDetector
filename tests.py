# import random
#
# random.randint(1,5)
#
# print(random.randint(1,5))
# import string
#
# [''.join(random.choices(string.ascii_letters, k=random.randint(1,7))) for _ in range(2)]
#
# random_strings_complex = [''.join(random.choices(string.ascii_letters + string.digits + '@#%&*', k=random.randint(1,15))) for _ in range(2)]
#
# persian_words = set(read_file_as_text('/content/drive/MyDrive/TextPlainDetector/persian_words.txt', ['utf-8', 'windows-1256']).replace('غغغ', ' ').split())

import TextPlainDetector
text=""""ببا سلام و احترام
    بدینوسیله به استحضار آن مقام محترم می رساند نظر به  افزایش روزافزون نرخ تورم و تحمیل آن به پیکر قشر حقوق بگیر، تناسب دخل و خرج خانواده را به نحوی بر هم ریخته که به‌هیچ‌عنوان دریافتی جاری حداقل نیازهای اولیه را نیز تأمین نمی‌نماید، لذا خواهشمند است با توجه به این که این‌جانب منبع درآمد دیگری غیر از این شرکت برای تأمین معاش خود ندارم، عنایت فرموده دستور تجدید نظر در حقوق دریافتی بنده را امر به ابلاغ فرمایید."""
obj = TextPlainDetector.TextPlainDetector(text=text)

print(obj)