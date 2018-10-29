import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class EmailUtil:

    @staticmethod
    def send(content):
        sender = 'springbootadmin163@163.com'
        user = '1227602328@qq.com'

        server = smtplib.SMTP('smtp.163.com', 25)
        server.login(sender, 'spring123')

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["Blog App", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["Dear", user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "Blog App Notify"  # 邮件的主题，也可以说是标题

        server.sendmail(sender, [user], msg.as_string())

        server.quit()


if __name__ == '__main__':
    EmailUtil.send('hello it`s me!')
