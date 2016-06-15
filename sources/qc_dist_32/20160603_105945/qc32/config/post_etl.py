#expecting args
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32com.client
	
def send_email(subj):
	assert args.email_to, 'Email_to is not set'
	if 1:
		gmail_user = 'data.buddy.test@gmail.com' 
		gmail_pwd = "data;buddy;test"
		FROM = 'alex_buz@yahoo.com'
		TO = args.email_to.split(';') #must be a list
		SUBJECT = subj #'QC job "%s" completed.' % args.job_name
		TEXT = "<table><th align=left>%s:<th align=left>%s"  % (args.job_name.upper(), args.copy_vector.upper())
		for k,val in sorted(args.__dict__.items()):
			if 'passwd' not in k and 'to_db' not in k and 'from_db' not in k:
				TEXT='%s\n<tr><td>%s:<td>%s</tr>' % (TEXT,k, val)
		# Prepare actual message
		msg = MIMEMultipart('alternative')
		msg['Subject'] = SUBJECT
		msg['From'] = FROM
		msg['To'] = ", ".join(TO)
		message = "%s</table>" % TEXT
		part1 = MIMEText(message, 'html')
		msg.attach(part1)
		try:
			#server = smtplib.SMTP(SERVER) 
			server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
			server.ehlo()
			server.starttls()
			server.login(gmail_user, gmail_pwd)
			server.sendmail(FROM, TO, msg.as_string())
			#server.quit()
			server.close()
			print 'successfully sent the mail'
			print subj
		except:
			print "failed to send mail"
			raise
def	execute(status_title):
	if args.email_to:
		print 'Sending mail...'
		send_email(status_title)	
		print 'Done.'
if __name__=='__main__':
	if 1:
		send_email()
